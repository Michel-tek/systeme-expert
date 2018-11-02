#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Predicat:
	def __init__(self, nom, variable=[]):
		self.nom = nom
		self.variable=variable

	def __str__(self):
		return self.nom

	def __eq__(self, other):
		if isinstance(other, Predicat):
			return self.nom == other.nom
		return False

	def arite(self):
		return len(self.variable)

class Regle:
	def __init__(self, conditions, conclusion):
		self.conditions, self.conclusion = conditions, conclusion

	def __str__(self):
		string = "Si "
		for i in range(len(self.conditions)):
			string += ( "et " if i >=1 else "") +  str(self.conditions[i]) + " "
		string += "Alors " + str(self.conclusion)
		return string


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
		
		print("\nVoici notre but : \n\t" + str(but) + "\n")

		print("En partant des faits de base suivant :")
		for i, f in enumerate(self.faits):
			print("\n\t\t" + str(i) + " - " + str(f))

		print()

		appliquee=[False]*len(self.regles)
		modification = True

		while modification and ( list(filter(lambda x: x==False, appliquee)) != [] ) and (but == None  or not(but in self.faits) ) :
			modification = False
			for i , regle in enumerate(self.regles):
				if not(appliquee[i]):
					print("Avons nous appliquee la regle " + str(i) + " : \n\t" + str(regle) + " ?")
					if regle.conclusion in self.faits:
						print("\tOui!")
						modification = True
						appliquee[i] = True
						for c in regle.conditions:
							print("\tAjout de " + str(c)+ " à la liste de faits")
							self.faits.append(c)
					else:
						print("\tNon!")
				if modification:
					break
		print("fin du chainage arriere")



	def chainage_avant(self, but=None):
		if but != None:
			print("\nVoici notre but : \n\t" + str(but) + "\n")

		print("Partons des faits de base suivant :")
		for i, f in enumerate(self.faits):
			print("\t\t" + str(i) + " - " + str(f))

		print()

		appliquee=[False]*len(self.regles)
		modification = True
		while modification and ( list(filter(lambda x: x==False, appliquee)) != [] ) and (but == None  or not(but in self.faits) ):
			modification = False
			for i , regle in enumerate(self.regles):
				if not(appliquee[i]):
					print("Est-il possible d'appliquer la regle " + str(i) + " : \n\t" + str(regle) + " ?")
					if (list(filter(lambda x: x in self.faits, regle.conditions))) == regle.conditions:
						print("\tOui!")
						modification = True
						appliquee[i] = True
						print("\tAjout de " + str(regle.conclusion)+ " à la liste de faits")
						self.faits.append(regle.conclusion)
					else:
						print("\tNon!")
				if modification:
					break
		print("fin du chainage avant")
