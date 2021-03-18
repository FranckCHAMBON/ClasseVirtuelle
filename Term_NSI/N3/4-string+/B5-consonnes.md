# [Consonnes](http://www.france-ioi.org/algo/task.php?idChapter=556&iOrder=16)

## Sujet



Écrivez un programme qui affiche dans l'ordre alphabétique toutes les consonnes de l'alphabet en minuscules, en les séparant par des espaces.

On utilisera bien entendu une boucle !

## Solution

```python
def lettre_minuscule(indice: int) -> str:
    """
    Renvoie la lettre minuscule d'indice donné.
    
    >>> lettre_minuscule(0)
    'a'
    
    >>> lettre_minuscule(25)
    'z'
    
    """
    return chr(ord('a') + indice)

CONST_voyelles = "aeiouy"
alphabet = iter(lettre_minuscule(i) for i in range(26))
consonnes = [lettre for lettre in alphabet if lettre not in CONST_voyelles]
print(" ".join(consonnes))
```

### Commentaire

On a construit ici `alphabet` comme un itérateur et non une liste, on s'en sert qu'une fois ensuite, donc l'itérateur est un bon choix.

