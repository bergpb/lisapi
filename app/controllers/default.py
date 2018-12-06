from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login
import subprocess

from app.models.tables import User, Pin
from app.models.forms import Login, NewPin, ChangePassword, EditPin
from app.helpers import helpers


@login.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html', **locals())


@app.route("/api/status", methods=["GET"])
def status():
    process = subprocess.getstatusoutput('ps -aux | wc -l')[1]
    uptime = subprocess.getstatusoutput('uptime -p')[1]
    mem_total = subprocess.getstatusoutput('free -h | grep \'Mem\' | cut -c 16-18')[1]
    mem_used = subprocess.getstatusoutput('free -h | grep \'Mem\' | cut -c 28-30')[1]
    mem_free = subprocess.getstatusoutput('free -h | grep \'Mem\' | cut -c 41-42')[1]
    return jsonify(
        process=process,
        uptime=uptime,
        mem_total=mem_total,
        mem_used=mem_used,
        mem_free=mem_free
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = Login()
    if form_login.validate_on_submit():
        user = User.query.filter_by(username=form_login.username.data).first()
        if user and user.password == form_login.password.data:
            login_user(user, remember=form_login.remember_me.data)
            flash("Logged in.", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid login.", "error")
            return render_template('login.html', form=form_login)
    else:
        if len(form_login.errors) > 0:
            flash("Check data.", "error")
        return render_template('login.html', form=form_login)


@app.route("/create", methods=["GET", "POST"])
def create_pin():
    form_new_pin = NewPin()
    if form_new_pin.validate_on_submit():
        pin_name = form_new_pin.name.data
        pin_number = form_new_pin.pin.data
        check_pin = helpers.checkPin(pin_number)
        pin_exists = Pin.query.filter_by(pin=pin_number).first()
        if not check_pin:
            flash("Pin {} dont exists!".format(pin_number), "error")
            return render_template('new.html', form=form_new_pin)
        elif pin_exists:
            flash("Pin {} is not disponible!".format(pin_number), "error")
            return render_template('new.html', form=form_new_pin)
        else:
            pin = Pin(name=pin_name, pin=pin_number, state=False, user_id=current_user.id)
            db.session.add(pin)
            db.session.commit()
            flash("Pin created!", "success")
            return redirect(url_for('list_pins'))
    else:
        if len(form_new_pin.errors) > 0:
            flash("Check form data", "error")
        return render_template('new.html', form=form_new_pin)


@app.route("/list", methods=["GET"])
@login_required
def list_pins():
    list_pins = Pin.query.all()
    return render_template('list.html', pins=list_pins)


@app.route("/edit/<int:pin_id>", methods=["GET", "POST"])
@login_required
def edit_pin(pin_id):
    form_editpin = EditPin()
    if form_editpin.validate_on_submit():
        pin = Pin.query.get(pin_id)
        pin.name = form_editpin.name.data
        pin.pin = form_editpin.pin.data
        db.session.commit()
        flash("Pin edited", "success")
        return redirect(url_for('list_pins'))
    else:
        if len(form_editpin.errors) > 0:
            flash("Check form data", "error")
        pin = Pin.query.get(pin_id)
        return render_template('edit.html', form=form_editpin, pin=pin)


@app.route("/delete/<int:pin_id>", methods=["GET"])
@login_required
def delete_pin(pin_id):
    pin = Pin.query.get(pin_id)
    db.session.delete(pin)
    db.session.commit()
    flash('Pin removed.', 'warning')
    return redirect(url_for('list_pins'))


@app.route("/control", methods=["GET"])
@login_required
def control_pins():
    list_pins = Pin.query.all()
    return render_template('control.html', pins=list_pins)


@app.route("/control/<int:pin_number>", methods=["GET"])
@login_required
def control_pin(pin_number):
    pin = Pin.query.filter_by(pin=pin_number).first()
    pin_state = helpers.setPin(pin_number)
    if pin_state == True:
        pin.state = pin_state
    elif pin_state == False:
        pin.state = pin_state
    else:
        flash("Pin {} dont exists!".format(pin.pin), "warning")
        return redirect(url_for('control_pins'))
    db.session.commit()
    flash("{} changed.".format(pin.name), "success")
    return redirect(url_for('control_pins'))


@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    form_passwd = ChangePassword()
    user = User.query.filter_by(id=current_user.id).first()
    if form_passwd.validate_on_submit():
        if user.password == form_passwd.current_password.data:
            if form_passwd.new_password.data == form_passwd.confirm_password.data:
                user.password = form_passwd.confirm_password.data
                db.session.commit()
                logout_user()
                flash("Password Changed.", "success")
                return redirect(url_for('login'))
            else:
                flash("Password dont match.", "error")
                return render_template('change_password.html', form=form_passwd)
        else:
            flash("Wrong password.", "error")
            return render_template('change_password.html', form=form_passwd)
    else:
        if len(form_passwd.errors) > 0:
            flash("Check data.", "error")
        return render_template('change_password.html', form=form_passwd)


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("Logged out.", "warning")
    return redirect(url_for("login"))
