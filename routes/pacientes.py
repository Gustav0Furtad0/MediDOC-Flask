from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import Patient
from flask_paginate import Pagination, get_page_parameter
from database import db
from datetime import datetime

pacientes_bp = Blueprint('pacientes', __name__, template_folder='templates')

@pacientes_bp.route('/pacientes', methods=['GET'])
def listar_consultas():
    if not session.get("crm"):
        return redirect('/login')
    
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10

    pacientes = Patient.query.paginate(page=page, per_page=per_page)
    
    pagination = Pagination(page=page, total=pacientes.total, per_page=per_page, css_framework='bootstrap5')

    return render_template('pacientes.html', pacientes=pacientes, pagination=pagination)

@pacientes_bp.route('/registrarPaciente', methods=['GET', 'POST'])
def cadastrar_paciente():
    if not session.get("crm"):
        return redirect('/login')

    if request.method == 'POST':
        nome_completo = request.form.get('nome_completo')
        cpf = request.form.get('cpf')
        data_nascimento = request.form.get('data_nascimento')
        sexo = request.form.get('sexo')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        if not nome_completo:
            return render_template("cadastrarPaciente.html", message='É necessário informar o nome completo!')
        elif len(nome_completo) > 255:
            return render_template("cadastrarPaciente.html", message='Nome completo inválido!')

        if not cpf:
            return render_template("cadastrarPaciente.html", message='CPF necessário!')
        elif not cpf.isnumeric() or len(cpf) != 11:
            return render_template("cadastrarPaciente.html", message='CPF inválido! Deve conter 11 dígitos numéricos.')

        if not data_nascimento:
            return render_template("cadastrarPaciente.html", message='Data de nascimento necessária!')

        if not sexo:
            return render_template("cadastrarPaciente.html", message='Sexo necessário!')

        if nome_completo and cpf and data_nascimento and sexo:
            paciente = Patient(
                nome_completo=nome_completo,
                cpf=cpf,
                data_nascimento=datetime.strptime(data_nascimento, '%Y-%m-%d'),
                sexo=sexo,
                telefone=telefone,
                email=email
            )

            db.session.add(paciente)
            db.session.commit()

            return url_for('pacientes')
        
    return render_template('cadastrarPaciente.html')

@pacientes_bp.route('/editarPaciente/<string:cpf>', methods=['GET', 'POST'])
def editar_paciente(cpf):
    if not session.get("crm"):
        return redirect('/login')

    paciente = Patient.query.filter_by(cpf=cpf).first()

    if request.method == 'POST':
        nome_completo = request.form.get('nome_completo')
        data_nascimento = request.form.get('data_nascimento')
        cpf = request.form.get('cpf')
        sexo = request.form.get('sexo')
        telefone = request.form.get('telefone') 
        email = request.form.get('email')

        if not nome_completo:
            flash('É necessário informar o nome completo!', 'error')
        elif len(nome_completo) > 255:
            flash('Nome completo inválido!', 'error')

        if not data_nascimento:
            flash('Data de nascimento necessária!', 'error')

        if not sexo:
            flash('Sexo necessário!', 'error')

        if nome_completo and data_nascimento and sexo:
            paciente.nome_completo = nome_completo
            paciente.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')
            paciente.sexo = sexo
            paciente.telefone = telefone
            paciente.email = email
            
            db.session.commit()

            flash('Paciente atualizado com sucesso!', 'success')
            return redirect(url_for('pacientes.listar_consultas'))

    paciente.to_dict()
    
    return render_template('editarPaciente.html', paciente=paciente)

@pacientes_bp.route('/excluirPaciente/<string:cpf>')
def excluir_paciente(cpf):
    if not session.get("crm"):
        return redirect('/login')

    paciente = Patient.query.filter_by(cpf=cpf).first()
    
    db.session.delete(paciente)
    db.session.commit()

    return redirect(url_for('pacientes.listar_consultas'))