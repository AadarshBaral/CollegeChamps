import os
from flask import Flask, session,redirect,url_for
from flask_login.mixins import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin,login_required
from flask_mail import Mail
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_scss import Scss
# import flask_whooshalchemy as wa
from flask_migrate import Migrate
from werkzeug.utils import redirect
import requests
from oauthlib.oauth2 import WebApplicationClient


app = Flask(__name__)



GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)

class env_v:
    db_username = os.environ.get('DB_USERNAME')
    db_pw = os.environ.get('DB_PASSWORD') 

creds = env_v()

Scss(app)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=os.environ.get('DB_EMAIL'),
    MAIL_PASSWORD=os.environ.get('DB_EMAIL_PASSWORD')
)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['WOOSH_BASE'] = 'woosh'

db = SQLAlchemy(app)



Migrate(app, db)
# wa.whoosh_index(app,Post)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = 'users.login'

# for information alert
login_manager.login_message_category = 'info'


mail = Mail(app)

from collegechamps.users.routes import users
from collegechamps.err.handlers import errors
from collegechamps.subjects.subjects import subjects
from collegechamps.main.routes import main
# from collegechamps.mcqs.routes import quest
from collegechamps.blog.routes import blogs

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(errors)
app.register_blueprint(subjects)
# app.register_blueprint(quest)
app.register_blueprint(blogs)

from collegechamps.models import User, Post ,Set

 

  
class MyModelView(ModelView):
    def is_accessible(self):
        return "user" in session and session['user'] == creds.db_username

admin = Admin(app)
admin.add_view(MyModelView(Post, db.session))
admin.add_view(MyModelView(User, db.session))

