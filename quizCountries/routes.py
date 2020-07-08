from quizCountries import app
from flask import render_template
from quizCountries.functions import randomGame

@app.route('/')
def home():
    return render_template('home.html')


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