# No�mie SALAUN-PENQUER
# Mars 2016
# Integration velov
# en python 3.4

# 3 scripts disponibles:
	# 1/ Chargement et integration du Json velov (disponible en ligne)
	# 2/ Integration des json disponible sur un Drive 
	# 3/ Integration des json disponible dans un dossier

######### SCRIPT 1 ###########
# challenge_NSP_script1 

# Pr�requis:
	# Adresse de r�cup�ration du fichier: 'https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json'
	# Sch�ma de la table : int�gr� au code mais qui pourrait �tre stock� dans un fichier.txt et pass� en param�tre
	# V�rification de tous les packages n�cessaires � l'ex�cution du code 
	# import utils_ch_NSP


# 1 fichiers python:
	# challenge_NSP_script1 (host database_name table_name user pwd)
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
	# >C:\Python34\python challenge_NSP_script1.py "localhost:5432" "velov" "velov" "admin" "admin"
	# >La table � velov.velov � existe d�j�.
	# >Fichier charg� et modifi� avec succ�s
	# >Construction de la requ�te d'insertion
	# >Insertion des 348 entr�es pour 348 lignes du json
	# >Tps execution --- 0:00:01.727544  ---

######### SCRIPT 2 ###########
# challenge_NSP_script2

# Pr�requis:
	# client secret de l'adresse gmail: 'ldsa.velov@gmail.com' (demander le pwd)
	# Sch�ma de la table : int�gr� au code mais qui pourrait �tre stock� dans un fichier.txt et pass� en param�tre
	# V�rification de tous les packages n�cessaires � l'ex�cution du code 
	# import utils_ch_NSP
	# execution de createCredential.py 
	# Dans les 2 .py passer en param�tre le chemin du fichier client_secret.json : *home_dir*

# 1 fichiers python:
	# challenge_NSP_script2 (host database_name table_name user pwd)
		# host : adresse de la base de donn�es avec le num�ro de port
        	# database_name : nom de la base de donn�es
        	# table_name : nom de la table o� ins�rer les donn�es
        	# user : nom d'utilisateur pour se connecter � la base de donn�es
        	# pwd : mot de passe pour se connecter � la base de donn�es
	# MAIN:		
		# R�cup�ration des param�tres
		# V�rification de l'existence de la table
		# Connexion au Drive
		# Tant qu'il y a des json (seulement ceux du mois de f�vrier pour test):
			# Chargement d'un fichier
			# Int�gration (apr�s manipulations, tests)

# Exemple ex�cution :
	# >C:\Python34\python createCredential.py
	# 
	# >C:\Python34\python challenge_NSP_script2.py "localhost:5432" "velov" "velov" "admin" "admin"
	# ...
	# ...
