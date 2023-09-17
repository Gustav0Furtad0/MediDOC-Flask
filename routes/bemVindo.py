from flask import Blueprint, render_template

bemVindo_bp = Blueprint('bemvindo', __name__, template_folder='templates')

@bemVindo_bp.route('/bemvindo', methods=['GET'])
def register():
    return render_template('welcome.html')