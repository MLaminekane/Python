age = int(input("entrer votre age: "))
sexe = input("entrer votre sexe: ") 
if age >= 18 and sexe == "masculin":
    print("vous etes un homme majeur")
else:
    if age >= 18 and sexe == "feminin":
        print("vous etes une femme majeur")
    else:
        if age < 18 and sexe == "masculin":
            print("vous etes un garcon ")
        else:
            if age < 18 and sexe == "feminin":
                print("vous etes une fille ")
                