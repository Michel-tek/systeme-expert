
#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Predicat:
	def __init__(self, nom, variable=[]):
		self.nom = nom
		self.variable=variable

	def __str__(self):
		return self.nom

	def arite(self):
		return len(self.variable)


class Condition:
	def __int__(self, predicat):
		self.predicat = predicat

	def __str__(self):
		return str(self.predicat)

class Regle: # premise : predicat , conclusion : liste de predicat
	def __init__(self, conditions, conclusion):
		self.conditions, self.conclusion = conditions, conclusion

	def __str__(self):
		string = "Si "
		for i in range(len(self.conditions)):
			string += ( "et " if i >=1 else "")+  str(self.conditions[i]) + " "
		string += "Alors " + str(self.conclusion)
		return string
''' useless
class BaseDeConnaissance:
	def __init__(self, regles=[], faits=[]):
		self.regles , self.faits = regles, faits
'''

class Moteur:
	def __init__(self, regles=[], faits=[]):
		self.regles , self.faits = regles, faits

	def __str__(self):
		string = "Voici la base de connaissance du moteur :"
		string += "\n\t*Liste des regles :"
		for r in self.regles:
			string += "\n\t\t- " + str(r)
		string += "\n\t*Liste des faits"
		for f in self.faits:
			string += "\n\t\t- " + str(f)
		return string


	def chainage_arriere(self, but=None):
		if (but == None):
			print("tu as besoin d un but dans ta vie")
		return

	def verification_condition(self, regle):
		return

	def chainage_avant(self, but=None, profondeur = True):
		appliquee=[]
		for i in range(len(self.regles)):
			appliquee.append(False)
		modification = True

		while modification and ( list(filter(lambda x: x==False, appliquee)) != [] and (but == None  or (list(filter(lambda x: x==but, self.faits))) ) ):
			#print("modification " + str(modification) + " appliquee = " +str(( list(filter(lambda x: x==True, appliquee)))))
			modification = False
			for i in range(len(self.regles)):
				if not(appliquee[i]):
					print("Est-il possible d'appliquer la regle " + str(i) + " : \n\t" + str(self.regles[i]) + " ?")
					if (list(filter(lambda x: x in self.faits, self.regles[i].conditions))) == self.regles[i].conditions:
						print("\tOui!")
						modification = True
						appliquee[i] = True
						print("ajout de " + str(self.regles[i].conclusion))
						if profondeur:
							self.faits.append(self.regles[i].conclusion)
						else:
							self.faits.insert(0,self.regles[i].conclusion)
						break
					else:
						print("\tNon!")
		#print("modification " + str(modification) + " appliquee = " +str(( list(filter(lambda x: x==True, appliquee)))))
		#print("liste des faits finaux :")
		#for f in self.faits:
		#	print("\t- " + str(f))
		print("fin du chainage_avant")
		return


print("Let's begin")

beau = Predicat("il fait beau")
pluie = Predicat("il pleut")

chien_dehors = Predicat("le chien peut aller dehors")
chien_interieur = Predicat("le chien ne peut pas sortir")

chien_heureux = Predicat("le chien est heureux")
chien_triste = Predicat("le chien est triste")

facteur_arrive = Predicat("le facteur arrive")

facteur_heureux = Predicat("le chien joue avec le facteur")
facteur_triste = Predicat("le chien aboie sur le facteur")

balle = Predicat("le facteur lance la baballe")

balle_le_retour = Predicat("le chien rapporte la baballe")

regle_beau_dehors = Regle([beau],chien_dehors)
regl_pluie_interieur = Regle([pluie],chien_interieur)
regle_dehors_heureux = Regle([chien_dehors], chien_heureux)
regle_dehors_facteur_balle = Regle([chien_dehors, facteur_arrive],balle)
regle_balle_rapporte = Regle([balle],balle_le_retour)

moteur = Moteur([regle_beau_dehors, regl_pluie_interieur, regle_dehors_heureux,regle_dehors_facteur_balle, regle_balle_rapporte],[beau,facteur_arrive])

print(str(moteur))


moteur.chainage_avant()

print(str(moteur))

'''
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

'''


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

