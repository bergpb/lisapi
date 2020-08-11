from lisapi.errors import errors as errors_blueprint
from lisapi.auth import auth as auth_blueprint
from lisapi.main import main as main_blueprint
from lisapi.pin import pin as pin_blueprint
from lisapi.pwa import pwa as pwa_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(pwa_blueprint)
    app.register_blueprint(pin_blueprint)
    app.register_blueprint(errors_blueprint)
