equipe1 = input("nom equipe 1: ")
equipe2 = input("nom equipe 2: ")
score1 = int(input("score equipe 1: "))
score2 = int(input("score equipe 2: "))
print(f"le score de la rencontre entre l'equipe {equipe1} face a l'equipe {equipe2} est de: {score1} - {score2}")
if score1<0 or score2<0:
     print("entrer un nombre positif")
     if equipe1 == int() and equipe2 == int():
         print("entrer les valeurs correctes")