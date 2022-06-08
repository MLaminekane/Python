# ecrire un programme qui demande a l'utilisateur de saisir un numero de face de des.
#  le programme demande a un autre utilisateur de deviner le premier numero.
# le programme doit afficher le message "essayer encore" dans le cas ou le deuxieme utilisateur 
# n'a pas deviner le numero correct sinon le programme affiche bravo vous avez devinez apres tant de tentatives


uti1 = int(input("entrer un nombre de dess: "))
while uti1 < 1 or uti1 > 6:
    print("entrer de bons nombre")
    uti1 = int(input("entrer un nombre de dess: "))
uti2 = int(input("deviner le nombre:"))
cpt=1
while uti2 != uti1:
    uti2 = int(input("deviner encore: "))
    cpt += 1
print(f"vous avec reussi avec {cpt} tentatives")