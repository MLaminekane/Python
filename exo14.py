# Exercice 1 : Un nombre est parfait s’il est égal à la somme de ses diviseurs stricts (différents
# de lui-même). Ainsi par exemple, l’entier 6 est parfait car 6 = 1 + 2 + 3. Écrire un algorithme
# permettant de déterminer si un entier naturel est un nombre parfait


n = int()
if n > 0:
    for i in range(1,n//2 +1):
        if n%i==0:
            s = s+1
        if s==n:
            print("nombre parfait") 
        else:
            print("non parfait")
else:
    print("entrer un nombre positif")
    