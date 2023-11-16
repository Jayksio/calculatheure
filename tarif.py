import csv
from datetime import datetime

# les taux horaires de l'équipe
taux_horaires = {"Calypso": 16.48, "Alexandre": 11.52, "Pierre": 11.52, "Sophie": 11.52, "Jacques": 11.52, "Guillaume": 11.52}

def ajouter_donnees(nom, projet, heures):
    date_actuelle = datetime.now().strftime("%Y-%m-%d")  # format AAAA-MM-JJ, à modifier si besoin mais j'ai utilisé ce format pour faciliter le tri
    cout = taux_horaires[nom] * int(heures)
    with open('donnees.csv', 'a', newline='') as fichier:
        ecrivain = csv.writer(fichier)
        ecrivain.writerow([nom, projet, heures, cout, date_actuelle])

def calculer_cout_total_projet(nom_projet):
    total = 0
    with open('donnees.csv', 'r', newline='') as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            if ligne[1] == nom_projet:
                total += float(ligne[3])
    return round(total, 2)

def calculer_cout_et_heures_par_personne_et_projet(nom_personne, nom_projet):
    total_heures = 0
    total_cout = 0
    with open('donnees.csv', 'r', newline='') as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            if ligne[0] == nom_personne and ligne[1] == nom_projet:
                total_heures += int(ligne[2])
                total_cout += float(ligne[3])
    return total_heures, round(total_cout, 2)

def calculer_cout_et_heures_par_personne_projet_et_mois(nom_personne, nom_projet, mois, annee):
    total_heures = 0
    total_cout = 0
    with open('donnees.csv', 'r', newline='') as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            date = datetime.strptime(ligne[4], "%Y-%m-%d")
            if (ligne[0] == nom_personne and ligne[1] == nom_projet and 
                date.month == mois and date.year == annee):
                total_heures += int(ligne[2])
                total_cout += float(ligne[3])
    return total_heures, total_cout