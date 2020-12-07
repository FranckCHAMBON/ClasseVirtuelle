# [Problème 6](https://prologin.org/train/2013/semifinal/reverse_alchemying)
> Reverse Alchemying

Niveau 3

## Énoncé

Après d'innombrables essais allant du pas terrible au catastrophique, Merlin a enfin réussi à créer la potion de réduction du temps de dessalage de la morue et compte bien s'en vanter dans tout le royaume de Bretagne. Malheureusement à force de mélanger au hasard tous ces ingrédients il a fini par oublier ce dont il avait besoin pour débuter et il ne lui reste plus que des notes dans un carnet décrivant ce que donne chaque association d'ingrédients. Vous devez lui rafraîchir la mémoire en listant tous les ingrédients qu'il lui faut pour démarrer la préparation de cette potion qui à coup sûr révolutionnera le monde moderne !

### Entrée

L'entrée est de la forme:

+ `N M`
+ `id_res id1 id2 ...`
+ `...`
+ `ingredient0`
+ `ingredient1`
+ `...`

Avec $N$ le nombre d'ingrédients, $M$ le nombre de recettes, les id des entiers correspondant aux ingrédients formant les recettes `id_res = id1 + id2 + ...` et les ingrédients des chaînes de caractères présentées dans l'ordre de leur identifiant.

### Sortie

En sortie, vous devez afficher la liste des étapes, une par ligne et dans l'ordre de la recette (les ingrédients utilisés sont soit de base, soit déjà décomposés précédemment), sous la forme `RÉSULTAT = INGRÉDIENT + INGRÉDIENT + ...` puis une suite de chaînes de caractères correspondant aux ingrédients de base, c'est-à-dire ceux pour lesquels il n'y a pas de décomposition, nécessaires à la création de l'élément d'identifiant 0.

### Contraintes

+ $1 < N < 1500$
+ $1 < M < 300$


#### Contraintes d'exécution

Utilisation mémoire maximum : 1000 kilo-octets
Temps d'exécution maximum : 1000 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    16 7
    0 1 2
    1 3 4
    2 5 6 7
    3 8 9
    4 10 11
    5 12 13
    6 14 15
    potion
    mayo
    papier
    noix
    feu
    arbre
    ninja
    baleine
    encre
    sel
    ours
    mouche
    poil
    eau
    bois
    pierre

Exemple de sortie

    noix = encre + sel
    feu = ours + mouche
    mayo = noix + feu
    arbre = poil + eau
    ninja = bois + pierre
    papier = arbre + ninja + baleine
    potion = mayo + papier
    baleine pierre bois eau poil mouche ours sel encre 

---

Exemple d'entrée

    42 11
    0 1 2
    1 3 4 5 6 7
    2 8 9 10 11
    3 12 13 14 15 16
    4 17 18 19 20 21
    5 22 23
    6 24 25 26 27
    7 28 29 30 31
    12 32 33 34
    13 35 36 37 38
    14 39 40 41
    plastique
    cheveu
    bierre
    azote
    eau
    cafe
    parahydroxybenzoate
    savon
    polyhexadifluoromethane
    poil
    plomb
    plume
    or
    poivre
    tabac
    uranium
    dent
    papier
    guitare
    os
    acide
    air
    marteau
    argent
    oeil
    corde
    aluminium
    mousse
    tasse
    dentifrice
    sel
    faucille
    poire
    chien
    klaxon
    fluoromethyle
    feu
    moustache
    fer
    ninja
    sucre
    cristal

Exemple de sortie

    or = poire + chien + klaxon
    poivre = fluoromethyle + feu + moustache + fer
    tabac = ninja + sucre + cristal
    azote = or + poivre + tabac + uranium + dent
    eau = papier + guitare + os + acide + air
    cafe = marteau + argent
    parahydroxybenzoate = oeil + corde + aluminium + mousse
    savon = tasse + dentifrice + sel + faucille
    cheveu = azote + eau + cafe + parahydroxybenzoate + savon
    bierre = polyhexadifluoromethane + poil + plomb + plume
    plastique = cheveu + bierre
    aluminium faucille uranium poire mousse fluoromethyle corde dent dentifrice oeil plume marteau tasse feu fer polyhexadifluoromethane klaxon cristal plomb sel ninja papier argent guitare moustache air sucre poil chien os acide

---

## Indices

+ Une solution qui utilise la récursivité est facile à écrire.

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2013 - Problème 6 - Reverse Alchemying
https://prologin.org/train/2013/semifinal/reverse_alchemying
"""

nb_ingrédients, nb_recettes = map(int, input().split())

recettes = dict()
for _ in range(nb_recettes):
    numéros = tuple(map(int, input().split()))
    recettes[numéros[0]] = numéros[1:]

ingrédients = [input() for _ in range(nb_ingrédients)]

def affiche(id_produit: int) -> None:
    if id_produit in recettes:
        for id_sous_produit in recettes[id_produit]:
            affiche(id_sous_produit)
        print(ingrédients[id_produit], end=" = ")
        ingrédients_produit = (ingrédients[i] for i in recettes[id_produit])
        print(" + ".join(ingrédients_produit))

affiche(0)
# récursivement, affiche avant les ingrédients nécessaires avec leur formule

# et les produits de base
for id_produit in range(nb_ingrédients):
    if id_produit not in recettes:
        print(ingrédients[id_produit], end=" ")
```