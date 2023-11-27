import tkinter as tk
from tkinter import ttk
import tarif

def soumettre():
    nom = nom_var.get()
    projet = projet_var.get()
    heures = heures_var.get()
    tarif.ajouter_donnees(nom, projet, heures)

def afficher_cout_total():
    projet = projet_var.get()
    total = tarif.calculer_cout_total_projet(projet)
    label_resultat.config(text=f"Coût total pour {projet}: {total}€")

def afficher_cout_personne_projet_mois():
    nom = nom_var.get()
    projet = projet_var.get()
    mois = int(mois_var.get())
    annee = int(annee_var.get())
    heures, cout = tarif.calculer_cout_et_heures_par_personne_projet_et_mois(nom, projet, mois, annee)
    label_resultat.config(text=f"{nom} a travaillé {heures} heures sur {projet} en {mois}/{annee}. Coût total: {cout}€")

# fenêtre principale
fenetre = tk.Tk()
fenetre.title("Formulaire de saisie des heures")

# style
font_label = ('Arial', 14)
font_bouton = ('Arial', 14, 'bold')
font_resultat = ('Arial', 16, 'bold')

color_background = "#ffffff"
color_button = "#ff3366"
color_text = "#000000"

fenetre.configure(background=color_background)

# variables tkinter
nom_var = tk.StringVar()
projet_var = tk.StringVar()
heures_var = tk.StringVar()
mois_var = tk.StringVar()
annee_var = tk.StringVar()

ttk.Label(fenetre, text="Choisissez un nom :", font=font_label, background=color_background, foreground=color_text).grid(column=0, row=0)
nom_menu = ttk.Combobox(fenetre, textvariable=nom_var, values=["Calypso", "Alexandre", "Pierre", "Sophie", "Jacques", "Guillaume"])
nom_menu.grid(column=1, row=0)

ttk.Label(fenetre, text="Choisissez un projet :", font=font_label, background=color_background, foreground=color_text).grid(column=0, row=1)
projet_menu = ttk.Combobox(fenetre, textvariable=projet_var, values=["AJP", "Colombbus", "10MW", "Renaissance"])
projet_menu.grid(column=1, row=1)

ttk.Label(fenetre, text="Heures travaillées :", font=font_label, background=color_background, foreground=color_text).grid(column=0, row=2)
heures_entree = ttk.Entry(fenetre, textvariable=heures_var)
heures_entree.grid(column=1, row=2)

ttk.Label(fenetre, text="Mois (MM):", font=font_label, background=color_background, foreground=color_text).grid(column=0, row=3)
mois_entree = ttk.Entry(fenetre, textvariable=mois_var)
mois_entree.grid(column=1, row=3)

ttk.Label(fenetre, text="Année (AAAA):", font=font_label, background=color_background, foreground=color_text).grid(column=0, row=4)
annee_entree = ttk.Entry(fenetre, textvariable=annee_var)
annee_entree.grid(column=1, row=4)

bouton_soumettre = ttk.Button(fenetre, text="Soumettre", command=soumettre)
bouton_soumettre.grid(column=1, row=5)

bouton_cout_total = ttk.Button(fenetre, text="Calculer le coût total du projet", command=afficher_cout_total)
bouton_cout_total.grid(column=1, row=6)

bouton_cout_personne_projet_mois = ttk.Button(fenetre, text="Calculer par personne, mois et projet", command=afficher_cout_personne_projet_mois)
bouton_cout_personne_projet_mois.grid(column=1, row=7)

label_resultat = ttk.Label(fenetre, text="", font=font_resultat, background=color_background, foreground=color_text)
label_resultat.grid(column=1, row=8)

# interface utilisateur
fenetre.mainloop()