import csv

# Dictionnaire des taux horaires pour chaque personne
taux_horaires = {"Calypso": 16.48, "Alexandre": 11.52, "Pierre": 11.52, "Sophie": 11.52, "Jacques": 11.52, "Guillaume": 11.52,}

def ajouter_donnees(nom, projet, heures):
    cout = taux_horaires[nom] * int(heures)
    with open('donnees.csv', 'a', newline='') as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow([nom, projet, heures, cout])
