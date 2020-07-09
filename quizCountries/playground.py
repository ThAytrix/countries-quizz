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

def getFourDifferentKeys(nbre_pays):
	key_response = randrange(1, nbre_pays)
	keysTab = [key_response]
	while (True):
		key_choice = randrange(1, nbre_pays)
		if key_choice not in keysTab:
			print(f"la clé {key_choice} n'était pas encore le tableau keysTab de taille ")
			keysTab.append(key_choice)
		else:
			print(f"{bcolors.FAIL}la clé {key_choice} est déjà dans le tableau keysTab{bcolors.ENDC}")
			for key in keysTab:
				if key == key_choice:
					print(f"{bcolors.WARNING}{key}{bcolors.ENDC} ", end='')
				else:
					print(f"{key} ", end='')
			print()
		if len(keysTab) == 40:
			break
	return key_response, keysTab[1], keysTab[2], keysTab[3]

url_total_pays = "https://restcountries.eu/rest/v2/all"
rq_pays = requests.get(url_total_pays)
nbre_pays = len(rq_pays.json())
key_reponse, key_choix_2, key_choix_3, key_choix_4 = getFourDifferentKeys(nbre_pays)
print(f"\t key_response : {key_reponse}\n \
        key_choix_2 : {key_choix_2}\n \
        key_choix_3 : {key_choix_3}\n \
        key_choix_4 : {key_choix_4}\n")
