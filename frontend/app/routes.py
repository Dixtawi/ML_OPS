from flask import Blueprint, request, render_template, current_app, url_for, redirect
import json
import locale
from datetime import datetime
import os
from instance.config import MODEL_PATH
import joblib
from sklearn.preprocessing import StandardScaler

routes = Blueprint('routes', __name__)

model = joblib.load(MODEL_PATH)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        area = int(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        stories = int(request.form['stories'])
        mainroad = 1 if request.form['mainroad'] == 'yes' else 0
        guestroom = 1 if request.form['guestroom'] == 'yes' else 0
        basement = 1 if request.form['basement'] == 'yes' else 0
        hotwaterheating = 1 if request.form['watheat'] == 'yes' else 0
        airconditioning = 1 if request.form['aircond'] == 'yes' else 0
        parking = int(request.form['parkings'])
        prefarea = 1 if request.form['prefarea'] == 'yes' else 0
        furnishingstatus = request.form['furnishingstatus']
        
        furnishing_map = {'furnished': 0, 'semi-furnished': 1, 'unfurnished': 2}
        furnishingstatus = furnishing_map[furnishingstatus]

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
        print(input_data)
        try:
            predicted_price = round(model.predict([input_data])[0])
        except Exception as e:
            print(f"Error loading model or predicting: {e}")
        
        return render_template('prediction.html', predicted_price=predicted_price, input_data=input_data)
    else:
        return render_template('prediction.html')