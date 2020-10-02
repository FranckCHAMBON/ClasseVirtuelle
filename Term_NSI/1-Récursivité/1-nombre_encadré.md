# [Nombre encadré](http://www.france-ioi.org/algo/task.php?idChapter=513&idTask=511)

Écrivez un programme qui lit deux entiers sur l'entrée, et qui affiche le premier entier, entouré d'autant de paires de crochets `[` et `]`, qu'indiqué par la valeur du deuxième nombre.

**Votre programme doit impérativement utiliser une fonction récursive, et non une boucle.**

## Contraintes

* $0 \leqslant E \leqslant 50$, où $E$ est le nombre de crochets à mettre de chaque côté.

## Exemples

### Exemple 1

entrée :

    42 3

sortie :

    [[[42]]]

### Exemple 2

entrée :

    24 0

sortie :

    24

---

## Solution

```python
def main():
    def nb_encadré(nombre: int, nb_crochets: int) -> str:
        """Renvoie 'nombre' entouré de paires de crochets.
        La sortie est de type str
        >>> exo(42, 3)
        [[[42]]]
        >>> exo(24, 0)
        24
        """
        if nb_crochets == 0:
            return str(nombre)
        else:
            return "[" + nb_encadré(nombre, nb_crochets - 1) + "]"
        

    nombre, nb_crochets = map(int, input().split())
    print(nb_encadré(nombre, nb_crochets))
main()
```

### Commentaires
* Le cœur de la fonction récursive est de construire un objet `str`, avec :
    * un crochet ouvrant, puis
    * le nombre encadré avec une profondeur inférieure de $1$, puis
    * le crochet fermant.
* Le cas de base étant de ne renvoyer que le nombre... avec le type `str` ! 
* On voit ici l'intérêt de déclarer les types, en particulier le type de sortie. L'oubli de `str` dans le `return` du cas de base `nb_crochets == 0` serait une faute importante. La concaténation (`+`) dans le cas général générerait une erreur.