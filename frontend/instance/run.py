import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app
from config import API_PORT, API_HOST, DEBUG


app = create_app()

if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT, debug=DEBUG)
