#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lxml import etree
from moteur import *


def creation_moteur(fichier_regles):
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

    liste_incoherence=[]
    for i, coherence in enumerate(regles.xpath("/regles/coherences/coherence")):
        liste_des_predicats=[]
        for p in coherence.xpath("predicat"):
            liste_des_predicats.append(Predicat(p.get("nom"), p.get("operateur"),p.get("valeur")))
        liste_incoherence.append(Coherence(liste_des_predicats))

    return Moteur(liste_des_regles, liste_incoherence)


def recuperation_des_faits(fichier_faits):
    faits = etree.parse(fichier_faits)

    liste_des_faits = []
    for fait in faits.xpath("/faits/predicat"):
        liste_des_faits.append(Predicat(fait.get("nom"), fait.get("operateur"), fait.get("valeur")))
    return liste_des_faits
