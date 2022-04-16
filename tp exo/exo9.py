nom = input("nom et prenom: ")
mois = int(input("mois de naissane: "))
jour = int(input(" jour de naissance: "))
annee = int(input("  votre annee de naissance: "))
an_en_cours = int(input("annee en cours: "))
age = an_en_cours - annee
print(f"Donnees de l'etudiant: {nom}, {mois}/{jour}/{annee}, {age} ans")