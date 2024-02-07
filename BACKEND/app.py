from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user,
from werkzeug.utils import secure_filename
import os

app = Flask()
app.config['SQLALCHEMY_DATABASE_URL'] = 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False