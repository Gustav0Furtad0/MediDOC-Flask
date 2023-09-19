from flask import Blueprint, request, render_template, redirect, session, url_for
from models import Doctor
from werkzeug.security import check_password_hash, generate_password_hash
from database import db
from datetime import datetime

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        crm = request.form.get('crm')
        senha = request.form.get('senha')
        
        doctor = Doctor.query.filter_by(crm=crm).first()
        
        if doctor is None:
            return render_template('login.html', message='CRM inválido ou não cadastrado!'), 400
        
        if check_password_hash(doctor.senha, senha) == False:
            return render_template('login.html', message='Senha incorreta!'), 400
        
        session['crm'] = crm
        session['doctor'] = doctor
        
        return redirect('/bemvindo')

    elif request.method == 'GET':
        return render_template('login.html')
    
@login_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        if 'nome_completo' not in request.form and request.form['nome_completo'] == '':
            return render_template('register.html', message='É necessário informar o nome completo!')
        if len(request.form['nome_completo']) > 255:
            return render_template('register.html', message='Nome completo inválido!')
        nome_completo = request.form['nome_completo']
        
        if 'crm' not in request.form and request.form['crm'] == '':
            return render_template('register.html', message='CRM necessário')
        if len(request.form['crm']) > 20 or request.form['crm'].isnumeric() == False:
            return render_template('register.html', message='CRM inválido!')
        crm = request.form['crm']
        
        if 'crm' not in request.form and request.form['crm'] == '':
            return render_template('register.html', message='CPF necessário')
        if len(request.form['crm']) != 11 or request.form['crm'].isnumeric() == False:
            return render_template('register.html', message='CPF inválido!')
        cpf = request.form['cpf']
        
        if 'data_inscricao_crm' not in request.form and request.form['data_inscricao_crm'] == '':
            return render_template('register.html', message='Data de inscrição no CRM necessária!')
        data_inscricao_crm_str = request.form['data_inscricao_crm']
        
        if 'senha' not in request.form and request.form['senha'] == '':
            return render_template('register.html', message='Senha necessária!')
        senha = generate_password_hash(request.form['senha'])
        
        data_inscricao_crm = datetime.strptime(data_inscricao_crm_str, '%Y-%m-%d').date()

        novo_medico = Doctor(nome_completo=nome_completo, crm=crm, cpf=cpf, data_inscricao_crm=data_inscricao_crm, senha=senha)
        
        db.session.add(novo_medico)
        db.session.commit()

        return redirect(url_for('login.login'))

    return render_template('register.html')

@login_bp.route('/logout')
def logout():
    session.pop('crm', None)
    session.pop('doctor', None)
    return redirect(url_for('login.login'))