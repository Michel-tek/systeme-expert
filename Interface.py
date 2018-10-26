import tkinter as Tk

class Interface(Tk.Frame):
	def __init__(self, master=None):
		## Initialisation de la fenêtre
		Tk.Frame.__init__(self, master)
		self.grid()
		self.master.title("Moteur 0+")

		## Grandes divisions

		self.cadre_controle = Tk.Frame(self, bd=2).grid()
		self.cadre_faits = Tk.Frame(self, bd=2).grid()

		## Option de chaînage avant ou arrière
		self.chainage         = Tk.IntVar()
		self.chainage_avant   = Tk.Radiobutton(self.cadre_controle, variable=self.chainage, value=0, text="Avant").grid()
		self.chainage_arriere = Tk.Radiobutton(self.cadre_controle, variable=self.chainage, value=1, text="Arrière").grid()
		#self.chainage_avant.grid()
		#self.chainage_arriere.grid()

	def changement_chainage(self):
		pass
