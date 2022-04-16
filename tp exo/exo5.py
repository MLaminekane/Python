from cmath import sqrt
from math import pi
import math

longueur = float(input("entrer la longueur: "))
largeur = float(input("entrer la largeur: "))
peri = 2*longueur+2*largeur
surface = longueur * largeur
diagonale = math.sqrt((longueur**2 + largeur**2))
print("perimetre: ", peri)
print("surface: ", surface)
print("diagonale: ", diagonale)