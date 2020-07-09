from random import randrange
import requests
import json
import requests
import random

def randomGame():
	'''renvoie un nombre aléatoire correspondant à un type de question'''
	select_game = randrange(1, 4)
	
	if select_game == 1:
		return capital()
	elif select_game == 2:
		return monnaie()
	else:
		return drapeau()

def getFourDifferentKeys(nbre_pays):
	'''retourne 4 pays différents'''
	key_response = randrange(1, nbre_pays)
	keysTab = [key_response]
	while (True):
		key_choice = randrange(1, nbre_pays)
		if key_choice not in keysTab:
			keysTab.append(key_choice)
		if len(keysTab) == 40:
			break
	return key_response, keysTab[1], keysTab[2], keysTab[3]

def getFourDifferentsCountriesWithCapitale(nbre_pays, rq_pays):
	'''retourne 4 pays différents contenant une capitale renseignée'''
	pays = rq_pays.json()
	while True:
		key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentKeys(nbre_pays)
		if "" not in (pays[key_reponse]["capital"], pays[key_choix_2]["capital"], pays[key_choix_3]["capital"], pays[key_choix_4]["capital"]):
			break
	return key_reponse, key_choix_2, key_choix_3, key_choix_4

def getFourDifferentsCountriesWithDifferentsDevises(nbre_pays, rq_pays):
	'''retourne 4 pays différents contenant des monnaies différentes'''
	pays = rq_pays.json()
	while True:
		key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentKeys(nbre_pays)
		listCurrencies =[pays[key_reponse]['currencies'][0]['name'], pays[key_choix_2]['currencies'][0]['name'], pays[key_choix_3]['currencies'][0]['name'], pays[key_choix_4]['currencies'][0]['name']]
		listUniqueCurrencies = list(set(listCurrencies))
		if len(listCurrencies) == len(listUniqueCurrencies):
			break
	return key_reponse, key_choix_2, key_choix_3, key_choix_4

def capital():

	#url_un_pays = "https://restcountries.eu/rest/v2/name/" + pays + "?fullText=true"
	url_total_pays = "https://restcountries.eu/rest/v2/all"

	rq_pays = requests.get(url_total_pays)
	# rq_total_pays = requests.get(url_total_pays)

	# r3 = requests.get("http://api.worldbank.org/countries?incomeLevel=LMC")

	nbre_pays = len(rq_pays.json())

	# key_reponse = randrange(1, nbre_pays)
	key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentsCountriesWithCapitale(nbre_pays, rq_pays)
	pays_reponse = rq_pays.json()[key_reponse]

	# key_choix_2 = randrange(1, nbre_pays)
	# key_choix_3 = randrange(1, nbre_pays)
	# key_choix_4 = randrange(1, nbre_pays)

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

	key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentsCountriesWithDifferentsDevises(nbre_pays, rq_pays)

	# key_reponse = randrange(1, nbre_pays)
	pays_reponse = rq_pays.json()[key_reponse]

	# key_choix_2 = randrange(1, nbre_pays)
	# key_choix_3 = randrange(1, nbre_pays)
	# key_choix_4 = randrange(1, nbre_pays)

	pays_choix2 = rq_pays.json()[key_choix_2]
	pays_choix3 = rq_pays.json()[key_choix_3]
	pays_choix4 = rq_pays.json()[key_choix_4]


	# return r2.content
	question = {}
	question["type"] = "monnaie_quiz.html"
	question["enonce"] = "Quel est la monnaie de " + pays_reponse['translations']["fr"] + " ?"
	question["reponse"] = pays_reponse['currencies'][0]['name']
	question["leschoix"] = []
	question["leschoix"].append(pays_reponse['currencies'][0]['name'])
	question["leschoix"].append(pays_choix2['currencies'][0]['name'])
	question["leschoix"].append(pays_choix3['currencies'][0]['name'])
	question["leschoix"].append(pays_choix4['currencies'][0]['name'])
	random.shuffle(question["leschoix"])



	return question


def drapeau():
	
	#url_un_pays = "https://restcountries.eu/rest/v2/name/" + pays + "?fullText=true"
	url_total_pays = "https://restcountries.eu/rest/v2/all"

	rq_pays = requests.get(url_total_pays)
	# rq_total_pays = requests.get(url_total_pays)

	# r3 = requests.get("http://api.worldbank.org/countries?incomeLevel=LMC")

	nbre_pays = len(rq_pays.json())

	# key_reponse = randrange(1, nbre_pays)
	key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentKeys(nbre_pays)

	pays_reponse = rq_pays.json()[key_reponse]

	# key_choix_2 = randrange(1, nbre_pays)
	# key_choix_3 = randrange(1, nbre_pays)
	# key_choix_4 = randrange(1, nbre_pays)

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
