from tkinter.ttk import *
from tkinter import IntVar, BooleanVar, N, S, W, E

class Interface(Frame):
	def __init__(self, master=None):
		## Initialisation de la fenêtre
		Frame.__init__(self, master)
		self.grid()
		self.master.title("Moteur 0+")
		self.grid_configure(sticky=(N, S, E, W))

		## Grandes divisions
		self.divisions = Notebook(self)
		self.divisions.grid(sticky=(N, S, E, W))
		self.divisions.grid_anchor(anchor="center")

		self.base = Frame(self.divisions)
		self.divisions.add(self.base, text="Base")

		self.cas  = Frame(self.divisions)
		self.divisions.add(self.cas, text="Cas")
		self.cas.columnconfigure(0, weight=1)
		self.cas.rowconfigure(0, weight=1)

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
		self.lance  = BooleanVar
		self.lancer = Button(self.cadre_controle, text="Lancer").grid(sticky=W)



	def changement_chainage(self):
		pass
