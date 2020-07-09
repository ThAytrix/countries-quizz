from random import randrange
import requests
import json
import requests
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getFourDifferentsCountriesWithCapitale(nbre_pays, rq_pays):
	'''Fonction retournant 4 pays différents contenant une capitale renseignée'''
	pays = rq_pays.json()
	while True:
		key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentKeys(nbre_pays)
		if "" not in (pays[key_reponse]["capital"], pays[key_choix_2]["capital"], pays[key_choix_3]["capital"], pays[key_choix_4]["capital"]):
			print(f"\t\t\t\t{bcolors.OKGREEN}Pas de pays sans capitale !{bcolors.ENDC}")
			break
		print(f"\t\t\t\t{bcolors.FAIL}Capitale non renseignée dans l'un des pays de la liste suivante donc liste non retenue !{bcolors.ENDC}")
		print(f"\t\t\t\tPays/capitale 1 : {pays[key_reponse]['name']}/{bcolors.OKGREEN}{pays[key_reponse]['capital']}{bcolors.ENDC}\n \
				Pays/capitale 2 : {pays[key_choix_2]['name']}/{bcolors.OKGREEN}{pays[key_choix_2]['capital']}{bcolors.ENDC}\n \
				Pays/capitale 3 : {pays[key_choix_3]['name']}/{bcolors.OKGREEN}{pays[key_choix_3]['capital']}{bcolors.ENDC}\n \
				Pays/capitale 4 : {pays[key_choix_4]['name']}/{bcolors.OKGREEN}{pays[key_choix_4]['capital']}{bcolors.ENDC}")
	return key_reponse, key_choix_2, key_choix_3, key_choix_4

def getFourDifferentsCountriesWithDifferentsDevises(nbre_pays, rq_pays):
	'''Fonction retournant 4 pays différents contenant des monnaies différentes'''
	pays = rq_pays.json()
	while True:
		key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentKeys(nbre_pays)
		listCurrencies =[pays[key_reponse]['currencies'][0]['name'], pays[key_choix_2]['currencies'][0]['name'], pays[key_choix_3]['currencies'][0]['name'], pays[key_choix_4]['currencies'][0]['name']]
		listUniqueCurrencies = list(set(listCurrencies))
		if len(listCurrencies) == len(listUniqueCurrencies):
			print(f"\t\t\t\t{bcolors.OKGREEN}Pas de monnaie en doublon !{bcolors.ENDC}")
			break
		print(f"\t\t\t\t{bcolors.FAIL}Monnaie en doublon dans la liste suivante donc liste non retenue !{bcolors.ENDC}")
		print(f"\t\t\t\tPays/monnaie 1 : {pays[key_reponse]['name']}/{pays[key_reponse]['currencies'][0]['name']}\n \
				Pays/monnaie 2 : {pays[key_choix_2]['name']}/{pays[key_choix_2]['currencies'][0]['name']}\n \
				Pays/monnaie 3 : {pays[key_choix_3]['name']}/{pays[key_choix_3]['currencies'][0]['name']}\n \
				Pays/monnaie 4 : {pays[key_choix_4]['name']}/{pays[key_choix_4]['currencies'][0]['name']}")
	return key_reponse, key_choix_2, key_choix_3, key_choix_4

def getFourDifferentKeys(nbre_pays):
	'''Fonction retournant 4 pays différents'''
	key_response = randrange(1, nbre_pays)
	keysTab = [key_response]
	while (True):
		key_choice = randrange(1, nbre_pays)
		if key_choice not in keysTab:
			# print(f"\t\t\t\tla clé {key_choice} n'était pas encore le tableau keysTab de taille ")
			keysTab.append(key_choice)
		# else:
		# 	print(f"\t\t\t\t{bcolors.FAIL}la clé {key_choice} est déjà dans le tableau keysTab{bcolors.ENDC}")
		# 	print(f"\t\t\t\t", end='')
		# 	for key in keysTab:
		# 		if key == key_choice:
		# 			print(f"{bcolors.WARNING}{key}{bcolors.ENDC} ", end='')
		# 		else:
		# 			print(f"{key} ", end='')
		# 	print()
		if len(keysTab) == 40:
			break
	return key_response, keysTab[1], keysTab[2], keysTab[3]

url_total_pays = "https://restcountries.eu/rest/v2/all"
rq_pays = requests.get(url_total_pays)
nbre_pays = len(rq_pays.json())

# teste le fait que l'application nous ressort 4 pays différents ayant des capitales renseignées

print("\n")
print(f"\t\t\t\t{bcolors.OKBLUE}TEST SUR LES CAPITALES{bcolors.ENDC}")
print("\n")

i = 0
while i < 30:
	key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentsCountriesWithCapitale(nbre_pays, rq_pays)
	i += 1

# teste le fait que l'application nous ressort 4 pays différents ayant des monnaies différentes

print("\n")
print(f"\t\t\t\t{bcolors.OKBLUE}TEST SUR LES MONNAIES{bcolors.ENDC}")
print("\n")

i = 0
while i < 30:
	key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentsCountriesWithDifferentsDevises(nbre_pays, rq_pays)
	i += 1

#  # teste le fait que l'application nous ressort 4 pays différents

# print("\n")
# print(f"\t\t\t\t{bcolors.OKBLUE}TEST SUR LES PAYS{bcolors.ENDC}")
# print("\n")

# key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentKeys(nbre_pays)
# print(f"\t\t\t\tkey_response : {key_reponse}\n \
#         \t\t\tkey_choix_2 : {key_choix_2}\n \
#         \t\t\tkey_choix_3 : {key_choix_3}\n \
#         \t\t\tkey_choix_4 : {key_choix_4}")
