# ecrire un programme qui permet de saisir le nom et le prenom d'un prof.
# le programme affiche "bonjour monnsieur nandite" dans le cas ou le prof est aly
# ali tall prenom
# niang : 

nom_prof = input("entrer votre nom: ")
prenom = input("enter votre prenom: ")
if nom_prof == "Niang" and prenom == "Aly Tall":
    print("bonjour monsieur nandite")
elif nom_prof != "Niang" and prenom != "Aly Tall":
    print("bonjour")