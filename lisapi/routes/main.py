from lisapi import db, login, bcrypt
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user


from lisapi.models.tables import User, Pin
from lisapi.models.forms import Login, NewPin, ChangePassword, EditPin
from lisapi.helpers import helpers



main = Blueprint('main', __name__)


@login.user_loader
def load_user(id):
    return User.query.get(id)


@main.route('/', methods=['GET'])
def dashboard():
    return render_template('main/dashboard.html', data=helpers.statusInfo())


@main.route('/create', methods=['GET', 'POST'])
def create_pin():
    form_new_pin = NewPin()
    if form_new_pin.validate_on_submit():
        pin_name = form_new_pin.name.data
        pin_number = form_new_pin.pin.data
        pin_color = form_new_pin.color.data
        pin_icon = form_new_pin.icon.data
        check_pin = helpers.checkPin(pin_number)
        pin_exists = Pin.query.filter_by(pin=pin_number).first()
        if not check_pin:
            flash('Pin {} dont exists!'.format(pin_number), 'error')
            return render_template('main/new.html', form=form_new_pin)
        elif pin_exists:
            flash('Pin {} is not disponible!'.format(pin_number), 'error')
            return render_template('main/new.html', form=form_new_pin)
        else:
            pin = Pin(name=pin_name, pin=pin_number,
                      color=pin_color, icon=pin_icon,
                      state=False, user_id=current_user.id)
            db.session.add(pin)
            db.session.commit()
            flash('Pin created!', 'success')
            return redirect(url_for('main.list_pins'))
    else:
        if len(form_new_pin.errors) > 0:
            flash('Check form data', 'error')
        return render_template('main/new.html', form=form_new_pin)


@main.route('/list', methods=['GET'])
@login_required
def list_pins():
    list_pins = Pin.query.all()
    return render_template('main/list.html', pins=list_pins)


@main.route('/edit/<int:pin_id>', methods=['GET', 'POST'])
@login_required
def edit_pin(pin_id):
    if request.method == 'POST':
        form_editpin = EditPin()
        if form_editpin.validate_on_submit():
            pin = Pin.query.get(pin_id)
            pin.name = form_editpin.name.data
            pin.pin = form_editpin.pin.data
            pin.color = form_editpin.color.data
            pin.icon = form_editpin.icon.data
            db.session.commit()
            flash('Pin edited', 'success')
            return redirect(url_for('main.list_pins'))
        else:
            if len(form_editpin.errors) > 0:
                flash('Check form data', 'error')
    else:
        pin = Pin.query.get(pin_id)
        form_editpin = EditPin(obj=pin)

    return render_template('main/edit.html', form=form_editpin, pin=pin)


@main.route('/delete/<int:pin_id>', methods=['GET'])
@login_required
def delete_pin(pin_id):
    pin = Pin.query.get(pin_id)
    db.session.delete(pin)
    db.session.commit()
    flash('Pin removed.', 'warning')
    return redirect(url_for('main.list_pins'))


@main.route('/control', methods=['GET'])
@login_required
def control_pins():
    list_pins = Pin.query.all()
    return render_template('main/control.html', pins=list_pins)


@main.route('/control/<int:pin_number>', methods=['GET'])
@login_required
def control_pin(pin_number):
    pin = Pin.query.filter_by(pin=pin_number).first()
    pin_state = helpers.setPin(pin_number)
    if pin_state is True:
        pin.state = pin_state
    elif pin_state is False:
        pin.state = pin_state
    else:
        flash('Pin {} don\'t exists!'.format(pin.pin), 'warning')
        return redirect(url_for('main.control_pins'))
    db.session.commit()
    flash('{} changed.'.format(pin.name), 'success')
    return redirect(url_for('main.control_pins'))


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
