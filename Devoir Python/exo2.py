n= int(input("Entrer une valeur: "))
som=0
s=0
for i in range(0, n+1):
    n= int(input("Entrer une valeur: "))
    s = s+n+i
    som = s 
    if i %10 and i>10 and i <55:
        print("le produit est:",i)
print("La sommme est:  ", som)
