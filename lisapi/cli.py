from lisapi import db
from lisapi.models.tables import User


def init_app(app):
    @app.cli.command()
    def seed():
        """Add admin user"""
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print('Creating user admin...')
            admin = User('admin', 'admin@email.com', 'admin')
            db.session.add(admin)
            db.session.commit()
            print('User created.')
        else:
            print('User exists.')