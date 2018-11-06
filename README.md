# Système expert

## Le projet

	Ce projet est divisé en 3 parties principales, la gestion des fichiers xml, le moteur et l'interface graphique 

### Les fichiers xml

### Faits

	les 

Le moteur possède une liste de règles, celles ci sont constituées de conditions et conclusion (liste de prédicats).
Un prédicat est composé d'un nom et si besoin un opérateur et d'une valeur.

les infos suivantes ne sont ni bonnes ni à jour...

le moteur est une classe abstraite avec une liste de faits et une liste de regles
	la liste de faits est un ensemble de predicats
	la liste de regles comprend des conditions (plusieurs predicats) donnant accès à une conclusion (un prédicat)
	
ainsi que les fonctions
	initialisation des bases de faits et regles (fichier.xml)
	chainage avant (but=None, profondeur=true)
	chainage arriere (but=None, profondeur=true)
	verification des conditions(regle)
	verification de la conclusion(regle)
	
	
Fonctionnement du chainage avant:
	variables :
		appliquee[] 	# tableau de la taille de la liste des regles initialisé a faux
		faits 		# attribut de classe
		regles		# attribut de classe
		modification	# booleen informant de modification lors du déroulement de l'algorithme
		
	code :
		modification = vrai
		Tant que ( 	
			modification 
			&& 
			(filtre sur appliquee pour verifier qu'il reste des regles a appliquer) 
			&& 
			(but==None || but n'appartient pas à la base de faits )
			 )
			modification = faux
			Pour i allant de 0 à Regles.size
				Si !appliquee[i]
					Si verifications des conditions(Regles[i])(toutes les conditions appartiennent aux faits)
						modification = vrai
						appliquee[i] = vrai
						Si profondeur
							ajouter Regles[i].conclusion à la fin des faits
						sinon
							ajouter Relges[i].conclusion au debut des faits
						break de la boucle pour i (est ce que c'est vraiment utile?)
			fin boucle pour i
			update de l'interface
		fin boucle tant que
		retourne but atteint (vrai ou faux(ou None est ce que c'est possible?? sinon 1 2 ou 3))
	ensuite traitement par l'interface graphique 
	(utilisation de yield pour verifier a chaquavecavece etape dans la boucle???????? possible?
	sinon appel a une fonction update de l'interface graphique pour afficher quelle regle est appliquee et l'etat de la base de faits)

fonctionnement chainage arrière:
	variables :
		appliquee[] 	# tableau de la taille de la liste des regles initialisé a faux
		faits 		# attribut de classe
		regles		# attribut de classe
		modification	# booleen informant de modification lors du déroulement de l'algorithme
		
	code :
		modification = vrai
		Tant que ( 	
			modification 
			&& 
			(filtre sur appliquee pour verifier qu'il reste des regles a appliquer) 
			&& 
			(but==None || but n'appartient pas à la base de faits )
			 )
			modification = faux
			Pour i allant de 0 à Regles.size
				Si !appliquee[i]
					Si verifications de la conclusion(Regles[i]) (la conclusion appartient à la base de faits)
						modification = vrai
						appliquee[i] = vrai
						Si profondeur
							ajouter Regles[i].conditions à la fin des faits
						sinon
							ajouter Relges[i].conditions au debut des faits
						break de la boucle pour i (est ce que c'est vraiment utile?)
			fin boucle pour i
			update de l'interface
		fin boucle tant que
		retourne but atteint (vrai ou faux (ou None est ce que c'est possible?? sinon 1 2 ou 3))
	ensuite traitement par l'interface graphique 
