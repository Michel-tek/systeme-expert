import tkinter as Tk

class Interface(Tk.Frame):
	def __init__(self, master=None):
		Tk.Frame.__init__(self, master)
		self.grid()
		self.master.title("Moteur 0+")
