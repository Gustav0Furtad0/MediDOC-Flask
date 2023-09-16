from flask import Flask
from flask_migrate import Migrate
from database import db
from routes.doctor import doctor_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(doctor_bp, url_prefix='/api')

migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'
