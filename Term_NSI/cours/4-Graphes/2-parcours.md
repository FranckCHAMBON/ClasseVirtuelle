# Parcours

On rappelle d'abord comment parcourir un arbre (qui est un graphe connexe, et sans cycle)

## Parcours d'arbre

On utilise `print`, mais celà pourrait être n'importe quelle action lors du parcours.

```python
class Arbre:
    def __init__(self, racine, enfants):
        self.racine = racine
        self.enfants = enfants
    

def parcours(arbre):
    """Parcours récursif d'un arbre, (parcours en profondeur).
    """
    print(arbre.racine)
    for enfant in arbre.enfants:
        parcours(enfant)


def parcours(arbre):
    """Parcours itératif d'un arbre en profondeur.
    On utilise une pile.
    """
    pile = Pile()
    pile.empile(arbre)
    while not pile.est_vide():
        noeud = pile.dépile()
        print(noeud.racine)
        for enfant in noeud.enfants:
            pile.empile(enfant)

    
def parcours(arbre):
    """Parcours itératif d'un arbre en largeur.
    On utilise une file, et un code similaire !!!
    """
    pile = File()
    pile.enfile(arbre)
    while not file.est_vide():
        noeud = pile.défile()
        print(noeud.racine)
        for enfant in noeud.enfants:
            pile.enfile(enfant)
```

**Exercice** : Vérifier sur un arbre écrit à la main que les parcours proposés sont bons.

## Parcours de graphe

**Exercice** :
1. Quels problèmes avons-nous à appliquer ces parcours sur des graphes ?
    * **Réponse** : le parcours peut entrer dans un cycle, et il ne parcourt que la composante connexe !
2. Comment éviter de rentrer dans un cycle ?
    * **Réponse** : on va stocker dans une structure de données, des booléens pour indiquer si un sommet a déjà (ou va bientôt) être visité. On pourra alors faire un test avant de l'enfiler ou de l'empiler.


```python
# Exemple de graphe d'ordre n, où
# les sommets sont numérotés de 0 inclus à n exclu. 

def parcours(sommet_départ):
    """Parcours itératif d'un graphe,
    parcours en profondeur, en partant de 'sommet',
    uniquement de sa composante connexe.
    """
    visité = [False for _ in range(n)]
    pile = Pile()
    pile.empile(sommet_départ)
    visité[sommet_départ] = True
    while not pile.est_vide():
        sommet = pile.dépile()
        print(sommet) # ou autre action
        for enfant in sommet.enfants:
            if visité[enfant] == False:
                visité[enfant] = True
                pile.empile(enfant)
```

**Exercice** :
1. Obtenir le parcours en largeur d'un graphe.
2. Obtenir la distance du sommet le plus éloigné de `sommet_départ`.
3. Obtenir la distance la plus courte entre `sommet_départ` et `sommet_destination`.
