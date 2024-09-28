from flask import Blueprint, request, render_template, current_app, url_for, redirect
import json
import locale
from datetime import datetime
import os
from instance.config import MODEL_PATH
import joblib

routes = Blueprint('routes', __name__)
print(MODEL_PATH)
model = joblib.load(MODEL_PATH)

@routes.route('/')
def home():
    return render_template('prediction.html')

@routes.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        furnishing_map = {'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2}
        strings_map = {'yes': 1, 'no': 0}
        
        area = int(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        stories = int(request.form['stories'])
        mainroad = strings_map[request.form['mainroad']]
        guestroom = strings_map[request.form['guestroom']]
        basement = strings_map[request.form['basement']]
        hotwaterheating = strings_map[request.form['watheat']]
        airconditioning = strings_map[request.form['aircond']]
        parking = int(request.form['parkings'])
        prefarea = strings_map[request.form['prefarea']]
        furnishingstatus = furnishing_map[request.form['furnishingstatus']]
        

        input_data = [
            area,
            bedrooms,
            bathrooms,
            stories,
            mainroad,
            guestroom,
            basement,
            hotwaterheating,
            airconditioning,
            parking,
            prefarea,
            furnishingstatus
        ]
        predicted_price = None
        try:
            predicted_price = round(model.predict([input_data])[0])
            
            input_data_origine = {
                'area': area,
                'bedrooms': bedrooms,
                'bathrooms': bathrooms,
                'stories': stories,
                'mainroad': 'yes' if mainroad == 1 else 'no',
                'guestroom': 'yes' if guestroom == 1 else 'no',
                'basement': 'yes' if basement == 1 else 'no',
                'hotwaterheating': 'yes' if hotwaterheating == 1 else 'no',
                'airconditioning': 'yes' if airconditioning == 1 else 'no',
                'parking': parking,
                'prefarea': 'yes' if prefarea == 1 else 'no',
                'furnishingstatus': [key for key, value in furnishing_map.items() if value == furnishingstatus][0]
            }
            
            input_data = map(input_data, lambda x: str(x))
        except Exception as e:
            print(f"Error loading model or predicting: {e}")
        
        return render_template('prediction.html', predicted_price=predicted_price, input_data=input_data_origine)
    else:
        return render_template('prediction.html')