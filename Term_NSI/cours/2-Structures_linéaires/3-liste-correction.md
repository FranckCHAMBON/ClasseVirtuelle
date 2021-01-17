# Correction de certains exercices {ignore = true}

## Sommaire {ignore = true}
[TOC]

## La liste chaînée, bien pour une pile

@import "liste1.py"

### Complexité

On pose $n$ la longueur de la chaîne. La complexité des méthodes est la suivante :
* `ajout_gauche` : $\mathcal O(1)$ ; il suffit de modifier un maillon, et d'en ajouter un. Coût constant.
* `extrait_gauche` : $\mathcal O(1)$ ; il suffit de modifier un maillon. Coût constant.
* En revanche pour lire ou écrire à droite, il faut parcourir toute la chaîne pour accéder à l'autre bout. Ce parcours a un coût linéaire en $n$.
* `ajout_droite` : $\mathcal O(n)$ ; il suffit de modifier un maillon, et d'en ajouter un ; mais avant cela, il faut parcourir la liste entièrement.
* `extrait_droite` : $\mathcal O(n)$.

### Première conclusion
Si on a besoin uniquement d'une structure de pile, alors la liste chaînée est parfaitement adaptée. De plus il n'y pas de limite fixée à l'avance pour la taille de la pile. Cela fournit donc une implémentation légèrement plus lente mais bien plus flexible qu'avec un tableau. C'est aussi un peu plus technique à écrire...


Pour bénéficier d'une structure de file (ou de deque, c'est presque le même coût intellectuel), on va utiliser des listes qui mémorisent le maillon gauche et droite, (et/ou des maillons qui pointent à droite et à gauche).

## La liste doublement chaînée, pour une file

On peut avoir une file en conservant correctement le maillon gauche et le maillon droite de la liste.

@import "file.py"

### Complexité

On pose $n$ la longueur de la chaîne. La complexité des méthodes est la suivante :
* `ajout_gauche` : $\mathcal O(1)$ ; il suffit de modifier un maillon, et d'en ajouter un. Coût constant.
* `extrait_droite` : $\mathcal O(1)$ ; il suffit de modifier un maillon. Coût constant.

### Conclusion
Si on a besoin de construire une classe file cette liste doublement chaînée est idéale.

## La liste doublement chaînée, pour une deque

On utilise des maillons qui pointent dans les deux sens.

@import "liste2.py"

### Illustration des méthodes

#### `ajout_gauche`

##### Cas 1, si la liste est vide
Si la liste est vide, on crée un maillon qui sera le maillon gauche et aussi droite de la liste, il ne pointe nulle part, ni à droite, ni à gauche.

Exemple où on ajoute un premier maillon avec l'élément $42$.

$$\text{Nil} \leftarrow \boxed{\text{vers le vide} ; 42 ; \text{vers le vide}} \rightarrow \text{Nil}$$

##### Cas 2, si la liste est non vide

Si la liste est non vide, alors :
* On crée un nouveau maillon, et ce maillon sera le nouveau maillon gauche de la liste.
* À sa droite se trouvera l'ancien maillon gauche de la liste.
* Cet ancien maillon gauche pointait avant à gauche sur le vide, désormais il pointera sur le nouveau maillon.

Exemple où le maillon gauche possède l'attribut élément à $42$. On ajoute à gauche un maillon avec $1337$.

* Avant :
$$\text{Nil} \leftarrow m_1: \boxed{\text{vers le vide} ; 42 ; \text{vers la suite}} \rightarrow ...$$
    * On crée le maillon $m_0$ :
        * qui pointe à gauche sur le vide,
        * avec l'élément $1337$,
        * qui pointe à droite sur $m_1$.
    * On modifie $m_1$, il pointera désormais à gauche vers $m_0$.
* Après :
$$\text{Nil} \leftarrow m_0: \boxed{\text{vers le vide} ; 1337 ; \text{vers }m_1} \leftrightarrow m_1: \boxed{\text{vers }m_0 ; 42 ; \text{vers la suite}} \rightarrow ...$$

#### `extrait_gauche`
##### Cas 1, la liste est vide
On ne peut pas extraire, on lève une exception.

##### Cas 2, la liste ne contient qu'un élément
Dans ce cas, le maillon de gauche existe mais il pointe à sa droite sur le vide. En supprimant un maillon, la liste devient vide.

##### Cas 3, la liste contient plusieurs éléments
Dans ce cas, le maillon de gauche existe et il pointe à sa droite sur un autre maillon ; ce maillon sera le nouveau maillon gauche.

Exemple où le maillon gauche possède l'attribut élément à $1337$, et pointe vers un maillon avec $42$.


* Avant :
$$\text{Nil} \leftarrow m_0: \boxed{\text{vers le vide} ; 1337 ; \text{vers }m_1} \leftrightarrow m_1: \boxed{\text{vers }m_0 ; 42 ; \text{vers la suite}} \rightarrow ...$$
    * On enregistre la valeur $1337$, pour la renvoyer à la fin.
    * On établit que le maillon gauche de la liste est celui à droite de l'ancien maillon gauche. Ici, $m_1$ devient le maillon gauche de la liste.
    * On modifie $m_1$ afin qu'il pointe désormais à gauche sur le vide.
    * On renvoie $1337$.
* Après :
$$\text{Nil} \leftarrow m_1: \boxed{\text{vers le vide} ; 42 ; \text{vers la suite}} \rightarrow ...$$

### Complexité

On pose $n$ la longueur de la chaîne. La complexité des méthodes est la suivante :
* `ajout_gauche` : $\mathcal O(1)$ ; il suffit de modifier un maillon, et d'en ajouter un. Coût constant.
* `extrait_gauche` : $\mathcal O(1)$ ; il suffit de modifier un maillon. Coût constant.
* `ajout_droite` : $\mathcal O(1)$ ; il suffit de modifier un maillon, et d'en ajouter un. Coût constant.
* `extrait_droite` : $\mathcal O(1)$ ; il suffit de modifier un maillon. Coût constant.

### Conclusion
Si on a besoin de construire une classe file ou une deque, la liste doublement chaînée est idéale. On rappelle que cette construction est utile pour les langages qui ne fournissent pas ces structures naturellement. **Cette construction est aussi pédagogique.**
> Avec Python, en dehors de l'aspect pédagogique, on utilisera la deque fournie dans `collections`.

Donnons maintenant une motivation à vouloir créer de nouvelles structures de données toujours plus efficaces.
* On aimerait pouvoir insérer ou supprimer ailleurs qu'aux extrémités.
* On devine qu'avec les maillons, il est facile d'insérer une valeur au milieu d'une liste, il suffira de modifier quelques liens droite et gauche de certains maillons.
* En revanche, pour chercher un élément, il faut parcourir la liste, et dans le pire des cas, **toute la liste**.

On aimerait une structure de donnée, où :
* La recherche d'un élément est aussi rapide que possible.
* L'insertion d'un élément est aussi rapide que possible.
* La suppression d'un élément est aussi rapide que possible.

> Les **a**rbres **b**inaires de **r**echerches (ABR) seront une réponse à cette question.