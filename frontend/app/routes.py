from flask import Blueprint, request, render_template, current_app, url_for, redirect
import json
import locale
from datetime import datetime
import os
from instance.config import DEBUG

routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    return render_template('index.html')

