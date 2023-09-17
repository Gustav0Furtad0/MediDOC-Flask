from flask import Blueprint, request, render_template
from models import Doctor

login_bp = Blueprint('login', __name__, template_folder='templates')


@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if 'crm' not in request.form and request.form['crm'] == '':
            return 'CRM is required', 400    
        crm = request.form['crm']
        
        if 'senha' not in request.form and request.form['senha'] == '':
            return 'Senha is required', 400
        senha = request.form['senha']
        
        doctor = Doctor.query.filter_by(crm=crm, senha=senha).first()
        
        if doctor is None:
            return 'CRM or senha is invalid', 400
        
        return 'Login Feito!!!!', 201
    elif request.method == 'GET':
        return render_template('login.html')