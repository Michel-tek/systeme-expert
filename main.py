#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml_reader import *
from moteur import *
from interface import *

vp_start_gui()

"""
fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()

print("\n\nTEST CHAINAGE AVANT\n\n")

moteur = creation_moteur("regles_chien.xml")

liste_des_faits = recuperation_des_faits("faits_chien_avant.xml")

print(moteur)

moteur.chainage_avant(liste_des_faits, Predicat("le chien joue avec le facteur"))

print("\n\nRESULTAT CHAINAGE AVANT\n\n")

print(moteur)

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
"""