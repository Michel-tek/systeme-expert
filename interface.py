from tkinter.ttk import *
from tkinter import IntVar, BooleanVar, N, S, W, E

class Interface(Frame):
	def __init__(self, master=None):
		## Initialisation de la fenêtre
		Frame.__init__(self, master)
		self.grid()
		self.master.title("Moteur 0+")

		## Grandes divisions
		self.divisions = Notebook(self, padding=(0, 30, 0, 0))
		self.divisions.grid()

		self.base = Frame(self.divisions)
		self.divisions.add(self.base, text="Base")
		self.base.grid()

		self.cas  = Frame(self.divisions)
		self.divisions.add(self.cas, text="Cas")
		self.cas.grid()

		self.cadre_faits    = Labelframe(self.cas, text="Faits")
		self.cadre_faits.grid(column=0, sticky=(N, S, E, W))
		self.cadre_controle = Labelframe(self.cas, text="Controle")
		self.cadre_controle.grid(column=1, sticky=(N, S))

		## Controle:
		##    Option de chaînage avant ou arrière
		self.chainage         = IntVar(0)
		self.chainage_avant   = Radiobutton(self.cadre_controle, variable=self.chainage, value=0, text="Avant")
		self.chainage_avant.grid(sticky=W)
		self.chainage_arriere = Radiobutton(self.cadre_controle, variable=self.chainage, value=1, text="Arrière")
		self.chainage_arriere.grid(sticky=W)

		##    Lancer
		self.lance  = BooleanVar()
		self.lancer = Button(self.cadre_controle, text="Lancer")
		self.lancer.grid(sticky=W)



	def changement_chainage(self):
		pass
