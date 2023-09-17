from flask import Blueprint, render_template, session, redirect

bemVindo_bp = Blueprint('bemvindo', __name__, template_folder='templates')

@bemVindo_bp.route('/bemvindo', methods=['GET'])
def bemvindo():
    if not session.get("crm"):
        return redirect('/login')
    
    return render_template('welcome.html', doctor=session.get('doctor'))