# [Alphabet](http://www.france-ioi.org/algo/task.php?idChapter=556&iOrder=15)

## Sujet

Écrivez un programme qui affiche tous les caractères de l'alphabet en majuscules, avec une espace entre chaque caractère.

On utilisera bien entendu une boucle !

### Exemple

---

entrée :

sortie :

```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```

## Solution

```python
def lettre_majuscule(indice: int) -> str:
    """
    Renvoie la lettre majuscule d'indice donné.
    
    >>> lettre_majuscule(0)
    'A'
    
    >>> lettre_majuscule(25)
    'Z'
    """
    return chr(ord('A') + indice)

print(" ".join(lettre_majuscule(i) for i in range(26)))
```

Même pour un problème facile, on essaie de produire un code propre et décomposé avec des fonctions qui incluent un *doctest* ; bonne pratique !
