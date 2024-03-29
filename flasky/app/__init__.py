#!/usr/bin/python3

"""应用包的构造文件"""

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment 
from flask_sqlalchemy import SQLAlchemy 
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown
from flask_debugtoolbar import DebugToolbarExtension 
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager() 
login_manager.login_view = 'auth.login' 
pagedown = PageDown()
toolbar = DebugToolbarExtension()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app) 
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    toolbar.init_app(app)
   
    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth') 

    return app

    
