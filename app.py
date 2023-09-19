import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, redirect
from flask_migrate import Migrate
from database import db
from flask_bootstrap import Bootstrap5
from flask_session import Session

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

bootstrap = Bootstrap5(app)
db.init_app(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Register blueprints
from routes import login, bemVindo, medicoinfo, consultas, pacientes
app.register_blueprint(login.login_bp)
app.register_blueprint(bemVindo.bemVindo_bp)
app.register_blueprint(medicoinfo.medicoinfo_bp)
app.register_blueprint(consultas.consultas_bp)
app.register_blueprint(pacientes.pacientes_bp)

migrate = Migrate(app, db)

@app.route('/', methods=['GET'])
def index():
    return redirect("/login", code=302)

app.run(debug=os.environ.get("DEBUG"), use_reloader=True, port=os.environ.get("PORT"))
