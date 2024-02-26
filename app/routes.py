from flask import render_template,redirect,url_for,send_from_directory,flash
from app import server
from app.forms import RegistrationForm, LoginForm
from flask_login import current_user, login_user, login_required, logout_user
from app import mongo
from app.models import UserProfile


@server.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = mongo.db.personal.find_one({'login': form.username.data})
        if existing_user:
            flash('Username is already taken. Please choose a different one.', 'error')
            return redirect(url_for('register'))

        new_user = UserProfile(
            login=form.username.data,
            password=form.password.data
        )

        new_user.save_to_db()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@server.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = mongo.db.personal.find_one({'login': form.username.data})
        user_ins = UserProfile(login=user['login'],password=user['password_hash'])
        if user is None or not user_ins.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user_ins)
        return redirect(url_for('profile'))
    return render_template('login.html', title='Sign In', form=form)

@server.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@server.route('/')
def index():
    return redirect(url_for('login'))

@server.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@server.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
