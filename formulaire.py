import tkinter as tk
from tkinter import ttk
import tarif  # Importation du module tarif


noms = ["Calypso", "Alexandre", "Pierre", "Sophie", "Jacques", "Guillaume"]
projets = ["AJP", "Colombbus", "10MW", "Renaissance"]

def soumettre():
    nom = nom_var.get()
    projet = projet_var.get()
    heures = heures_var.get()
    tarif.ajouter_donnees(nom, projet, heures)

fenetre = tk.Tk()
fenetre.title("Formulaire de saisie des heures")

nom_var = tk.StringVar()
projet_var = tk.StringVar()
heures_var = tk.StringVar()

ttk.Label(fenetre, text="Choisissez un nom :").grid(column=0, row=0)
nom_menu = ttk.Combobox(fenetre, textvariable=nom_var, values=noms)
nom_menu.grid(column=1, row=0)

ttk.Label(fenetre, text="Choisissez un projet :").grid(column=0, row=1)
projet_menu = ttk.Combobox(fenetre, textvariable=projet_var, values=projets)
projet_menu.grid(column=1, row=1)

ttk.Label(fenetre, text="Heures travaillées :").grid(column=0, row=2)
heures_entree = ttk.Entry(fenetre, textvariable=heures_var)
heures_entree.grid(column=1, row=2)

bouton_soumettre = ttk.Button(fenetre, text="Soumettre", command=soumettre)
bouton_soumettre.grid(column=1, row=3)

fenetre.mainloop()
