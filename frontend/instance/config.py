import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', '..', 'model', 'model.pkl')
API_PORT = 5000
API_HOST = '0.0.0.0'
DEBUG = False
DEBUG_METRICS = 1

