# Noémie SALAUN-PENQUER
# Mars 2016
# Chargement et integration du Json velov (disponible en ligne)
# en python 3.4

# Prérequis:
	# Adresse de récupération du fichier: 'https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json'
	# Schéma de la table : intégré au code mais qui pourrait être stocké dans un fichier.txt et passé en paramètre
	# Vérification de tous les packages nécessaires à l'exécution du code 
	# import utils_ch_NSP


# 1 fichiers python:
	# challenge_NSP (host database_name table_name user pwd)
		# host : adresse de la base de données avec le numéro de port
        	# database_name : nom de la base de données
        	# table_name : nom de la table où insérer les données
        	# user : nom d'utilisateur pour se connecter à la base de données
        	# pwd : mot de passe pour se connecter à la base de données

	# MAIN:		
		# Récupération des paramètres
		# Vérification de l'existence de la table
		# Récupération du fichier en ligne
		# Intégration (après manipulations, tests)
			
# Exemple exécution :
	# >C:\Python34\python challenge_NSP.py "localhost:5432" "velov" "velov" "admin" "admin"
	# >La table « velov.velov » existe déjà.
	# >Fichier chargé et modifié avec succès
	# >Construction de la requête d'insertion
	# >Insertion des 348 entrées pour 348 lignes du json
	# >Tps execution --- 0:00:01.727544  ---