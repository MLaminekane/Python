# ecrire un programme qui permet de saisir 3 entiers impairs.
# le programme affiche la somme de ces 3 entiers impairs
som = int()
retry = int
n1 = 0
n2 = 0
n3 = 0
while n1 / 2 == 0 or n2 / 2 == 0 or n3 / 2 == 0:
    n1 = int(input("enter le 1er entier: "))
    n2 = int(input("enter le 2eme entier: "))
    n3 = int(input("enter le 3eme entier: "))
    retry = print("entrer des valeurs impairs: ")
    n1 = int(input("enter le 1er entier: "))
    n2 = int(input("enter le 2eme entier: "))
    n3 = int(input("enter le 3eme entier: "))
    if n1 / 2 != 0 and n2 / 2 != 0 and n3 / 2 != 0 :
        som = n1 + n2 + n3
        print(f"la somme est: {som}")

