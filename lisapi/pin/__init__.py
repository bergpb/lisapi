from flask import Blueprint

pin = Blueprint('pin', __name__)

from . import views