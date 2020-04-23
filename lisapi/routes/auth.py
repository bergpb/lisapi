from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from lisapi import db, login
from lisapi.models.forms import ChangePassword, Login
from lisapi.models.tables import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form_login = Login()
    if form_login.validate_on_submit():
        user = User.query.filter_by(username=form_login.username.data).first()
        password = form_login.password.data

        if user.check_password(password):
            login_user(user, remember=form_login.remember_me.data)
            flash('Logged in.', 'success')
            return redirect(url_for('main.dashboard'))

        flash('Invalid login!', 'error')
        return render_template('auth/login.html', form=form_login)

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

    if form_passwd.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        current_password = form_passwd.current_password.data
        new_password = form_passwd.new_password.data

        if user.check_password(current_password):
            user.set_password(new_password)
            db.session.commit()
            logout_user()
            flash('Password Changed!', 'success')
            return redirect(url_for('auth.login'))

        flash('Wrong password!', 'error')
        return render_template('auth/change_password.html', form=form_passwd)

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
