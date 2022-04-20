a = float(input("entrer a: "))
b = float(input("entrer b: "))
add = a + b;
sous = a - b;
multi = a * b;
div = a / b;
print("choisir entre 1 et 4: + , - , * , /")
choix = int(input("choix: "))
if choix == 1 :
    print(add)
else:
    if choix == 2 :
        print(sous)
    else:
        if choix == 3 :
            print(multi)
        else:
            if choix == 4 and choix != 0 :
                print(f"{div:.2f}")
            else:
                print("error")
            