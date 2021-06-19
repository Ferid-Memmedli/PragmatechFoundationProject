from flask import Flask,abort,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager,UserMixin, login_manager,login_user,current_user,logout_user

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/database.db'
app.config['UPLOAD_PATH'] ='admin/static/upload'

db = SQLAlchemy(app) 
migrate = Migrate(app, db, render_as_batch=True)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
login_manager=LoginManager(app)
# login_manager.init_app(app)

import models
import forms
from app.routes import *
app.register_blueprint(blog)
import admin
import auth


