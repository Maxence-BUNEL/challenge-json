# No�mie SALAUN-PENQUER
# Mars 2016
# Chargement et integration du Json velov (disponible en ligne)
# en python 3.4

# Pr�requis:
	# Adresse de r�cup�ration du fichier: 'https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json'
	# Sch�ma de la table : int�gr� au code mais qui pourrait �tre stock� dans un fichier.txt et pass� en param�tre
	# V�rification de tous les packages n�cessaires � l'ex�cution du code 
	# import utils_ch_NSP


# 1 fichiers python:
	# challenge_NSP (host database_name table_name user pwd)
		# host : adresse de la base de donn�es avec le num�ro de port
        	# database_name : nom de la base de donn�es
        	# table_name : nom de la table o� ins�rer les donn�es
        	# user : nom d'utilisateur pour se connecter � la base de donn�es
        	# pwd : mot de passe pour se connecter � la base de donn�es

	# MAIN:		
		# R�cup�ration des param�tres
		# V�rification de l'existence de la table
		# R�cup�ration du fichier en ligne
		# Int�gration (apr�s manipulations, tests)
			
# Exemple ex�cution :
	# >C:\Python34\python challenge_NSP.py "localhost:5432" "velov" "velov" "admin" "admin"
	# >La table � velov.velov � existe d�j�.
	# >Fichier charg� et modifi� avec succ�s
	# >Construction de la requ�te d'insertion
	# >Insertion des 348 entr�es pour 348 lignes du json
	# >Tps execution --- 0:00:01.727544  ---