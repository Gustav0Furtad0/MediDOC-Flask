from flask import Blueprint, render_template, request
from models import Patient
from flask_paginate import Pagination, get_page_parameter

pacientes_bp = Blueprint('pacientes', __name__, template_folder='templates')

@pacientes_bp.route('/pacientes', methods=['GET'])
def listar_consultas():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10

    pacientes = Patient.query.paginate(page=page, per_page=per_page)
    
    pagination = Pagination(page=page, total=pacientes.total, per_page=per_page, css_framework='bootstrap4')

    return render_template('listar_pacientes.html', pacientes=pacientes, pagination=pagination)