#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml_reader import *


moteur = creation_moteur("faits_chien.xml", "regles_chien.xml")

print(moteur)

moteur.chainage_avant()

print("Résultat :")

print(moteur)
