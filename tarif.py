import csv

taux_horaires = {"Calypso": 16.48, "Bob": 11.52, "Pierre": 11.52}

def ajouter_donnees(nom, projet, heures):
    cout = taux_horaires[nom] * heures
    with open('donnees.csv', 'a', newline='') as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow([nom, projet, heures, cout])

def calculer_couts_et_heures(projet):
    total_heures = 0
    total_cout = 0
    with open('donnees.csv', 'r') as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            if ligne[1] == projet:
                total_heures += int(ligne[2])
                total_cout += float(ligne[3])
    return total_heures, total_cout
