#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 05, 2018 04:36:21 PM CET  platform: Linux

from xml_reader import *
from tkinter import tix
import Pmw

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("1174x780+378+123")
        top.title("Moteur d'inférence")

        self.moteur = creation_moteur("regles_chien.xml")
        self.liste_des_faits = recuperation_des_faits("faits_chien_avant.xml")
        self.liste_but = self.generation_but()

        self.faits_list = [" "] + list(map(lambda f : str(f) , self.liste_but))
        
        self.Labelframe_regles_et_faits = tk.LabelFrame(top)
        self.Labelframe_regles_et_faits.place(relx=0.009, rely=0.006
                , relheight=0.387, relwidth=0.98)
        self.Labelframe_regles_et_faits.configure(relief='groove')
        self.Labelframe_regles_et_faits.configure(text='''Règles et faits''')
        self.Labelframe_regles_et_faits.configure(width=1150)

        self.Labelframe_regle = tk.LabelFrame(self.Labelframe_regles_et_faits)
        self.Labelframe_regle.place(relx=0.009, rely=0.066, relheight=0.877
                , relwidth=0.522, bordermode='ignore')
        self.Labelframe_regle.configure(relief='groove')
        self.Labelframe_regle.configure(text='''Règles''')
        self.Labelframe_regle.configure(width=600)

        self.Text_regles = tk.Text(self.Labelframe_regle)
        self.Text_regles.place(relx=0.017, rely=0.075, relheight=0.875
                , relwidth=0.96, bordermode='ignore')
        self.Text_regles.configure(background="white")
        self.Text_regles.configure(font="TkTextFont")
        self.Text_regles.configure(selectbackground="#c4c4c4")
        self.Text_regles.configure(width=576)
        self.Text_regles.configure(wrap='word')
        self.Text_regles.configure(state="disabled")

        self.Labelframe_faits = tk.LabelFrame(self.Labelframe_regles_et_faits)
        self.Labelframe_faits.place(relx=0.557, rely=0.066, relheight=0.613
                , relwidth=0.426, bordermode='ignore')
        self.Labelframe_faits.configure(relief='groove')
        self.Labelframe_faits.configure(text='''Faits''')
        self.Labelframe_faits.configure(width=490)

        self.Text_faits = tk.Text(self.Labelframe_faits)
        self.Text_faits.place(relx=0.02, rely=0.108, relheight=0.822
                , relwidth=0.951, bordermode='ignore')
        self.Text_faits.configure(background="white")
        self.Text_faits.configure(font="TkTextFont")
        self.Text_faits.configure(selectbackground="#c4c4c4")
        self.Text_faits.configure(width=466)
        self.Text_faits.configure(wrap='word')
        self.Text_faits.configure(state="disabled")

        self.Labelframe_fichiers = tk.LabelFrame(self.Labelframe_regles_et_faits)
        self.Labelframe_fichiers.place(relx=0.557, rely=0.695, relheight=0.248
                , relwidth=0.426, bordermode='ignore')
        self.Labelframe_fichiers.configure(relief='groove')
        self.Labelframe_fichiers.configure(text='''Fichiers''')
        self.Labelframe_fichiers.configure(width=490)

        self.Entry_regles = tk.Entry(self.Labelframe_fichiers)
        self.Entry_regles.place(relx=0.02, rely=0.533, height=20, relwidth=0.298
                , bordermode='ignore')
        self.Entry_regles.configure(background="white")
        self.Entry_regles.configure(font="TkFixedFont")
        self.Entry_regles.insert(tk.INSERT, "regles_chien.xml")

        self.Label_regles = tk.Label(self.Labelframe_fichiers)
        self.Label_regles.place(relx=0.02, rely=0.267, height=18, width=43
                , bordermode='ignore')
        self.Label_regles.configure(text='''Règles''')

        self.Entry_faits = tk.Entry(self.Labelframe_fichiers)
        self.Entry_faits.place(relx=0.367, rely=0.533, height=20, relwidth=0.298
                , bordermode='ignore')
        self.Entry_faits.configure(background="white")
        self.Entry_faits.configure(font="TkFixedFont")
        self.Entry_faits.insert(tk.INSERT, "faits_chien_avant.xml")

        self.Label_faits = tk.Label(self.Labelframe_fichiers)
        self.Label_faits.place(relx=0.367, rely=0.267, height=18, width=32
                , bordermode='ignore')
        self.Label_faits.configure(text='''Faits''')

        self.Button_chargement = tk.Button(self.Labelframe_fichiers)
        self.Button_chargement.place(relx=0.673, rely=0.267, height=36, width=157
                , bordermode='ignore')
        self.Button_chargement.configure(activebackground="#d9d9d9")
        self.Button_chargement.configure(text='''Chargement des fichiers''')
        self.Button_chargement.configure(command=self.bouton_chargement_xml)
        self.Button_chargement.configure(width=157)

        self.Labelframe_moteur = tk.LabelFrame(top)
        self.Labelframe_moteur.place(relx=0.009, rely=0.41, relheight=0.071
                , relwidth=0.98)
        self.Labelframe_moteur.configure(relief='groove')
        self.Labelframe_moteur.configure(text='''Moteur -- Chainage -- But''')
        self.Labelframe_moteur.configure(width=1150)

        self.Button2 = tk.Button(self.Labelframe_moteur)
        self.Button2.place(relx=0.765, rely=0.364, height=26, width=237
                , bordermode='ignore')
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(text='''Lancement du moteur''')
        self.Button2.configure(command=self.bouton_lancement_moteur)
        self.Button2.configure(width=237)

        self.var_choix = tk.StringVar()
        self.Radiobutton_avant = tk.Radiobutton(self.Labelframe_moteur)
        self.Radiobutton_avant.place(relx=0.052, rely=0.364, relheight=0.364
                , relwidth=0.055, bordermode='ignore')
        self.Radiobutton_avant.configure(activebackground="#d9d9d9")
        self.Radiobutton_avant.configure(justify='left')
        self.Radiobutton_avant.configure(text='''Avant''')
        self.Radiobutton_avant.configure(variable=self.var_choix)
        self.Radiobutton_avant.configure(value="avant")

        self.Radiobutton_arriere = tk.Radiobutton(self.Labelframe_moteur)
        self.Radiobutton_arriere.place(relx=0.157, rely=0.364, relheight=0.364
                , relwidth=0.059, bordermode='ignore')
        self.Radiobutton_arriere.configure(activebackground="#d9d9d9")
        self.Radiobutton_arriere.configure(justify='left')
        self.Radiobutton_arriere.configure(text='''Arrière''')
        self.Radiobutton_arriere.configure(variable=self.var_choix)
        self.Radiobutton_arriere.configure(value="arriere")

        #self.Entry3 = tk.Entry(self.Labelframe_moteur)
        #self.Entry3.place(relx=0.383, rely=0.364, height=20, relwidth=0.275
        #        , bordermode='ignore')
        #self.Entry3.configure(background="white")
        #self.Entry3.configure(font="TkFixedFont")
        #self.Entry3.configure(width=316)

        self.combo = Pmw.ComboBox(self.Labelframe_moteur, scrolledlist_items = self.faits_list)
        self.combo.place(relx=0.383, rely=0.364, height=20, relwidth=0.275, bordermode='ignore')

        self.Label_but = tk.Label(self.Labelframe_moteur)
        self.Label_but.place(relx=0.339, rely=0.364, height=18, width=25
                , bordermode='ignore')
        self.Label_but.configure(text='''But :''')

        self.Labelframe_resultat = tk.LabelFrame(top)
        self.Labelframe_resultat.place(relx=0.009, rely=0.5, relheight=0.442
                , relwidth=0.98)
        self.Labelframe_resultat.configure(relief='groove')
        self.Labelframe_resultat.configure(text='''Résultat''')
        self.Labelframe_resultat.configure(width=1150)

        self.Text3 = tk.Text(self.Labelframe_resultat)
        self.Text3.place(relx=0.009, rely=0.058, relheight=0.904, relwidth=0.553
                , bordermode='ignore')
        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(width=636)
        self.Text3.configure(wrap='word')
        self.Text3.configure(state="disabled")

        self.Text4 = tk.Text(self.Labelframe_resultat)
        self.Text4.place(relx=0.574, rely=0.058, relheight=0.904, relwidth=0.414
                , bordermode='ignore')
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(width=636)
        self.Text4.configure(wrap='word')
        self.Text4.configure(state="disabled")

        self.Button_quitter = tk.Button(top)
        self.Button_quitter.place(relx=0.498, rely=0.949, height=26, width=68)
        self.Button_quitter.configure(activebackground="#d9d9d9")
        self.Button_quitter.configure(command=root.quit)
        self.Button_quitter.configure(text='''Quitter''')

    def bouton_lancement_moteur(self):
        self.Text3.configure(state="normal")
        self.Text4.configure(state="normal")
        self.Text3.delete(1.0, tk.END)
        self.Text4.delete(1.0, tk.END)
        b = self.combo.get()
        but = None
        for lb in self.liste_but:
            if str(lb) == b:
                but = lb

        if self.var_choix.get() == "avant":
            # print("lancement du chainage avant")
            string = self.moteur.chainage_avant(self.liste_des_faits, but)
            self.Text3.configure(state="normal")
            self.Text3.insert(1.0, string)
            self.Text3.configure(state="disabled")
            string = ""
            for i, f in enumerate(self.liste_des_faits):
                string += "Fait " + str(i) + "\n\t" + str(f) + "\n"

            self.Text4.configure(state="normal")
            self.Text4.insert(1.0, string)
            self.Text4.configure(state="disabled")
            self.liste_des_faits = recuperation_des_faits(self.Entry_faits.get())

        elif self.var_choix.get() == "arriere":
            # print("lancement du chainage arriere")
            string = self.moteur.chainage_arriere(self.liste_des_faits, but)
            self.Text3.configure(state="normal")
            self.Text3.insert(1.0, string)
            self.Text3.configure(state="disabled")
            string = ""
            for i, f in enumerate(self.liste_des_faits):
                string += "Fait " + str(i) + "\n\t" + str(f) + "\n"

            self.Text4.configure(state="normal")
            self.Text4.insert(1.0, string)
            self.Text4.configure(state="disabled")
            self.liste_des_faits = recuperation_des_faits(self.Entry_faits.get())
        else:
            self.Text3.configure(state="normal")
            self.Text3.insert(1.0, "Veuillez choisir un type de chainage")
            self.Text3.configure(state="disabled")
            self.Text4.configure(state="normal")
            self.Text4.insert(1.0, "Veuillez choisir un type de chainage")
            self.Text4.configure(state="disabled")
            self.liste_des_faits = recuperation_des_faits(self.Entry_faits.get())

    def bouton_chargement_xml(self):
        self.Text_faits.configure(state="normal")
        self.Text_faits.delete(1.0, tk.END)
        self.Text_regles.configure(state="normal")
        self.Text_regles.delete(1.0, tk.END)
        self.moteur = creation_moteur(self.Entry_regles.get())
        self.liste_des_faits = recuperation_des_faits(self.Entry_faits.get())
        string = ""
        for i, f in enumerate(self.liste_des_faits):
            string += "Fait " + str(i) + "\n\t" + str(f) + "\n"

        self.Text_faits.configure(state="normal")
        self.Text_faits.insert(tk.INSERT, string)
        self.Text_faits.configure(state="disabled")
        self.Text_regles.configure(state="normal")
        self.Text_regles.insert(tk.INSERT, str(self.moteur))
        self.Text_regles.configure(state="disabled")

        self.liste_but = self.generation_but()

        self.combo.destroy()
        self.faits_list = [" "] + list(map(lambda f : str(f) , self.liste_but))
        self.combo = Pmw.ComboBox(self.Labelframe_moteur, scrolledlist_items = self.faits_list)
        self.combo.place(relx=0.383, rely=0.364, height=20, relwidth=0.275 , bordermode='ignore')

    def generation_but(self):
        liste_buts = []
        for r in self.moteur.regles:
            if not(r.conclusion in liste_buts):
                liste_buts += [r.conclusion]
            for c in r.conditions:
                if c not in liste_buts:
                    liste_buts += [c]

        return liste_buts

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)


if __name__ == '__main__':
    vp_start_gui()
