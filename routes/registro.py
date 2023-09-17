from flask import Blueprint, request, render_template, flash
from database import db
from models import Doctor
from datetime import datetime
from werkzeug.security import generate_password_hash

register_bp = Blueprint('registro', __name__, template_folder='templates')

