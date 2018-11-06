#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Predicat:
    """
    un predicat est composé d'un nom et éventuellement d'un opérateur et d'une valeur
    la surcharge de __eq__ permet de gérer l'égalité 
    ou la vérité de la comparaison si l'opérateur est différent de l'égalité
    """
    def __init__(self, nom="", operateur="", valeur=""):
        self.nom = nom
        self.operateur = operateur
        self.valeur = valeur

    def __str__(self):
        return str(self.nom) + (" " + str(self.operateur) + " " + (str(self.valeur) )if self.operateur is not None else "")

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
            return func(other)
        else:
            return False


class Coherence:

    def __init__(self, liste_predicat):
        self.coherence = tuple(liste_predicat)

    def __str__(self):
        string = "\nIl existe une incohérence entre les faits suivants : "
        for c in self.coherence:
            string += "\n\t" + str(c)
        return string


class Regle:

    def __init__(self, conditions, conclusion):
        self.conditions, self.conclusion = conditions, conclusion

    # def __str__(self):
    #     string = Colors.BOLD + "Si " + Colors.ENDC
    #     for i, condition in enumerate(self.conditions):
    #         string += ((Colors.BOLD + "et " + Colors.ENDC) if i >= 1 else "") + str(condition) + " "
    #     string += Colors.BOLD + "Alors " + Colors.ENDC + str(self.conclusion)
    #     return string

    def __str__(self):
        string = "Si "
        for i, condition in enumerate(self.conditions):
            string += ("et " if i >= 1 else "") + str(condition) + " "
        string += "\n\tAlors "+ str(self.conclusion)
        return string


class Moteur:
    def __init__(self, regles, coherences):
        self.regles = regles
        self. coherences = coherences

    def __str__(self):
        string="Règles : \n"
        for i, r in enumerate(self.regles):
            string += "Règle " + str(i) + " \n" + str(r) + "\n"
        if self.coherences is not []:
            string += "\nListe des incohérences : "
            for c in self.coherences:
                string += str(c)
        return string

    def chainage_avant(self, faits, but=None):
        string =""
        if self.test_coherence(faits):
            return "Il y a une incohérence dans les faits de base"
        if but:
            # print("\nVoici notre but : \n\t" + str(but) + "\n")
            string += "\nVoici notre but : \n\t" + str(but) + "\n"
        # print("Partons des faits de base suivant :")
        string += "Partons des faits de base suivant :\n"
        for i, f in enumerate(faits):
            # print("\t\t" + str(i) + " - " + str(f))
            string += "\n\t\t" + str(i) + " - " + str(f)
        # print("")
        string += "\n"

        appliquee = [False] * len(self.regles)
        modification = True
        while modification and (list(filter(lambda r: r is False, appliquee)) != []) and (
                but is None or not (but in faits)):
            modification = False
            for i, regle in enumerate(self.regles):
                if not (appliquee[i]):
                    # print("Est-il possible d'appliquer la regle " + str(i) + " : \n\t" + str(regle) + " ?")
                    string += "\nEst-il possible d'appliquer la regle " + str(i) + " : \n\t" + str(regle) + " ?"
                    if (list(filter(lambda fait: fait in regle.conditions, faits))) == regle.conditions:
                        # print(Colors.OKGREEN +"\tOui!" + Colors.ENDC)
                        string += "\n\tOui!"
                        modification = True
                        appliquee[i] = True
                        # print("\tAjout de " + str(regle.conclusion) + " à la liste de faits")
                        string += "\n\tAjout de " + str(regle.conclusion) + " à la liste de faits"
                        faits.append(regle.conclusion)
                        if self.test_coherence(faits):
                            return string + "\nl'ajout du dernier fait mène à une incohérence"
                    else:
                        # print(Colors.WARNING + "\tNon!" + Colors.ENDC)
                        string += "\n\tNon!"
                if modification:
                    break
        # print("fin du chainage avant")
        string += "\nfin du chainage avant"
        if but in faits:
            string += "\nLe but est atteint!"

        return string

    def chainage_arriere(self, faits, but=None):
        string = ""
        if but is None:
            # print("tu as besoin d un but dans ta vie")
            string += "Veuillez choisir un but"
            return string

        # print("\nVoici notre but : \n\t" + str(but) + "\n")
        string += "Voici notre but : \n\t" + str(but) + "\n"
        # print("En partant des faits de base suivant :")
        string += "En partant des faits de base suivant :"
        for i, f in enumerate(faits):
            # print("\t" + str(i) + " - " + str(f))
            string += "\n\t" + str(i) + " - " + str(f)
        # print("")
        string += "\n"

        appliquee = [False] * len(self.regles)
        modification = True

        while modification and (list(filter(lambda r: r is False, appliquee)) != []) and (
                but is None or not (but in faits)):
            modification = False
            for i, regle in enumerate(self.regles):
                if not (appliquee[i]):
                    # print("Avons nous appliqué la règle " + str(i) + " : \n\t" + str(regle) + " ?")
                    string += "\nAvons nous appliqué la règle " + str(i) + " : \n\t" + str(regle) + " ?"
                    if regle.conclusion in faits:
                        # print(Colors.OKGREEN +"\tOui!" + Colors.ENDC)
                        string += "\n\tOui!"
                        modification = True
                        appliquee[i] = True
                        for c in regle.conditions:
                            # print("\tAjout de " + str(c) + " à la liste de faits")
                            string += "\n\tAjout de " + str(c) + " à la liste de faits"
                            faits.append(c)
                            if self.test_coherence(faits):
                                return string + "\nl'ajout du dernier fait mène à une incohérence"
                    else:
                        # print(Colors.WARNING + "\tNon!" + Colors.ENDC)
                        string += "\n\tNon!"
                if modification:
                    break
        # print("fin du chainage arriere")
        string += "fin du chainage arriere"
        if but in faits:
            string += "Le but est atteint!"

        return string

    def test_coherence(self, faits):
        for f in faits:
            for c in self.coherences:
                if f in c.coherence:
                    for fait in c.coherence:
                        if fait != f:
                            if fait in faits:
                                return True

        return False