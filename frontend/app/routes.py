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

@routes.route('/prediction')
def prediction():
    model = {}
    # with open(MODEL_PATH, 'r') as file:
    #     model = json.load(file)
    return render_template('prediction.html', model=model)
    