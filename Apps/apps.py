# try:
#     x = int(input("la valeur de x: "))
# except ValueError:
#     print("vous avez entre autre qu'un nombre")
# print(f"x est {x}")

#def bonjour():
#    print("bonjour")

#name = input("votre nom: ")
#bonjour()
#print(name)



nombre = int(input("entrer un nombre: "))
try:
    nombre = int(input("entrer un nombre: "))
except ValueError:
    print("entrer un bon nombre")
    