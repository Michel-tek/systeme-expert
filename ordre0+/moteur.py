#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Predicat:
    def __init__(self, nom="", operateur="", valeur=""):
        self.nom = nom
        self.operateur = operateur
        self.valeur = valeur

    def __str__(self):
        return str(self.nom) + (" " + str(self.operateur) + " " + str(self.valeur) if self.operateur is not None else "")

    def inf(self, other):
        return int(self.valeur) < int(other.valeur)

    def sup(self, other):
        return int(self.valeur) > int(other.valeur)

    def inf_eq(self, other):
        return int(self.valeur) <= int(other.valeur)

    def sup_eq(self, other):
        return int(self.valeur) >= int(other.valeur)

    def eq(self, other):
        return self.valeur == other.valeur

    def dif(self, other):
        return self.valeur != other.valeur

    def __eq__(self, other):
        print("Début de comparaison entre")
        print(self)
        print("et")
        print(other)
        print("operateur self: " + (self.operateur if self.operateur is not None else "pas d'operateur"))
        print("operateur other: " + (other.operateur if other.operateur is not None else "pas d'operateur"))
        if not (isinstance(other, Predicat)):
            return False
        if self.nom == other.nom:
            switch = {
                "<": self.inf(other),
                ">": self.sup(other),
                "<=": self.inf_eq(other),
                ">=": self.sup_eq(other),
                "==": self.eq(other),
                "!=": self.dif(other)
            }
            func = switch.get(self.operateur, self.eq(other))
            return func
        else:
            return False


class Regle:

    def __init__(self, conditions, conclusion):
        self.conditions, self.conclusion = conditions, conclusion

    def __str__(self):
        string = "Si "
        for i, condition in enumerate(self.conditions):
            string += ("et " if i >= 1 else "") + str(condition) + " "
        string += "Alors " + str(self.conclusion)
        return string


class Moteur:
    def __init__(self, regles, faits):
        self.regles, self.faits = regles, faits

    def __str__(self):
        string = "Voici la base de connaissance du moteur :"
        string += "\n\t*Liste des règles :"
        for i, r in enumerate(self.regles):
            string += "\n\t\tRègle " + str(i) + " " + str(r)
        string += "\n\t*Liste des faits"
        for i, f in enumerate(self.faits):
            string += "\n\t\t" + str(i) + " - " + str(f)
        return string

    def chainage_arriere(self, but=None):
        if but is None:
            print("tu as besoin d un but dans ta vie")
            return

        print("\nVoici notre but : \n\t" + str(but) + "\n")

        print("En partant des faits de base suivant :")
        for i, f in enumerate(self.faits):
            print("\t\t" + str(i) + " - " + str(f))

        appliquee = [False] * len(self.regles)
        modification = True

        while modification and (list(filter(lambda x: x == False, appliquee)) != []) and (
                but is None or not (but in self.faits)):
            modification = False
            for i, regle in enumerate(self.regles):
                if not (appliquee[i]):
                    print("Avons nous appliquee la regle " + str(i) + " : \n\t" + str(regle) + " ?")
                    if regle.conclusion in self.faits:
                        print("\tOui!")
                        modification = True
                        appliquee[i] = True
                        for c in regle.conditions:
                            print("\tAjout de " + str(c) + " à la liste de faits")
                            self.faits.append(c)
                    else:
                        print("\tNon!")
                if modification:
                    break
        print("fin du chainage arriere")

    def chainage_avant(self, but=None):
        if but:
            print("\nVoici notre but : \n\t" + str(but) + "\n")

        print("Partons des faits de base suivant :")
        for i, f in enumerate(self.faits):
            print("\t\t" + str(i) + " - " + str(f))

        print()

        appliquee = [False] * len(self.regles)
        modification = True
        while modification and (list(filter(lambda x: x == False, appliquee)) != []) and (
                but is None or not (but in self.faits)):
            modification = False
            for i, regle in enumerate(self.regles):
                if not (appliquee[i]):
                    print("Est-il possible d'appliquer la regle " + str(i) + " : \n\t" + str(regle) + " ?")
                    if (list(filter(lambda x: x in regle.conditions, self.faits))) == regle.conditions:
                        print("\tOui!")
                        modification = True
                        appliquee[i] = True
                        print("\tAjout de " + str(regle.conclusion) + " à la liste de faits")
                        self.faits.append(regle.conclusion)
                    else:
                        print("\tNon!")
                if modification:
                    break
        print("fin du chainage avant")
