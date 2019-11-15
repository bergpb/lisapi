from lisapi import db, login
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

from lisapi.models.tables import User
from lisapi.models.forms import Login, ChangePassword


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form_login = Login()
    if form_login.validate_on_submit():
        user = User.query.filter_by(username=form_login.username.data).first()
        form_pass = form_login.password.data
        user_pass = user.password
        if user and check_password_hash(user_pass, form_pass):
            login_user(user, remember=form_login.remember_me.data)
            flash('Logged in.', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid login!', 'error')
            return render_template('auth/login.html', form=form_login)
    else:
        if len(form_login.errors) > 0:
            flash('Check form data!', 'error')

    context = {
        'form': form_login,
        'active_menu': 'Login'
    }
    
    return render_template('auth/login.html', **context)


@auth.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form_passwd = ChangePassword()
    user = User.query.filter_by(id=current_user.id).first()
    if form_passwd.validate_on_submit():
        if check_password_hash(user.password, form_passwd.current_password.data):
            if form_passwd.new_password.data == form_passwd.confirm_password.data:
                user.password = generate_password_hash(form_passwd.confirm_password.data)
                db.session.commit()
                logout_user()
                flash('Password Changed!', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash('Passwords dont match!', 'error')
                return render_template('auth/change_password.html', form=form_passwd)
        else:
            flash('Wrong password!', 'error')
            return render_template('auth/change_password.html', form=form_passwd)
    else:
        if len(form_passwd.errors) > 0:
            flash('Check form data!', 'error')

    context = {
        'form': form_passwd,
        'active_menu': 'Change Password'
    }
    
    return render_template('auth/change_password.html', **context)


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('Logged out!', 'warning')
    return redirect(url_for('auth.login'))