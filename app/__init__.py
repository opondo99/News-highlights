from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap



def create_app(config_name):
        
    #Initializing the application
    app = Flask(__name__)

    # App configurations
    app.config.from_object(config_options[config_name])

    # seting config
    from .requests import configure_request
    configure_request(app)

    # Initializing flask Extensions
    bootstrap = Bootstrap(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.main import views,errors

    return app