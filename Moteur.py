
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
'''
chainage arriere (but)

	sur une base de connaissance
	

'''





'''
chainage avant
	sur une base de fait
	tant que ajout_regle ou que toutes les regles n'ont pas ete activées
		chercher une regle qui peut etre appliquée
			ajout_regle est vrai
			ajout de la conclusion de la regle a la base de faits
			regle.activee = vrai

resultat lister tous les predicats atteints

chainage avant (but)
	sur une base de fait
	tant que ajout_regle ou que toutes les regles n'ont pas ete activées ou que le but n'est pas atteint
		chercher une regle qui peut etre appliquée
			ajout_regle est vrai
			ajout de la conclusion de la regle a la base de faits
			regle.activee = vrai
			si conclusion == but alors but_atteint = vrai

resultat lister tous les predicats atteints

'''
