from flask import Blueprint

pwa = Blueprint('pwa', __name__)

from . import views