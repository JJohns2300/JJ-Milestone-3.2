from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user,
from werkzeug.utils import secure_filename
import os

app = Flask()
app.config['SQLALCHEMY_DATABASE_URL'] = 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456789'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

#USER AUTHENTIFICATION#
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    images = db.relationship('Image', backref='user', lazy=True)

#IMAGE STORING DATABASE#
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.string(225), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1) [1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    images = Image=query.all()
    return render_template('index.html', images=images)

@app.route('/login', methods=['GET', 'POST'])
def login():

@app.route('/logout')
@app.route
def logout():

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        title = request.form['title']
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            new_image = Image(title=title, file_path=file_path, user=current_user)
            db.session.add(new_image)
            db.session.commit()

            flash('Uploaded Successfully!')
            return redirect(url_for('index'))
        else:
            flash('Invalid file format. Allowed formats are png, jpg, jpeg, gif, mp4.', 'danger')

    return render_template('upload.html')

if__name__ == '__main__':
db.create_all()
app.run(debug=True)



