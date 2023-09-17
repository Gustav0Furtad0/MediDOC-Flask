from flask import Blueprint, request, render_template, redirect, session
from models import Doctor
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        crm = request.form.get('crm')
        senha = request.form.get('senha')
        
        doctor = Doctor.query.filter_by(crm=crm).first()
        
        if doctor is None:
            return render_template('login.html', message='CRM inválido ou não cadastrado!'), 400
        
        if not check_password_hash(doctor.senha, senha):
            return render_template('login.html', message='Senha incorreta!'), 400
        
        session['crm'] = crm
        session['doctor'] = doctor
        
        return redirect('/bemvindo')

    elif request.method == 'GET':   
        return render_template('login.html')