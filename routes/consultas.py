from flask import Blueprint, render_template, session, redirect
from models import Consultation

consultas_bp = Blueprint('consultas', __name__, template_folder='templates')

@consultas_bp.route('/consultas', methods=['GET'])
def listar_consultas():
    if not session.get("crm"):
        return redirect('/login')

    consultas = Consultation.query.filter_by(medico_id=session.get('crm')).all()

    return render_template('consultas.html', consultas=consultas)


@consultas_bp.route('/registrarConsulta', methods=['GET'])
def registrar_consulta():
    # Implemente a lógica para registrar novas consultas aqui
    # Pode ser necessário criar um formulário para coletar informações da consulta
    # Após o registro, redirecione o usuário de volta para a página de consultas
    return render_template('registrar_consulta.html')