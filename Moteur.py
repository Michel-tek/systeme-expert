
class Predicat:
	def __init__(self, nom, variable=[]):
		self.nom = nom
		self.variable=variable

	def arite(self):
		return len(self.variable)


class Condition:
	def __int__(self, predicat):
		self.predicat = predicat


class Regle: # premise : predicat , conclusion : liste de predicat
	def __init__(self, premise, conclusion=[]):
		self.premise, self.conclusion = premise, conclusion


class BaseDeConnaissance:
	def __init__(self, regles=[], faits=[]):
		self.regles , self.faits = regles, faits


class Moteur:
	def __init__(self, base_de_connaissance):
		self.base_de_connaissance = base_de_connaissance

	def chainage_avant(self, but=None):
		return

	def chainage_arriere(self, but=None):
		if (but == None):
			print("tu as besoin d'un but dans ta vie")
			return


'''
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

'''

