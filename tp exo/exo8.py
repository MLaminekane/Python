libelle = input("libelle du produit: ")
quantite = int(input("quantite du produit: "))
prix_unitaire = float(input('prix unitaire: '))
mht = float(prix_unitaire)
mht == prix_unitaire
tva_normal = 0.2
tva_inter = 0.1
tva_red = 0.055
tva_sup_red = 0.021 
tva = int(input("choisir valeur TVA  entre 1 et 4: normal, intermediaire, reduit, super-reduit"))
if tva == 1:
    print("le prix TTC est: ",quantite* mht + (mht * tva_normal))
else:
    if tva == 2:
        print("le prix TTC est: ",quantite * mht + (mht * tva_inter))
    else:
        if tva == 3:
            print("le prix TTC est: ",quantite * mht + (mht * tva_red))
        else:
            if tva == 4:
                print("le prix TTC est: ",quantite * mht + (mht * tva_sup_red))
print("montant HT: ", mht)