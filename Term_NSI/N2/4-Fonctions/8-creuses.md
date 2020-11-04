# Formes creuses

## Sujet

Écrivez un programme qui affiche une ligne de « X », un rectangle de « # », et un triangle de « @ ». Les deux formes doivent être creuses (remplies avec des espaces).

L'entrée comporte quatre entiers, un par ligne :

* le nombre de « X » de la ligne à afficher ;
* le nombre de lignes du rectangle de « # » ;
* le nombre de colonnes du rectangle ;
* le nombre de lignes du triangle de « @ ».

Vous devez afficher les trois formes successivement, avec une ligne blanche entre chaque forme, comme le montre l'exemple.

Votre objectif doit être d'obtenir le code source le plus simple et clair possible, en le décomposant en fonctions.

## Exemple

entrée :

    15
    5
    12
    6

sortie :

    XXXXXXXXXXXXXXX

    ############
    #          #
    #          #
    #          #
    ############

    @
    @@
    @ @
    @  @
    @   @
    @@@@@@

## Solution

On fabrique ici des fonctions qui renvoient du texte à afficher, et non des fonctions qui affichent directement le texte. C'est une meilleure pratique. On peut vouloir faire autre chose de ce texte plutôt que de l'afficher...

On utilise les possibilités de concaténation et multiplication avec les chaînes de caractères.

```python
def ligne(motif: str, longueur: int) -> str:
    """Renvoie une chaîne avec un motif répété.
    >>> ligne("X", 15)
    XXXXXXXXXXXXXXX
    """
    return motif * longueur

def rectangle(motif: str, hauteur: int, largeur: int) -> str:
    """Renvoie un rectangle creux entouré de motif.
    >>> rectangle("#", 5, 12)
    ############
    #          #
    #          #
    #          #
    ############
    """
    dessin = motif * largeur + "\n" # première ligne
    if hauteur > 1:
        if largeur > 1:
            dessin += (motif + " "*(largeur-2) + motif + "\n") * (hauteur - 2)
        else:
            dessin += (motif + "\n") * (hauteur - 2)
    dessin += motif * largeur # dernière ligne
    return dessin

def triangle(motif: str, côté: int) -> str:
    """Renvoie un triangle creux entouré de motif.
    >>> triangle("@", 6)
    @
    @@
    @ @
    @  @
    @   @
    @@@@@@
    """
    dessin = motif +"\n" # première ligne
    if côté > 1:
        for i in range(côté - 2):
            dessin += motif + " "*i + motif + "\n"
        dessin += motif * côté # dernière ligne
    return dessin

longueur = int(input())
print(ligne("X", longueur))

print()

hauteur = int(input())
largeur = int(input())
print(rectangle("#", hauteur, largeur))

print()

côté = int(input())
print(triangle("@", côté))
```

