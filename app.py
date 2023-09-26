import os
from dotenv import load_dotenv
from flask import Flask, redirect
from flask_bootstrap import Bootstrap5
from flask_session import Session
from os.path import join, dirname
from flask_migrate import Migrate
from src.Model.database import db

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

bootstrap = Bootstrap5(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db.init_app(app)

migrate = Migrate(app, db)

@app.route('/adicionar_paciente')
def rota_adicionar_paciente():
    with app.app_context():
        db.create_all()
    
    return redirect('/')

app.run(debug=os.environ.get("DEBUG"), use_reloader=True, port=os.environ.get("PORT"))
