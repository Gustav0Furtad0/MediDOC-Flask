from flask import Blueprint, request
from models import Doctor
from database import db
from datetime import datetime

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/doctor')
def doctor():
    return 'Hello doctor!'
