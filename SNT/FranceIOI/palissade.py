nb_maisons = int(input())

abs_mini = 1000000
abs_maxi = 0
ord_mini = 1000000
ord_maxi = 0

for x in range(nb_maisons):
    maison_abs = int(input())
    maison_ord = int(input())
    
    if maison_abs < abs_mini:
        abs_mini = maison_abs
    
    if maison_abs > abs_maxi:
        abs_maxi = maison_abs
    
    if maison_ord < ord_mini:
        ord_mini = maison_ord
    
    if maison_ord > ord_maxi:
        ord_maxi = maison_ord

# on est sorti de la boucle
# on affiche le périmètre

# print("absmaxi", abs_maxi)
# print("absmini", abs_mini)
# print("ordmaxi", ord_maxi)
# print("ordmini", ord_mini)

largeur = abs_maxi - abs_mini
hauteur = ord_maxi - ord_mini
périmètre = (largeur + hauteur) * 2

print(périmètre)
