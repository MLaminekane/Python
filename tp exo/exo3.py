from math import pi
r = float(input('entrer le rayon du cercle: '))
aire = pi*r**2
peri = pi*r*2
if r >= 0 :
    print("son diametre: ", aire)
    print("son perimetre: ", peri)