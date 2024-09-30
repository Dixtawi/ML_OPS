from flask import Flask
from .routes import routes
import os
import ssl
from prometheus_flask_exporter import PrometheusMetrics

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_pyfile('../instance/config.py')
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.register_blueprint(routes)
    metrics = PrometheusMetrics(app)
    
    context = None
    #if not app.debug:
    #    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    #    context.load_cert_chain('certificates/cert.pem', 'certificates/key.pem')
    
    return app, context
