# [Problème 4](https://prologin.org/train/2013/semifinal/gate_of_steiner)
> GATE OF STEINER

Niveau 2

## Énoncé

Tous les participants à GroLopin ont leur nom sur une carte !

Mais qui a obtenu le plus de lopins ? On vous donne la carte des joueurs, déterminer leur classement. En cas d'ex æquo, l'ordre importe peu (plusieurs réponses sont tolérées).

### Entrée

+ Sur la première ligne, deux nombres $N$ et $M$, respectivement la largeur et la longueur de la carte.
+ Sur les $N$ lignes suivantes : la carte de GroLopin. Une lettre minuscule représente un joueur, un `.` représente un lopin non acquis.

### Sortie

Sur une ligne, la chaîne formée des lettres minuscules, par ordre décroissant de nombre de lopins acquis.

### Contraintes

+ $1 \leqslant M, N \leqslant 500$

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 1000 kilo-octets
+ Temps d'exécution maximum : 500 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    3 3
    aab
    bac
    cca

Exemple de sortie

    acb

---

Exemple d'entrée

    4 4
    a.ac
    .bab
    ..a.
    cccc

Exemple de sortie

    cab

---

## Indices

1. Il serait bon de préparer au moins deux fonctions (que nous avons déjà vues) : 
    + une fonction qui donne une lettre en fonction de son indice (de 0 à 25).
    + une fonction qui donne un indice (de 0 à 25) en fonction d'une lettre minuscule.

2. Enfin, il sera utile de trier un tableau de couple (lettre, quantité) avec la quantité comme critère... Nous avons déjà vu comment faire.

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2013 - Problème 4 - GATE OF STEINER
https://prologin.org/train/2013/semifinal/gate_of_steiner
"""

def donne_lettre(i: int) -> str:
    """Renvoie la lettre minuscule d'indice i (de 0 à 25)
    >>> donne_lettre(0)
    'a'
    >>> donne_lettre(25)
    'z'
    """
    assert 0 <= i <= 25, f"i = {i} mais devrait être de 0 à 25"
    return chr(ord('a') + i)

def donne_indice(lettre: str) -> int:
    """Renvoie l'indice de la lettre minuscule, de 0 à 25
    >>> donne_indice('a')
    0
    >>> donne_indice('z')
    25
    """
    assert len(lettre) == 1, "il ne doit y avoir qu'un seul caractère"
    assert 'a' <= lettre <= 'z', f"'{lettre}' n'est pas une lettre minuscule"
    return ord(lettre) - ord('a')

# 1. initialisation d'une liste de 26 compteurs
compteurs = [0 for i in range(26)]

# 2. lecture de l'entrée
largeur, longueur = map(int, input().split())
for _ in range(largeur):
    ligne = input()
    assert len(ligne) == longueur, "Problème avec la longueur de la ligne"
    for caractère in ligne:
        if 'a' <= caractère <= 'z':
            # caractère est une lettre
            indice = donne_indice(caractère)
            compteurs[indice] += 1

# on construit une liste de couples (compteur, indice)
# + i est un indice, on filtre ceux qui ont un compteur > 0
# + compteur[i] donne l'effectif associé à i
# on a placé compteur en premier dans le couple,
# + on obtient ainsi un tri sur les compteurs,
# + on a choisit l'ordre inverse.

couples = [(compteurs[i], i) for i in range(26) if compteurs[i] > 0]
couples.sort(reverse=True)

# 3. écriture de la sortie
print("".join(donne_lettre(i) for q,i in couples))
```
