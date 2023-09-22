import os
from dotenv import load_dotenv
from flask import Flask, redirect
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return redirect("/login", code=302)

app.run(debug=os.environ.get("DEBUG"), use_reloader=True, port=os.environ.get("PORT"))