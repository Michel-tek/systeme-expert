#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml_reader import *


print("\n\nTEST CHAINAGE AVANT\n\n")

moteurAV = creation_moteur("faits_chien_avant.xml", "regles_chien.xml")

print(moteurAV)

moteurAV.chainage_avant(Predicat("le chien joue avec le facteur"))

print("\n\nRESULTAT CHAINAGE AVANT\n\n")

print(moteurAV)


print("\n\nTEST CHAINAGE ARRIERE\n\n")


moteurAR = creation_moteur("faits_chien_arriere.xml", "regles_chien.xml")

moteurAR.chainage_arriere(Predicat("il fait beau"))


print("\n\nRESULTAT CHAINAGE ARRIERE\n\n")

print(moteurAR)
