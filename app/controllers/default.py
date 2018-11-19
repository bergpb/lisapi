from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login

# import RPi.GPIO as gpio

from app.models.tables import User, Pin
from app.models.forms import Login, SignUp, NewPin, ChangePassword, EditPin


# gpio.setmode(gpio.BCM)
# gpio.setwarnings(False)


@login.user_loader
def load_user(id):
    return User.query.get(id)
    

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


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
            flash("Invalid login.", "danger")
            return render_template('login.html',
                           form=form_login)
    else:
        if len(form_login.errors) > 0:
            flash("Check data.", "danger")
        return render_template('login.html',
                           form=form_login)


@app.route("/create", methods=["GET", "POST"])
def create_pin():
    form_new_pin = NewPin()
    if form_new_pin.validate_on_submit():
        name = form_new_pin.name.data
        pin = form_new_pin.pin.data
        pin = Pin(name=name, pin=pin, state=False, user_id=current_user.id)
        db.session.add(pin)
        db.session.commit()
        flash("Pin created", "success")
        return redirect(url_for('list_pins'))
    else:
        if len(form_new_pin.errors) > 0:
            flash("Check form data", "danger")
        return render_template('new.html',
                           form=form_new_pin)


@app.route("/list", methods=["GET"])
@login_required
def list_pins():
    list_pins = Pin.query.filter_by(user_id=current_user.id)
    return render_template('list.html',
                            pins=list_pins)


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
            flash("Check form data", "danger")
        pin = Pin.query.get(pin_id)
        return render_template('edit.html',
                           form=form_editpin, pin=pin)


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
    list_pins = Pin.query.filter_by(user_id=current_user.id)
    return render_template('control.html', pins=list_pins)
    
    
@app.route("/control/<int:pin_number>", methods=["GET"])
@login_required
def control_pin(pin_number):
    pin = Pin.query.filter_by(pin=pin_number).first()
    
    # gpio.setup(pin_number, gpio.OUT)
    # state = gpio.input(pin_number)
    
    # if state == 0:
    #     gpio.output(pin_number, 1)
    #     state = gpio.input(pin_number)
    #     pin.state = not pin.state
    
    # elif state == 1:
    #     gpio.output(pin_number, 0)
    #     state = gpio.input(pin_number)
    #     pin.state = not pin.state

    # else:
    #     flash("Fail to change state for {} pin.".format(pin.name), "danger")
    #     return redirect(url_for('control_pins'))
    
    
    # db.session.commit()
    flash("{} changed.".format(pin.name), "success")
    return redirect(url_for('control_pins'))
    
    
@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')
    
    
@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    form_password = ChangePassword()
    user = User.query.filter_by(id=current_user.id).first()
    if form_password.validate_on_submit():
        if user.password == form_password.current_password.data:
            
            if form_password.new_password.data == form_password.confirm_password.data:
                user.password = form_password.confirm_password.data
                db.session.commit()
                logout_user()
                flash("Password Changed.", "success")
                return redirect(url_for('login'))
                
            else:
                flash("Password dont match.", "danger")
                return render_template('change_password.html',
                                        form=form_password)
            
        else:
            flash("Wrong password.", "danger")
            return render_template('change_password.html',
                                    form=form_password)
                                    
    else:
        if len(form_password.errors) > 0:
            flash("Check data.", "danger")
        return render_template('change_password.html',
                                    form=form_password)

    
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("Logged out.", "warning")
    return redirect(url_for("login"))
