from flask import Blueprint, render_template


error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404


@error.app_errorhandler(500)
def internal_error(error):
    return render_template('error/500.html'), 500


@error.app_errorhandler(401)
def internal_error(error):
    return render_template('error/401.html'), 401