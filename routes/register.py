from flask import Blueprint, request, render_template
from database import db
from models import Doctor
from datetime import datetime

register_bp = Blueprint('registro', __name__)

@register_bp.route('/registro', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if 'cpf' not in request.form and request.form['cpf'] == '':
            return f'CPF is required', 400
        if len(request.form['cpf']) != 11:
            return f'CPF is invalid', 400
        cpf = int(request.form['cpf'])
        
        if 'nome_completo' not in request.form and request.form['nome_completo'] == '':
            return 'Nome completo is required', 400
        if len(request.form['nome_completo']) > 255:
            return 'Nome completo is invalid', 400
        nome_completo = request.form['nome_completo']
        
        if 'crm' not in request.form and request.form['crm'] == '':
            return 'CRM is required', 400
        if len(request.form['crm']) > 20 or request.form['crm'].isnumeric() == False:
            return 'CRM is invalid', 400
        crm = int(request.form['crm'])
        
        if 'data_inscricao_crm' not in request.form and request.form['data_inscricao_crm'] == '':
            return 'Data inscricao CRM is required', 400
        data_inscricao_crm = datetime(1998, 1, 1)
        
        if 'senha' not in request.form and request.form['senha'] == '':
            return 'Senha is required', 400
        if len(request.form['senha']) > 50:
            return 'Senha is invalid', 400
        senha = request.form['senha']
        
        
        
        doctor = Doctor(nome_completo, crm, cpf, data_inscricao_crm, senha)
        db.session.add(doctor)
        db.session.commit()
        
        return 'POST doctor', 201
    elif request.method == 'GET':
        Doctors = Doctor.query.all()
        return render_template('register.html', doctors=Doctors)