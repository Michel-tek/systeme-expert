#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml_reader import *
from moteur import *
from interface import *

vp_start_gui()

"""

print("\n\nTEST CHAINAGE AVANT\n\n")

moteur = creation_moteur("regles_chien.xml")

liste_des_faits = recuperation_des_faits("faits_chien_arriere.xml")

print(moteur)

print("\n\nRESULTAT CHAINAGE AVANT\n\n")

print(moteur.chainage(liste_des_faits, False , False, Predicat("le temps", "=", "soleil")))# , Predicat("le chien joue avec le facteur")))


string = "\n\t*Liste des faits"
for i, f in enumerate(liste_des_faits):
    string += "\n\t\t" + str(i) + " - " + str(f)
print(string)

"""
"""
print("\n\nTEST CHAINAGE AVANT\n\n")

moteur = creation_moteur("regles_chien.xml")

liste_des_faits = recuperation_des_faits("faits_chien_avant.xml")

print(moteur)

print("\n\nRESULTAT CHAINAGE AVANT\n\n")

print(moteur.chainage_avant(liste_des_faits, Predicat("le chien joue avec le facteur")))


string = "\n\t*Liste des faits"
for i, f in enumerate(liste_des_faits):
    string += "\n\t\t" + str(i) + " - " + str(f)
print(string)


print("\n\nTEST CHAINAGE ARRIERE\n\n")

liste_des_faits = recuperation_des_faits("faits_chien_arriere.xml")

moteur.chainage_arriere(liste_des_faits, Predicat("le temps", "=", "soleil"))

print("\n\nRESULTAT CHAINAGE ARRIERE\n\n")

print(moteur)

string = "\n*Liste des faits"
for i, f in enumerate(liste_des_faits):
    string += "\n\t" + str(i) + " - " + str(f)
print(string)




*Liste des faits
        0 - le chien va chercher la balle et la rapporte dans la main = gauche
        1 - le facteur lance la balle = rouge
        2 - le facteur prend une balle
        3 - la couleur de la balle = rouge
        4 - le facteur arrive
        5 - le chien sort de la maison
        6 - l'heure >= 10
        7 - le temps = soleil

"""


