# Mouhamed Lamine Kane 770977510
# exo3
entier = int(input("saisir un entier : "))
if entier %2==0 or entier < 0:
    print("ENTRER un nombre impair positif") 
else:
    reste = (entier*entier) % 3
    print(f"le nombre saisi est : {entier}")
    print(f"le carree de {entier} par 3 est {reste} ")