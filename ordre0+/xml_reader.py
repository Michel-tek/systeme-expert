#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lxml import etree
from moteur import *

def creation_moteur(fichier_faits, fichier_regles):
	regles = etree.parse(fichier_regles)

	liste_des_regles=[]

	for regle in regles.xpath("/regles/regle"):
		liste_des_conditions=[]
		conclusion = None
		for c in regle.xpath("conditions/predicat"):
			liste_des_conditions.append(Predicat(c.get("nom"), c.get("operateur"),c.get("valeur")))
		for c in regle.xpath("conclusion/predicat"):
			conclusion = Predicat(c.get("nom"), c.get("operateur"),c.get("valeur"))

		liste_des_regles.append(Regle(liste_des_conditions,conclusion))

	faits = etree.parse(fichier_faits)

	liste_des_faits=[]
	print("liste des faits :")
	for fait in faits.xpath("/faits/predicat"):
		liste_des_faits.append(Predicat(fait.get("nom"), fait.get("operateur"),fait.get("valeur")))

	
	return Moteur(liste_des_regles, liste_des_faits)
