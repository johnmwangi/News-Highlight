from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)
    bootsrap = Bootstrap(app)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)



    #will add the views and forms

    return app
