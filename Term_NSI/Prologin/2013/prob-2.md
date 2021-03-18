# [Problème 2](https://prologin.org/train/2013/semifinal/qi)
> QI

Niveau 1

## Énoncé

Terry Pratchett a écrit : « *the IQ of a mob is the IQ of its most stupid member divided by the number of mobsters* »¹. On vous donne la liste des QI des membres d'un groupe, calculer le QI du groupe.

> ¹ « Le QI d'un groupe est le QI de son membre le plus stupide divisé par le nombre de personnes du groupe. »

### Entrée

+ Sur la première ligne, le nombre $N$ de personnes dans le groupe.
+ Sur la deuxième ligne, la liste des QI des membres du groupe.

### Sortie

Un entier, représentant la partie entière du QI du groupe.

### Contraintes

+ $1 \leqslant N \leqslant 100$
+ $0 \leqslant \text{QI}_i \leqslant 1000$

#### Contraintes d'exécution

* Utilisation mémoire maximum : 1000 kilo-octets

* Temps d'exécution maximum : 100 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    2
    90 110

Exemple de sortie

    45

---

Exemple d'entrée

    3
    100 110 160

Exemple de sortie

    33

---

## Indices


Pensez à bien choisir vos identifiants ; vous êtes aussi notés sur la qualité de votre code, pas seulement son efficacité.

## Solution

### Basique

```python
nb_personnes = int(input())
liste_qi = list(map(int, input().split()))

plus_bas_qi = min(liste_qi)
qi_groupe = plus_bas_qi // nb_personnes
print(qi_groupe)
```

### Avec POO

```python
"""
auteur : Franck CHAMBON
Régional 2013 - Problème 2 - QI
https://prologin.org/train/2013/semifinal/qi
"""

class Groupe():
    def __init__(self) -> None:
        "Constructeur"
        self.__liste_qi = []
    
    def taille(self) -> int:
        "Renvoie le nombre de membres"
        return len(self.__liste_qi)
    
    def ajoute(self, un_qi: int) -> None:
        "Ajoute un_qi d'un nouveau membre du groupe"
        self.__liste_qi.append(un_qi)
    
    def qi(self) -> int:
        "Renvoie la partie entière du QI du groupe suivant la définition de Pratchett"
        return min(self.__liste_qi) // self.taille()

# initialisation
groupe = Groupe()

## lecture de l'entrée
nb_personnes = int(input())
for qi in map(int, input().split()):
    groupe.ajoute(qi)

## test optionnel
assert nb_personnes == groupe.taille(), "Erreur avec le nombre de personnes !"

## écriture sortie
print(groupe.qi())
```