n=int(input("Entrer un entier Positif: \n"))
for a in range (1,n+1):
    s=0
    for i in range(1,a):
        if(a%i==0):
            s= s+i
    if(s==a):
        print(a," est parfait")
        
