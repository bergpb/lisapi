from flask import (flash, jsonify, redirect, render_template,
                   request, url_for)
from lisapi import db, login, socketio
from lisapi.helpers import helpers
from lisapi.models.tables import Pin, User
from . import main

@socketio.on('updateStatus')
def on_update(data):
    """Update content in page, receive updateStatus and emit statusUpdated"""
    data = helpers.status_info()
    socketio.emit('statusUpdated', data.json)


@socketio.on('changeState')
def change_pin_state(data):
    """Change state for pins """
    current_state = 0
    pin_number = data['pin_number']
    pin = Pin.query.filter_by(pin=pin_number).first()
    pin_state = helpers.set_pin(pin_number)
    pin.state = pin_state

    if pin_state is True:
        current_state = 1

    db.session.commit()

    data = jsonify({
        'pin': pin_number,
        'currentState': current_state
    })

    socketio.emit('statusChanged', data.json)


@socketio.on_error_default
def error_handler(error):
    socketio.emit('error', error)
    print(error)


@login.user_loader
def load_user(id):
    return User.query.get(id)


@main.route('/', methods=['GET'])
def dashboard():
    context = {
        'data': helpers.status_info(),
        'active_menu': 'Dashboard'
    }
    return render_template('main/dashboard.html', **context)


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html', active_menu='About')
