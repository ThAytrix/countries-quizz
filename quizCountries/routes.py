from quizCountries import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quiz/<id>')
def quizQ(id):
    print(f"{id}")
    return 'test'

@app.route('/quiz')
def quiz():
    pays = [
        {
            'name': 'Estonia',
            'alpha3Code' : 'EST',
            'capital': 'Tallinn',
            'population': 1315944,
            'flag': 'https://restcountries.eu/data/est.svg'         
        },
        {
            'name': 'France',
            'alpha3Code' : 'FRA',
            'capital': 'Paris',
            'population': 66710000,
            'flag': 'https://restcountries.eu/data/fra.svg'  
        },
        {  
            'name': 'Belgium',
            'alpha3Code' : 'BEL',
            'capital': 'Brussels',
            'population': 11319511,
            'flag': 'https://restcountries.eu/data/bel.svg'  
        },
        {  
            'name': 'Italy',
            'alpha3Code' : 'ITA',
            'capital': 'Rome',
            'population': 60665551,
            'flag': 'https://restcountries.eu/data/ita.svg'  
        }
    ]

    question = "Quel pays a pour capitale Rome?"
    return render_template('quiz.html', datas=pays, question=question)