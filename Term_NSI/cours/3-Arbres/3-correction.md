# Correction de certains exercices

## Constructions d'ABR
### Questions

Pour construire un ABR, on peut partir d'un ABR vide, et ajouter des nœuds en respectant la règle des ABR.

1. Montrer qu'en ajoutant successivement les nombres $[10, 7, 16, 2, 8, 12, 19]$ on retrouve l'ABR complet donné en exemple.
2. Trouver une autre liste permettant de construire le **même** ABR. Cette liste est une permutation de la première !
3. Trouver deux autres permutations de cette liste qui donnent trois ABR **différents**.
4. Quels sont les types d'ABR qui ne peuvent se construire qu'avec une unique liste ? 

### Réponses
1. RAS
2. On peut, par exemple, lire chaque niveau dans l'ordre que l'on veut, et obtenir le même ABR. Il y a d'autres solutions.
3. Il suffit de choisir une racine différente et de la placer en premier. Il y a bien d'autres solutions.
4. Les ABR peignes ne se construisent qu'avec une unique liste : la liste des éléments triés. Et réciproquement.

## Recherche dans un ABR
### Questions
> Pour chaque question, on demande quelques phrases claires. On se place comme une machine qui n'a pas la vision d'ensemble de l'ABR, mais qui a seulement l'accès à la racine (si elle existe), et à ses enfants de manière récursive...
1. Expliquer comment faire pour rechercher la présence d'un élément dans un ABR.
2. Pour un ABR donné, quel est le pire des cas pour le nombre d'étapes dans la recherche d'un élément.
3. Pour une taille donnée, quel est le pire type d'ABR qui peut donner le pire nombre d'étapes dans la recherche d'un élément.
4. Pour une taille donnée, quel est le meilleur type d'ABR qui permet de trouver un élément, dans le pire des cas, en le moins d'étapes.
5. Expliquer comment trouver l'élément minimal (resp. maximal) d'un ABR non vide.

### Réponses
1.  * Si l'ABR est vide, on renvoie absent (`False`).
    * Sinon, l'ABR est non vide, c'est un nœud.
        * Si l'élément cherché est égal à l'élément du nœud, on renvoie présent (`True`).
        * Si l'élément cherché est **inférieur** à l'élément du nœud, on fait une recherche, par récursivité, dans le sous arbre **gauche**.
        * Si l'élément cherché est **supérieur** à l'élément du nœud, on fait une recherche, par récursivité, dans le sous arbre **droite**.
2. Le pire des cas est la recherche d'un élément qui est égal (ou presque) à une feuille située à la profondeur maximale.
3. Pour une taille donnée, l'ABR peigne peut donner le pire nombre d'étapes pour une recherche ; chercher sa feuille, par exemple.
4. Un ABR équilibré est un arbre qui possède la plus petite hauteur à taille donnée, donc le moins d'étapes dans le pire des cas pour une recherche.
5.  * Si l'ABR est vide, on lève une exception, le minimum n'existe pas.
    * Sinon, l'ABR possède une racine qui est un nœud.
        * Si le sous arbre gauche est vide, on renvoie l'élément à la racine du nœud.
        * Sinon, par récursivité, on demande le minimum de ce sous-arbre gauche.
    * Pour le maximum, on travaille avec le sous-arbre droit.

## Suppression dans un ABR
### Questions
> La suppression dans un ABR n'est pas au programme en NSI. Cependant, on peut découvrir **pourquoi** !

1. Montrer, en utilisant un exemple précédent, que la suppression d'un nœud est un problème qui n'est pas trivial ; qu'il y a du travail à réaliser pour obtenir un ABR suite à la suppression d'un nœud.

2. Donner des exemples où la suppression d'un nœud est triviale ; il n'y a pas beaucoup de travail à effectuer.

3. **Hors programme** : Expliquer comment supprimer un nœud d'un ABR.

### Réponses
1. Supprimer l'élément à la racine n'est pas trivial ; il faut la remplacer par une autre et réagencer !
2. Supprimer une feuille est facile, il n'y rien à réagencer.
3. **Hors programme.** Pour supprimer un élément dans un ABR (où les éléments sont distincts) il suffit de le remplacer par le plus petit élément du sous-arbre droit, ou bien par le plus grand élément du sous-arbre gauche. **Attention**, c'est plus technique si l'ABR possède des éléments en double.

## Étude de la complexité
### Questions
## Étude de la complexité
On suppose que l'ABR est de taille $n$, et de hauteur $h$.
1. Quelle est la complexité, en fonction de $h$, pour la recherche, l'ajout (ou la suppression) d'un élément ?
2. Si l'arbre est équilibré (ou presque), quelle est la complexité en fonction de $n$ ?
3. Si l'arbre est un peigne (ou presque), quelle est la complexité en fonction de $n$ ?

### Réponses
1. La complexité est en $\mathcal O(h)$ dans chaque cas.
2. Si l'arbre est non vide et équilibré (ou presque), on a $2^{h-1} \leqslant n < 2^h - 1$. (Avec la définition de la hauteur de l'arbre vide à zéro). Et $h \approx \log(n)$, de sorte que la complexité est alors en $\mathcal O(\log(n))$. On rappelle que $\log(n)$ est environ le nombre de chiffre de l'écriture de $n$, quelle que soit la base, à un facteur multiplicatif près.
3. Si l'arbre est un peigne, on a $n = h$, et donc la complexité est $\mathcal O(n)$.

> **Conclusion** : Dans le pire des cas (peigne ou presque) la complexité est en $\mathcal O(n)$, mais si on se débrouille à conserver un ABR presque équilibré, alors la complexité est en $\mathcal O(\log(n))$.

> Les méthodes que nous avons vues ne garantissent pas de conserver un arbre équilibré (ou presque). Les solutions étudiées post BAC seront les arbres AVL ou encore les arbres rouges et noirs.

## Nombre d'occurrences
### Questions
On suppose qu'on a un ABR où un élément peut être présent plusieurs fois, et que donc les inégalités dans la définition se comprennent au sens large.
1. Donner une méthode efficace `.nb_occurrences(self, élément)` qui renvoie le nombre d'occurrences de `élément` dans l'ABR `self`. Cette méthode ne doit rien pré-supposer sur la méthode de construction de l'ABR, mais uniquement qu'il respecte les règles.

### Réponses
1. Code Python
```python
    def nb_occurences(self, élément):
        if self.racine is None:
            return 0
        if self.racine < élément:
            return  self.racine.droite.nb_occurences(élément)
        if self.racine > élément:
            return  self.racine.gauche.nb_occurences(élément)
        #On a : self.racine == élément:
        return  1 + \
                self.racine.gauche.nb_occurences(élément) + \
                self.racine.droite.nb_occurences(élément)
```


## Méthode vers liste triée
### Question
1. Écrire une méthode de la classe `ABR` qui renvoie la liste de ses éléments dans l'ordre croissant.
2. Un tri de liste peut être réalisé en construisant un ABR à partir d'une liste non triée, puis en utilisant la question 1, et obtenir la liste triée. Quelle est l'efficacité (temps et mémoire) de ce tri ?

### Réponses
1. Voir le code ci-dessous.
2.  * Si l'ABR obtenu est équilibré ou presque, alors la complexité de ce tri est en $\mathcal O(n\log(n))$, et on ne peut pas faire mieux. **Hors programme.** En effet, même si les premières étapes sont rapides, les $n/2$ dernières coûtent chacune au moins $\log(n/2)$ et (*maths*) $\log(n/2) = \log(n) - \log(2)$, pour la complexité on peut négliger la constante $\log(2)$ devant $\log(n)$ qui tend vers l'infini. On a donc un coût pour les $n/2$ dernières étapes d'environ $n/2 \times \log(n)$, et on se moque du facteur multiplicatif $1/2$ qui donne une complexité en $\mathcal O(n\log(n))$.
    * Si l'arbre est plutôt peigne ou presque, la complexité est en $\mathcal O(n^2)$, et c'est celle d'un tri classique (à bulle, ou par insertion).

```python
def vers_liste(self):
    # cela correspond à un parcours infixe
    if self.racine is None:
        return []
    return  self.racine.gauche.vers_liste() +\
            [self.racine.élément] +\
            self.racine.droite.vers_liste()
            # ici, on a concaténé trois listes.
```

