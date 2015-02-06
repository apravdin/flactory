from flask import render_template, Blueprint
from app import app

error_bp = Blueprint('error', __name__, template_folder='templates/error')


@error_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('error/500.html'), 500
