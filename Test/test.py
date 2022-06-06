# invites = ["Abdoulaye", "Diakhaté", "Racine"]
# print(f"Je t'invite à un diner {invites[0]}.")
# print(f"Je t'invite à un diner {invites[1]}.")
# print(f"Je t'invite à un diner {invites[2]}.")
# invites.pop()
# invites.append("Dabo")
# print(f"Je t'invite à un diner {invites[2]}.")
# print("j'ai trouvé une plus grande table pour les invités donc j'invite d'autres personnes")
# invites.append("Annita")
# invites.insert(0, "Guetti")
# invites.insert(3, "Moussa")
# invites.insert(4, "mata")
# print(invites)
# print("sorry but i c'ant invite two person only")
# invites.pop()
# print(f"désolé de pas pouvoir vous inviter {invites[5]}.")
# invites.pop()
# print(f"désolé de pas pouvoir vous inviter {invites[4]}.")
# invites.pop()
# print(f"désolé de pas pouvoir vous inviter {invites[3]}.")
# invites.pop()
# print(f"désolé de pas pouvoir vous inviter {invites[2]}.")
# invites.pop()
# print(f"désolé de pas pouvoir vous inviter {invites[1]}.")
# print(invites)
# print(invites)
# stillInvites = invites
# print(f"vous êtes toujours invités {invites} ")
# del invites[0]
# del invites[-1]
# print(invites)
# print(invites)

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 4, 6])
y = np.array([2, 3, 5, 1])
plt.plot(x, y)

plt.show() # affiche la figure a l'ecran