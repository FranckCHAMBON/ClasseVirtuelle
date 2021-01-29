# Correction de certains exercices


## Exercice 7 - Parcours en largeur

```python
# On suppose que l'on dispose d'une classe File
# avec les méthodes enfile et défile.

def parcours_largeur(arbre):
    nœuds = File()
    nœuds.enfile(arbre)
    while not nœuds.est_vide():
        nœud = nœuds.défile()
        if nœud is not None:
            print(nœud.élément)
            nœuds.enfile(nœud.gauche)
            nœuds.enfile(nœud.droite)

def parcours_largeur(arbre):
    # Avec les niveaux
    nœuds = File()
    nœuds.enfile((arbre, 0))
    while not nœuds.est_vide():
        nœud, niveau = nœuds.défile()
        if nœud is not None:
            print(nœud.élément, niveau)
            nœuds.enfile((nœud.gauche, niveau + 1))
            nœuds.enfile((nœud.droite, niveau + 1))
```

## Exercice 8 - Reconstruire un arbre
> Un arbre binaire est étiqueté avec des lettres.
>* Un parcours préfixe donne un affichage `ALORHGIMET`.
>* Un parcours infixe donne un affichage `OLHRAMIEGT`.

1. Le parcours préfixe commence par un `A`, donc la racine est étiquetée `A`. Il n'y a qu'un seul `A`, on déduit alors aussi que :
    * Le sous-arbre gauche est composé des étiquettes `OLHR` en infixe, et donc `LORH` en préfixe.
    * Le sous-arbre droite est composé des étiquettes `MIEGT` en infixe, et donc `GIMET` en préfixe.
2. La racine du sous arbre gauche est donc `L`, et `G` à droite.
    * Sous-arbre gauche :
        * Son sous-arbre gauche : `O` en préfixe comme en infixe.
        * Son sous-arbre droite : `RH` en préfixe et `HR` en infixe.
    * Sous-arbre droite :
        * Son sous-arbre gauche : `IME` en préfixe et `MIE` en infixe.
        * Son sous-arbre droite : `T` en préfixe comme en infixe.
3. On déduit ensuite que le parcours en largeur est `ALGORITHME`.

