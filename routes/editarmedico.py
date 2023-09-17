from flask import Blueprint, render_template, session, redirect, request
from models import Doctor
from database import db
from datetime import datetime

editarmedico_bp = Blueprint('editarmedico', __name__, template_folder='templates')

