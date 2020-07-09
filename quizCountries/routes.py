from flask import render_template, url_for, flash, redirect, request
from quizCountries import app, db, bcrypt
from quizCountries.forms import RegistrationForm, LoginForm
from quizCountries.models import User
from flask_login import login_user, current_user, logout_user, login_required
from quizCountries.functions import randomGame


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Votre compte a été créé! Vous pouvez désormais vous connecter', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('quiz'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('quiz'))
        else:
            flash('Connexion non réussie. Veuillez vérifier l\'adresse électronique et le mot de passe', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route('/quiz/<name>')
def quizQ(name):
    print(f"{name}")
    return "name vaut : " + name

@app.route('/quiz')
def quiz():

    question = randomGame()

    jeux = question["leschoix"]
    test = question["enonce"]
   
    templateQuiz = question["type"]

    return render_template(templateQuiz, datas=jeux, question=test)