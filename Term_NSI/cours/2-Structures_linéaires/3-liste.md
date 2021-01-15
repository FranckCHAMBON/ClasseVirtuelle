# 🚛 Structures linéaires - La liste {ignore=true}

## Sommaire {ignore=true}

[TOC]

## Le maillon

Dans une tentative de définition récursive de la pile, en Python, on a vu l'intérêt d'avoir un objet qui regroupe un élément et un lien vers la suite de la pile. Nous avions utilisé un tuple `(tête, queue)`, où `tête` était l'élément au sommet, et `queue` la suite des données de la pile, mais nous n'avions pas pu donner le status de pile à la `queue`. En utilisant deux classes, nous y arriverons.

Un maillon possède deux attributs, un élément et un **lien** vers le suivant.

```python
class Maillon:
    """Un maillon est donné par son élément et son maillon suivant à droite,
    éventuellement None."""

    def __init__(self, élément, droite):
        self.élément = élément
        self.droite = droite

    def __str__(self):
        return str(self.élément)
```

Voici un exemple d'utilisation simple.

```python
m_1 = Maillon(42, None)
m_2 = Maillon(1337, m_1)
m_3 = Maillon(2021, m_2)
```

$$\boxed{m_3:(2021, \text{vers }m_2)} \rightarrow \boxed{m_2:(1337, \text{vers }m_1)} \rightarrow \boxed{m_1:(42, \text{vers le vide})} \rightarrow \text{Nil}$$

> **Nil** représente le vide.

Avec Python, le passage de paramètres se fait par un lien, l'adresse mémoire, ainsi les objets `m_1` et `m_2` ne sont pas copiés dans `m_2` et `m_3`, seule leur adresse est donnée.

On devine qu'on va pouvoir avec cette structure construire les méthodes pour une pile, mais aussi pour une file, pour une deque, et plus encore. On va pouvoir supprimer un maillon au milieu d'une chaîne en faisant pointer le précédent sur un autre maillon, et pour insérer un maillon, il suffira de modifier les suivants de deux maillons...

## Listes chaînées

On va utiliser deux classes :
* Une classe `Maillon` qui contient un élément et le suivant dans la liste.
* Une classe `Liste` qui contient un maillon de tête et les méthodes pour la faire vivre.

On commence par construire les méthodes analogues à une pile, ensuite on complètera en deque.

### Première approche, implémenter la pile

```python
class Maillon:
    """Un maillon est donné par son élément et son maillon suivant à droite,
    éventuellement None."""

    def __init__(self, élément, droite):
        self.élément = élément
        self.droite = droite

    def __str__(self):
        return str(self.élément)


class Liste:
    "Une liste est donnée par son maillon de gauche"

    def __init__(self):
        self.maillon_gauche = None
    
    def est_vide(self):
        return self.maillon_gauche is None
    
    def ajout_gauche(self, élément):
        self.maillon_gauche = Maillon(élément, self.maillon_gauche)

    def extrait_gauche(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        élément = self.maillon_gauche.élément
        self.maillon_gauche = self.maillon_gauche.droite
        return élément
    
    def __str__(self):
        affichage = "Contenu : "
        maillon = self.maillon_gauche
        while maillon is not None:
            affichage += str(maillon) + "::"
            maillon = maillon.droite
        affichage += " fin."
        return affichage
    
```

**Exercice** : tester cette implémentation. Sur FranceIOI par exemple.

### Implémenter la deque

Implémenter la deque est de difficulté comparable à implémenter la file, autant faire mieux immédiatement, on aura indirectement la file.

**Exercice** : compléter la classe pour obtenir les méthodes de la deque. Ces méthodes sont-elles toutes efficaces ? Tester sur FranceIOI par exemple.


## Listes doublement chaînées

On utilise un nouveau type de maillon, qui possède trois attributs :
* son élément de donnée,
* un lien vers la gauche,
* un lien vers la droite.

**Exercice** : réécrire une implémentation de la deque avec une liste doublement chaînée. Les méthodes sont-elles toutes efficaces ? Tester sur FranceIOI par exemple.
