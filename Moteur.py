
class Predicat:
    def __init__(self, nom, variable=[]):
        self.nom = nom
        self.variable=variable

    def arite(self):
        return len(self.variable)


class Condition:
    def __int__(self, predicat):
	self.predicat = predicat


class Regle: # premise : predicat , conclusion : liste de predicat
    def __init__(self, premise, conclusion=[]):
        self.premise, self.conclusion = premise, conclusion


class BaseDeConnaissance:
    def __init__(self, regles=[], faits=[]):
        self.regles , self.faits = regles, faits


class Moteur:
    def __init__(self, base_de_connaissance):
        self.base_de_connaissance = base_de_connaissance

    def chainage_avant(self):
        return

    def chainage_arriere(self):
        return


print("coucou")
p1 = Predicat("nuage")
p2 = Predicat("soleil")


'''
class Fait:
    def __init__(self, predicat):
        self.predicat = predicat
'''

'''
    base de connaissance
        regles
            dictionnaire avec le nom de la fonction en clé et les variables dans une liste en valeur
        faits
            dictionnaire avec 
'''
