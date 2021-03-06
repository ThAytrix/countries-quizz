from flask import render_template, url_for, flash, redirect, request
from quizCountries import app, db, bcrypt
from quizCountries.forms import RegistrationForm, LoginForm
from quizCountries.models import User
from flask_login import login_user, current_user, logout_user, login_required
from quizCountries.functions import randomGame, infosJoueur
import json


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
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, nbrePartie=0, nbreReussite=0)
        db.session.add(user)
        db.session.commit()
        flash('Votre compte a été créé! Vous pouvez désormais vous connecter', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
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

@app.route('/quizResult', methods=['GET', 'POST'])
def quizQ():

    tab_question = request.form['select']


    listPreviousError = [' ', '(', '{', '[']
    listNextError = [':', ',', ']']

    i = 0
    while (i < len(tab_question)):
        if tab_question[i] == '\'' and ((tab_question[i + 1] in listNextError) or (tab_question[i - 1] in listPreviousError)):
            tab_question = tab_question[:i] + '\"' + tab_question[i + 1:]
        i += 1



    pos = tab_question.find("{")
    lastpos = tab_question.find("}")

    question = tab_question[pos:lastpos+1]
    question = json.loads(question)

    jeux = question["leschoix"]


    selection = tab_question.replace(tab_question[pos:lastpos+1], '')
    selection = selection.replace("\"", "")
    selection = selection.replace("(", "")
    selection = selection.replace(")", "")
    selection = selection.replace(",", "")
    selection = selection.strip()

    if selection == question['reponse']:
        trouve=1
        if current_user.is_authenticated:
            infosJoueur(1)
    else:
        trouve=0
        if current_user.is_authenticated:
            infosJoueur(0)
    
    return render_template('result_quiz.html', selection=selection, tab_question=question, jeux=jeux, trouve= trouve, question=question["enonce"])

@app.route('/quiz')
def quiz():

    question = randomGame()

    jeux = question["leschoix"]
    enonce = question["enonce"]
    reponse = question["reponse"]
   
    templateQuiz = question["type"]

    return render_template(templateQuiz, datas=jeux, question=enonce, tab_question=question)


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
    return render_template('error.html')

