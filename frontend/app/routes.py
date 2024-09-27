from flask import Blueprint, request, render_template, current_app, url_for, redirect
import json
import locale
from datetime import datetime
import os
from instance.config import DEBUG, MODEL_PATH

routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        area = request.form['area']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        stories = request.form['stories']
        mainroad = 1 if request.form['mainroad'] == 'yes' else 0
        guestroom = 1 if request.form['guestroom'] == 'yes' else 0
        basement = 1 if request.form['basement'] == 'yes' else 0
        hotwaterheating = 1 if request.form['watheat'] == 'yes' else 0
        airconditioning = 1 if request.form['aircond'] == 'yes' else 0
        parking = request.form['parkings']
        prefarea = 1 if request.form['prefarea'] == 'yes' else 0
        furnishingstatus = request.form['furnishingstatus']
        
        furnishing_map = {'unfurnished': 0, 'semi-furnished': 1, 'furnished': 2}
        furnishingstatus = furnishing_map[furnishingstatus]

        input_data = {
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

        model = {}
        predicted_price = None
        try:
            # Exemple de chargement du modèle
            # with open(MODEL_PATH, 'r') as file:
            #     model = json.load(file)
            
            # Appeler la fonction de prédiction du modèle
            # predicted_price = model.predict(input_data)
            
            predicted_price = 100000  # Placeholder
        except Exception as e:
            print(f"Error loading model or predicting: {e}")
        
        return render_template('prediction.html', predicted_price=predicted_price, input_data=input_data)
    else:
        return render_template('prediction.html')