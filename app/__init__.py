from flask import Flask
from config import config_options


def create_app(config_name):
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions

    # Registering the BluePrint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting the config
    from .request import configure_request
    configure_request(app)

    return app
