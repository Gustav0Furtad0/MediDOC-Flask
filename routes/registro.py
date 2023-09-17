from flask import Blueprint, request, render_template, flash
from database import db
from models import Doctor
from datetime import datetime
from werkzeug.security import generate_password_hash

register_bp = Blueprint('registro', __name__, template_folder='templates')

@register_bp.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if len(request.form['cpf']) != 11:
            return render_template('register.html', message='CPF inválido!')
        cpf = int(request.form['cpf'])

        if 'nome_completo' not in request.form and request.form['nome_completo'] == '':
            return render_template('register.html', message='É necessário informar o nome completo!')
        if len(request.form['nome_completo']) > 255:
            return render_template('register.html', message='Nome completo inválido!')
        nome_completo = request.form['nome_completo']
        
        if 'crm' not in request.form and request.form['crm'] == '':
            return render_template('register.html', message='CRM necessário')
        if len(request.form['crm']) > 20 or request.form['crm'].isnumeric() == False:
            return render_template('register.html', message='CRM inválido!')
        crm = int(request.form['crm'])
        
        if 'data_inscricao_crm' not in request.form and request.form['data_inscricao_crm'] == '':
            return render_template('register.html', message='Data de inscrição no CRM necessária!')
        data_inscricao_crm = datetime(1998, 1, 1)
        
        if 'senha' not in request.form and request.form['senha'] == '':
            return render_template('register.html', message='Senha necessária')
        if len(request.form['senha']) > 50:
            return render_template('register.html', message='Limite 50 de caracteres excedido!')
        senha = generate_password_hash(request.form['senha'])
        
        doctor = Doctor(nome_completo, crm, cpf, data_inscricao_crm, senha)
        db.session.add(doctor)
        db.session.commit()
        
        return render_template('login.html')
    elif request.method == 'GET':
        return render_template('register.html')
    
export = register_bp