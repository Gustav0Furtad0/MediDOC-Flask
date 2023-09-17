from flask import Flask
from flask_migrate import Migrate
from database import db
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap5(app)

db.init_app(app)

# Register blueprints
from routes.register import register_bp
from routes.login import login_bp

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

app.run(debug=True)
