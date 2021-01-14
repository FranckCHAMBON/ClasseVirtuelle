# [Carte de cinéma](http://www.france-ioi.org/algo/task.php?idChapter=527&idTask=1796)

## Énoncé

Vous êtes employé dans un cinéma et votre patron décide de lancer une offre spéciale. Toute personne possédant une carte de fidélité a le droit, pendant un mois, de voir un film gratuit par jour. Bien entendu certaines personnes vont essayer de tricher en venant plusieurs fois au cinéma dans la même journée et votre travail consiste à détecter ces tricheurs.

Si vous trouvez un tricheur, vous devez laisser votre caisse à un collègue, et emmener le tricheur chez votre patron qui lui confisquera sa carte de fidélité.

### Contraintes

* $0 \leqslant M \leqslant 1\,000\,000$, la valeur possible pour un numéro de carte de fidélité.
* $0 \leqslant N \leqslant 100\,000$, le nombre de clients venant au cinéma en une seule journée.

### Entrée

* La première ligne contient l'entier $N$, le nombre de clients de la journée.

* La seconde ligne contient leurs $N$ numéros de carte de fidélité.

### Sortie

* Vous devez écrire un seul entier, le numéro de carte de fidélité du premier tricheur que vous avez trouvé.

* S'il n'y avait pas de tricheur, écrivez la valeur -1.

### Exemples

#### Exemple 1

---

entrée :

    4
    10 2 3 2

sortie :

    2

---

#### Exemple 2

---

entrée :

    5
    11 3 17 13 19

sortie :

    -1

---

## Solution alternative

```python
def possède_doublon(liste):
    """Renvoie le premier doublon rencontré,
    sinon renvoie None."""
    déjà_vu = set()
    for x in liste:
        if x in déjà_vu:
            return x
        déjà_vu.add(x)


nb_clients = int(input())
numéros = list(map(int, input().split()))

doublon = possède_doublon(numéros)

print(doublon if doublon != None else "-1")
```

Ici, on utilise un ensemble (`set`) pour sauvegarder et rechercher rapidement parmi les clients déjà passés. Cependant, il s'agit d'une structure complexe à implémenter en général. Pouvons-nous en créer une simple dans le cadre de notre problème ?

> **Il faut penser au tableau de booléen** pour implémenter une structure d'ensemble lorsque les différentes clés peuvent avoir un indice contenu dans un intervalle qui rentre dans la mémoire disponible.
> Ici, les numéros de carte sont dans un intervalle de 1 million, et on dispose de 16 Mo de mémoire ; c'est adapté !

```python
class Ensemble:
    """Une classe qui implémente les ensembles d'entiers
    de 0 à indice_max donné à la construction."""
    
    def __init__(self, indice_max: int):
        self.présents = [False for _ in range(indice_max + 1)]
        self.indice_max = indice_max
    
    def ajoute(self, indice: int) -> None:
        if not(0 <= indice <= self.indice_max):
            raise ValueError("Indice hors intervalle")
        self.présents[indice] = True
    
    def est_présent(self, indice: int) -> bool :
        if not(0 <= indice <= self.indice_max):
            raise ValueError("Indice hors intervalle")
        return self.présents[indice]
    

def possède_doublon(liste):
    """Renvoie le premier doublon rencontré,
    sinon renvoie None."""
    déjà_vu = Ensemble(1000 * 1000)
    for x in liste:
        if déjà_vu.est_présent(x):
            return x
        déjà_vu.ajoute(x)


nb_clients = int(input())
numéros = list(map(int, input().split()))

doublon = possède_doublon(numéros)

print(doublon if doublon != None else "-1")
```
