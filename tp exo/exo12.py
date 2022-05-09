# ecrire un programme qui permet de gerer la gestion les employes de l'entreprise tesla.....

# le programme permet de saisir les donnees d'un employe puis de lui montrer son salaire net.

# les donnees de l'employe sont: son nom, son prenom, son annee de naissance,

# situation matrimoniale, genre, nombre d'enfants, duree d'anciennete

# salaire net = salaire de base + prime - taxes

# l'etat prend 18% du salaire de l'employe alors que l'entreprise elle meme prends 5% du salaire

# les employes suivant ont droit a des primes:

#   - 2% pour les mariees, chaque enfant d'un employe marie a 1%

#   - dans l';entreprise y a une prime dedie aux femmes qui est de 0.5% pour toutes les femmes qui ont aux moins

#       dure 3ans dans l'entreprise

#   - les directeurs ont un prime de 2% alors que les vigiles femmes auront 5% de prime de salaire

# les retraites ont un salaire egale a 35% de leur salaire de base


age = int()
taxes = int()
enfants = int()
nom = input("Nom et Prenom: ")
genre = int(input("votre genre = homme ou femme (1 ou 2): "))
jour= int(input("jour de naissance: "))
mois = int(input("mois de naissance: "))
en_cours = int(input("annee en cours: "))   
naissance = int(input("annee de naissance: "))
annee = int()
annee = en_cours - naissance
age = print(f"mois et anne de naissance = {jour} / {mois} / {annee}")
print(f"votre age: {annee}")
situation = int(input("marie ou celibataire(1 ou 2): "))
prime = int()
if situation == 1:
    prime = 2/100
else:
    prime == 0
enfants = int()
if situation == 1 and situation >= 1:
    prime = 2/100 + enfants / 100   
anciennete = int(input("annee anciennete: "))
if anciennete >= 3 and genre == 2:
    prime = 0.5/100
else:
    if genre == 1:
        prime = 0
sal_net_retraite = int()
salaire_base = int(input("votre salaire de base: "))
salaire_net = int()
taxes_ent = int()
taxes_etat = int()
fonction = int(input(" vous etes: directeur, vigile-homme, vigile-femme, retraite; (1 a 4): "))
if fonction == 1:
    prime = 0.02
elif fonction == 2:
    prime == 0
elif fonction == 3:
    prime == 0.02
elif fonction == 4:
    prime == salaire_base + salaire_base * 0.35

taxes_etat = salaire_base * 18/100
taxes_ent = salaire_base * 5/100
taxes = taxes_ent + taxes_etat

salaire_net = salaire_base + prime - taxes_ent - taxes_etat
print(salaire_net)