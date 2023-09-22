from flask import Blueprint, session
from src.model.models import Doctor, Patient


verifica_bp = Blueprint('verifica', __name__, template_folder='templates')

@verifica_bp.route('/verificaMedico', methods=['GET'])
def verificaMedico():
    if not session.get("crm"):
        return "Not Logged", 404
    
    medico = Doctor.query.filter_by(crm=session.get("crm")).first()
    if not medico:
        return False, 401
    else:
        return True, 302
    

@verifica_bp.route('/verificaPaciente', methods=['GET'])
def verificaPaciente():
    if not session.get("crm"):
        return "Not Logged", 404
    
    paciente = Patient.query.filter_by(cpf=session.get("cpf")).first()
    if not paciente:
        return False, 401
    else:
        return True, 302