from flask import (Blueprint, flash, jsonify, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from lisapi import db
from lisapi.helpers import helpers
from lisapi.models.forms import EditPin, NewPin
from lisapi.models.tables import Pin, User
from . import pin


@pin.route('/create', methods=['GET', 'POST'])
def create_pin():
    form_new_pin = NewPin()
    if form_new_pin.validate_on_submit():
        pin_name = form_new_pin.name.data
        pin_number = int(form_new_pin.pin.data)
        pin_color = form_new_pin.color.data
        pin_icon = form_new_pin.icon.data
        check_pin = helpers.check_pin(pin_number)

        if not check_pin:
            flash('Pin {} dont exists!'.format(pin_number), 'error')
            return render_template('pin/new.html', form=form_new_pin)
        else:
            pin = Pin(name=pin_name, pin=pin_number,
                      color=pin_color, icon=pin_icon,
                      state=False, user_id=current_user.id)
            db.session.add(pin)
            db.session.commit()
            flash('Pin created!', 'success')
            return redirect(url_for('pin.list_pins'))

    if len(form_new_pin.errors) > 0:
        flash('Check form data!', 'error')

    context = {
        'form': form_new_pin,
        'active_menu': 'New Pin'
    }
        
    return render_template('pin/new.html', **context)


@pin.route('/list', methods=['GET'])
@login_required
def list_pins():
    list_pins = Pin.query.all()

    context = {
        'pins': list_pins,
        'active_menu': 'List Pins'
    }

    return render_template('pin/list.html', **context)


@pin.route('/edit/<int:pin_id>', methods=['GET', 'POST'])
@login_required
def edit_pin(pin_id):
    pin = Pin.query.get(pin_id)
    form_editpin = EditPin(obj=pin)

    context = {
        'form': form_editpin,
        'pin': pin,
        'active_menu': 'Edit Pin'
    }

    if request.method == 'POST':
        if form_editpin.validate_on_submit():
            pin_number = int(form_editpin.pin.data)
            check_pin = helpers.check_pin(pin_number)

            if not check_pin:
                flash('Pin {} dont exists!'.format(pin_number), 'error')
                return render_template('pin/edit.html', **context)

            pin = Pin.query.get(pin_id)
            pin.name = form_editpin.name.data
            pin.pin = form_editpin.pin.data
            pin.color = form_editpin.color.data
            pin.icon = form_editpin.icon.data
            db.session.commit()
            flash('Pin edited!', 'success')
            return redirect(url_for('pin.list_pins'))

        if len(form_editpin.errors) > 0:
            flash('Check form data!', 'error')
            print(form_editpin.errors)

    return render_template('pin/edit.html', **context)


@pin.route('/delete/<int:pin_id>', methods=['GET'])
@login_required
def delete_pin(pin_id):
    pin = Pin.query.get(pin_id)
    db.session.delete(pin)
    db.session.commit()
    flash('Pin removed!', 'warning')
    return redirect(url_for('pin.list_pins'))


@pin.route('/control', methods=['GET'])
@login_required
def control_pins():
    list_pins = Pin.query.all()

    context = {
        'pins': list_pins,
        'active_menu': 'Control Pins'
    }

    return render_template('pin/control.html', **context)