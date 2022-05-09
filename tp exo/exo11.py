nom = input("entrer votre nom: ")
age = int(input("entrer votre age: "))
salaire = int(input("entrer votre salaire: "))
print(f"nom: {nom} \n{age} \n{salaire}")
if age >= 18:
    if salaire >50_000:
        print("vous etes majeur et riche: ")
if age < 18:
    if salaire > 50_000:
        print("vous etes mineur et riche")
if salaire < 50_000 and salaire >= 0:
    print("vous etes pauvre")

