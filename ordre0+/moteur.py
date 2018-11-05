#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    RED = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Predicat:
    def __init__(self, nom="", operateur="", valeur=""):
        self.nom = nom
        self.operateur = operateur
        self.valeur = valeur

    def __str__(self):
        return Colors.OKBLUE + str(self.nom) + Colors.ENDC + (" " + Colors.RED + str(self.operateur) + Colors.ENDC + " " + Colors.RED + (str(self.valeur) + Colors.ENDC )if self.operateur is not None else "")

    def eq(self, other):
        return self.valeur == other.valeur

    def inf(self, other):
        return int(self.valeur) < int(other.valeur)

    def sup(self, other):
        return int(self.valeur) > int(other.valeur)

    def sup_eq(self, other):
        return int(self.valeur) >= int(other.valeur)

    def inf_eq(self, other):
        return int(self.valeur) <= int(other.valeur)

    def dif(self, other):
        return self.valeur != other.valeur

    def __eq__(self, other):
        # print("Début de comparaison entre")
        # print(self)
        # print("et")
        # print(other)
        # print("operateur self: " + (self.operateur if self.operateur is not None else "pas d'operateur"))
        # print("operateur other: " + (other.operateur if other.operateur is not None else "pas d'operateur"))
        if not (isinstance(other, Predicat)):
            return False
        if self.nom == other.nom:
            switch = {
                "=": self.eq,
                "<": self.inf,
                ">": self.sup,
                "<=": self.inf_eq,
                ">=": self.sup_eq,
                "!=": self.dif
            }
            func = switch.get(self.operateur, self.eq)
            # print("comparaison : " + self.nom + " ( " + (self.valeur if self.valeur is not None else "pas de valeur") + " ) " + (self.operateur if self.operateur is not None else "pas d'operateur") + " " + other.nom + " ( " + (other.valeur if other.valeur is not None else "pas de valeur") + " ) " + " resultat : " + str(func(other)))
            return func(other)
        else:
            return False


class Regle:

    def __init__(self, conditions, conclusion):
        self.conditions, self.conclusion = conditions, conclusion

    def __str__(self):
        string = Colors.BOLD + "Si " + Colors.ENDC
        for i, condition in enumerate(self.conditions):
            string += ((Colors.BOLD + "et " + Colors.ENDC) if i >= 1 else "") + str(condition) + " "
        string += Colors.BOLD + "Alors " + Colors.ENDC + str(self.conclusion)
        return string


class Moteur:
    def __init__(self, regles):
        self.regles = regles

    def __str__(self):
        string = "*Liste des règles :"
        for i, r in enumerate(self.regles):
            string += "\n\tRègle " + str(i) + " " + str(r)
        return string

    def chainage_avant(self, faits, but=None):
        if but:
            print("\nVoici notre but : \n\t" + str(but) + "\n")

        print("Partons des faits de base suivant :")
        for i, f in enumerate(faits):
            print("\t\t" + str(i) + " - " + str(f))

        print("")

        appliquee = [False] * len(self.regles)
        modification = True
        while modification and (list(filter(lambda r: r is False, appliquee)) != []) and (
                but is None or not (but in faits)):
            modification = False
            for i, regle in enumerate(self.regles):
                if not (appliquee[i]):
                    print("Est-il possible d'appliquer la regle " + str(i) + " : \n\t" + str(regle) + " ?")
                    if (list(filter(lambda condition: condition in faits, regle.conditions))) == regle.conditions:
                        print(Colors.OKGREEN +"\tOui!" + Colors.ENDC)
                        modification = True
                        appliquee[i] = True
                        print("\tAjout de " + str(regle.conclusion) + " à la liste de faits")
                        faits.append(regle.conclusion)
                    else:
                        print(Colors.WARNING + "\tNon!" + Colors.ENDC)
                if modification:
                    break
        print("fin du chainage avant")

    def chainage_arriere(self, faits, but=None):
        if but is None:
            print("tu as besoin d un but dans ta vie")
            return

        print("\nVoici notre but : \n\t" + str(but) + "\n")

        print("En partant des faits de base suivant :")
        for i, f in enumerate(faits):
            print("\t" + str(i) + " - " + str(f))

        print("")

        appliquee = [False] * len(self.regles)
        modification = True

        while modification and (list(filter(lambda r: r is False, appliquee)) != []) and (
                but is None or not (but in faits)):
            modification = False
            for i, regle in enumerate(self.regles):
                if not (appliquee[i]):
                    print("Avons nous appliqué la regle " + str(i) + " : \n\t" + str(regle) + " ?")
                    if regle.conclusion in faits:
                        print(Colors.OKGREEN +"\tOui!" + Colors.ENDC)
                        modification = True
                        appliquee[i] = True
                        for c in regle.conditions:
                            print("\tAjout de " + str(c) + " à la liste de faits")
                            faits.append(c)
                    else:
                        print(Colors.WARNING + "\tNon!" + Colors.ENDC)
                if modification:
                    break
        print("fin du chainage arriere")
