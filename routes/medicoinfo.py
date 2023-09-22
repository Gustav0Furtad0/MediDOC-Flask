from flask import Blueprint, render_template, session, redirect, request
from src.model.models import Doctor
from datetime import datetime
from src.Model.database import db
from werkzeug.security import check_password_hash, generate_password_hash

medicoinfo_bp = Blueprint('medicoinfo', __name__, template_folder='templates')

@medicoinfo_bp.route('/medicoinfo', methods=['GET'])
def medicoinfo():
    if not session.get("crm"):
        return redirect('/login')

    doctor = Doctor.query.filter_by(crm=session.get('crm')).first().to_dict()
    
    return render_template('medicoinfo.html', doctor=doctor)

@medicoinfo_bp.route('/editarmedico', methods=['GET', 'POST'])
def editarmedico():
    if not session.get("crm"):
        return redirect('/login')
    
    doctor = Doctor.query.filter_by(crm=session.get('crm')).first()
    
    if request.method == 'GET':
        doctor = doctor.to_dict()
        return render_template('editarmedico.html', doctor=doctor)
    
    elif request.method == 'POST':
        if 'nome_completo' not in request.form and request.form['nome_completo'] == '':
            return render_template('editarmedico.html', message='É necessário informar o nome completo!')
        if len(request.form['nome_completo']) > 255:
            return render_template('editarmedico.html', message='Nome completo inválido!')
        doctor.nome_completo = request.form['nome_completo']
        
        if 'crm' not in request.form and request.form['crm'] == '':
            return render_template('editarmedico.html', message='CRM necessário')
        if len(request.form['crm']) > 20 or request.form['crm'].isnumeric() == False:
            return render_template('editarmedico.html', message='CRM inválido!')
        doctor.crm = int(request.form['crm'])
        
        if 'data_inscricao_crm' not in request.form and request.form['data_inscricao_crm'] == '':
            return render_template('editarmedico.html', message='Data de inscrição no CRM necessária!')
        doctor.data_inscricao_crm = datetime.strptime(request.form['data_inscricao_crm'], '%Y-%m-%d')
        
        if 'senha' not in request.form and request.form['senha'] == '':
            return render_template('editarmedico.html', message='Senha necessária!')
        doctor.senha = generate_password_hash(request.form['senha'])
        
        db.session.commit()
        
        redirect('/medicoinfo.html')

    return redirect('/bemvindo')