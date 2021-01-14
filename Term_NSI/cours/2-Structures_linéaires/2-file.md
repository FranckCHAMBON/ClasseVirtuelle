# 🚛 Structures linéaires - La file, la deque {ignore=true}

## Sommaire {ignore=true}

[TOC]

## La file

* Le principe de la **pile** est : *LIFO : Last In, First Out*, (dernier entré, premier sorti).
* Le principe de la **file** est : *FIFO : First In, First Out*, (premier entré, premier sorti).

![file](assets/FIFO_PEPS.png)

> Wikipedia [file](https://fr.wikipedia.org/wiki/File_(structure_de_donn%C3%A9es))

### Utilisations concrètes

* Les travaux à imprimer sont envoyés dans une file, le premier arrivé sera le premier servi.
* Un processeur reçoit des calculs à effectuer, ils arrivent dans une file. L'ordonnanceur est souvent plus élaboré qu'une simple file, et des travaux prioritaires peuvent être traités avant.

**Exercice 1** : En s'inspirant de la **première** implémentation de la pile, donner une implémentation d'une **file** d'une certaine taille maximale. On proposera le constructeur ainsi que les méthodes `.est_vide(self)`, `.enfile(self, élément)` et `.défile(self)` analogues au cas de la pile.

**Exercice 2** : En utilisant une implémentation de la pile, donner une implémentation de la file. On utilisera deux piles.
> On pourra s'inspirer d'une situation de jeux de cartes avec deux piles : la pioche et la défausse. Quand la pioche est vide, on retourne la défausse qui devient la pioche.

**Exercice 3** : Résoudre le problème [Distributeur automatique](http://www.france-ioi.org/algo/task.php?idChapter=527&iOrder=2) sur France-IOI.

> **Aide** : on pourra considérer [ce devoir](TAD-file-eval.pdf) et ses indications.

> **Conseil** : on peut résoudre les problèmes dans un premier temps sans l'écriture avec style POO. Cependant, on demande alors une seconde écriture. Pourquoi ?
> * Le jour où on dispose d'une meilleure structure de données, il suffit de remplacer uniquement le bout de code de la classe, le problème restant intact. Sans POO, il faut souvent réécrire tout le problème pour utiliser les nouvelles idées... L'écriture avec le stye POO permet de s'affranchir presque totalement de la manière dont est écrit la classe. Il faut en revanche **toujours** garder à l'esprit : quel est le coût algorithmique de chaque méthode ?


>>> **Toujours utile** : relire [le tutoriel sur les structures de données sur python.org](https://docs.python.org/fr/3/tutorial/datastructures.html)


## La deque

En plus des structures [présentées ici](https://fr.wikipedia.org/wiki/Type_abstrait), il existe une autre structure linéaire assez utilisée.

* La `deque` : (*double end queue*), une structure qui permet facilement d'ajouter ou d'extraire facilement un élément à une des deux extrémités, si elle est non vide.


**Exercice 1** : En s'inspirant de la **première** implémentation de la pile, donner une implémentation d'une **deque** d'une certaine taille maximale. On proposera :
* le constructeur `Deque()`, ainsi que les méthodes,
* `.est_vide(self)`
* `.ajout_droite(self, élément)`
* `.ajout_gauche(self, élément)`
* `.extrait_droite(self)`
* `.extrait_gauche(self)`

**Exercice 2** : En utilisant une implémentation de la pile, donner une implémentation de la deque. On utilisera deux piles. Tout comme pour la file, critiquer la complexité des méthodes.