from flask import Blueprint, request, render_template, current_app, url_for, redirect, abort
import json
import locale
from datetime import datetime
import os
from instance.config import MODEL_PATH
import joblib
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import ssl
from werkzeug.exceptions import BadRequest
from prometheus_client import Summary
import time

routes = Blueprint('routes', __name__)
model = joblib.load(MODEL_PATH)
limiter = Limiter(key_func=get_remote_address, default_limits=["100 per hour"])
REQUEST_TIME = Summary('api_request_processing_seconds', 'Time spent processing request')


@routes.route('/')
@limiter.limit("10 per minute")
def home():
    return render_template('prediction.html')

def validate_input(form_data):
    try:
        area = int(form_data['area'])
        bedrooms = int(form_data['bedrooms'])
        bathrooms = int(form_data['bathrooms'])
        stories = int(form_data['stories'])
        parking = int(form_data['parkings'])

        furnishing_map = {'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2}
        strings_map = {'yes': 1, 'no': 0}

        mainroad = strings_map[form_data['mainroad']]
        guestroom = strings_map[form_data['guestroom']]
        basement = strings_map[form_data['basement']]
        hotwaterheating = strings_map[form_data['watheat']]
        airconditioning = strings_map[form_data['aircond']]
        prefarea = strings_map[form_data['prefarea']]
        furnishingstatus = furnishing_map[form_data['furnishingstatus']]

        return {
            'area': area,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'stories': stories,
            'mainroad': mainroad,
            'guestroom': guestroom,
            'basement': basement,
            'hotwaterheating': hotwaterheating,
            'airconditioning': airconditioning,
            'parking': parking,
            'prefarea': prefarea,
            'furnishingstatus': furnishingstatus
        }
    except (KeyError, ValueError) as e:
        raise BadRequest(f"Invalid input: {e}")





@REQUEST_TIME.time()
@routes.route('/prediction', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def prediction():
    if request.method == 'POST':
        if request.content_type != 'application/x-www-form-urlencoded':
            abort(400, description="Bad Request: Content-Type must be application/x-www-form-urlencoded")
        try:
            input_data = validate_input(request.form)

            predicted_price = round(model.predict([list(input_data.values())])[0])

            input_data_origine = {
                'area': input_data['area'],
                'bedrooms': input_data['bedrooms'],
                'bathrooms': input_data['bathrooms'],
                'stories': input_data['stories'],
                'mainroad': 'yes' if input_data['mainroad'] == 1 else 'no',
                'guestroom': 'yes' if input_data['guestroom'] == 1 else 'no',
                'basement': 'yes' if input_data['basement'] == 1 else 'no',
                'hotwaterheating': 'yes' if input_data['hotwaterheating'] == 1 else 'no',
                'airconditioning': 'yes' if input_data['airconditioning'] == 1 else 'no',
                'parking': input_data['parking'],
                'prefarea': 'yes' if input_data['prefarea'] == 1 else 'no',
                'furnishingstatus': 'furnished' if input_data['furnishingstatus'] == 0 else (
                    'semi-furnished' if input_data['furnishingstatus'] == 1 else 'unfurnished')
            }
        except BadRequest as e:
            return render_template('prediction.html', error=str(e))

        return render_template('prediction.html', predicted_price=predicted_price, input_data=input_data_origine)

    return render_template('prediction.html')