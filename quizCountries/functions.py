from random import randrange
import requests
import json
import requests
import random

def randomGame():

	select_game = randrange(1, 4)
	
	if select_game == 1:
		return capital()
	elif select_game == 2:
		return monnaie()
	else:
		return drapeau()

def capital():

	#url_un_pays = "https://restcountries.eu/rest/v2/name/" + pays + "?fullText=true"
	url_total_pays = "https://restcountries.eu/rest/v2/all"

	rq_pays = requests.get(url_total_pays)
	# rq_total_pays = requests.get(url_total_pays)

	# r3 = requests.get("http://api.worldbank.org/countries?incomeLevel=LMC")

	nbre_pays = len(rq_pays.json())

	key_reponse = randrange(1, nbre_pays)
	pays_reponse = rq_pays.json()[key_reponse]

	key_choix_2 = randrange(1, nbre_pays)
	key_choix_3 = randrange(1, nbre_pays)
	key_choix_4 = randrange(1, nbre_pays)

	pays_choix2 = rq_pays.json()[key_choix_2]
	pays_choix3 = rq_pays.json()[key_choix_3]
	pays_choix4 = rq_pays.json()[key_choix_4]

	

	# return r2.content
	question = {}
	question["type"] = "capital_quiz.html"
	question["enonce"] = "Quel est la capital de " + pays_reponse['translations']["fr"] + " ?"
	question["reponse"] = pays_reponse['capital']
	question["leschoix"] = []
	question["leschoix"].append(pays_reponse['capital'])
	question["leschoix"].append(pays_choix2['capital'])
	question["leschoix"].append(pays_choix3['capital'])
	question["leschoix"].append(pays_choix4['capital'])
	random.shuffle(question["leschoix"])



	return question

	# return r1.json()

def monnaie():
	#url_un_pays = "https://restcountries.eu/rest/v2/name/" + pays + "?fullText=true"
	url_total_pays = "https://restcountries.eu/rest/v2/all"

	rq_pays = requests.get(url_total_pays)
	# rq_total_pays = requests.get(url_total_pays)

	# r3 = requests.get("http://api.worldbank.org/countries?incomeLevel=LMC")

	nbre_pays = len(rq_pays.json())

	key_reponse = randrange(1, nbre_pays)
	pays_reponse = rq_pays.json()[key_reponse]

	key_choix_2 = randrange(1, nbre_pays)
	key_choix_3 = randrange(1, nbre_pays)
	key_choix_4 = randrange(1, nbre_pays)

	pays_choix2 = rq_pays.json()[key_choix_2]
	pays_choix3 = rq_pays.json()[key_choix_3]
	pays_choix4 = rq_pays.json()[key_choix_4]


	# return r2.content
	question = {}
	question["type"] = "monnaie_quiz.html"
	question["enonce"] = "Quel est la monnaie de " + pays_reponse['translations']["fr"] + " ?"
	question["reponse"] = pays_reponse['currencies'][0]
	question["leschoix"] = []
	question["leschoix"].append(pays_reponse['currencies'][0]['name'] + " (" + pays_reponse['currencies'][0]['symbol'] + ")")
	question["leschoix"].append(pays_choix2['currencies'][0]['name'] + " (" + pays_choix2['currencies'][0]['symbol'] + ")")
	question["leschoix"].append(pays_choix3['currencies'][0]['name'] + " (" + pays_choix3['currencies'][0]['symbol'] + ")")
	question["leschoix"].append(pays_choix4['currencies'][0]['name'] + " (" + pays_choix4['currencies'][0]['symbol'] + ")")
	random.shuffle(question["leschoix"])



	return question


def drapeau():
	
	#url_un_pays = "https://restcountries.eu/rest/v2/name/" + pays + "?fullText=true"
	url_total_pays = "https://restcountries.eu/rest/v2/all"

	rq_pays = requests.get(url_total_pays)
	# rq_total_pays = requests.get(url_total_pays)

	# r3 = requests.get("http://api.worldbank.org/countries?incomeLevel=LMC")

	nbre_pays = len(rq_pays.json())

	key_reponse = randrange(1, nbre_pays)
	pays_reponse = rq_pays.json()[key_reponse]

	key_choix_2 = randrange(1, nbre_pays)
	key_choix_3 = randrange(1, nbre_pays)
	key_choix_4 = randrange(1, nbre_pays)

	pays_choix2 = rq_pays.json()[key_choix_2]
	pays_choix3 = rq_pays.json()[key_choix_3]
	pays_choix4 = rq_pays.json()[key_choix_4]

	

	# return r2.content
	question = {}
	question["type"] = "flag_quiz.html"
	question["enonce"] = "Quel est le drapeau de " + pays_reponse['translations']["fr"] + " ?"
	question["reponse"] = pays_reponse['flag']
	question["leschoix"] = []
	question["leschoix"].append(pays_reponse['flag'])
	question["leschoix"].append(pays_choix2['flag'])
	question["leschoix"].append(pays_choix3['flag'])
	question["leschoix"].append(pays_choix4['flag'])
	random.shuffle(question["leschoix"])



	return question
