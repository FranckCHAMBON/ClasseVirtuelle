# [Retournement de chaîne](http://www.france-ioi.org/algo/task.php?idChapter=513&idTask=513)


Écrivez un programme qui lit une ligne de texte sur l'entrée standard, et affiche cette ligne retournée, c'est-à-dire en commençant par le dernier caractère.

**Votre programme doit impérativement utiliser une fonction récursive, et non une boucle.**

## Contraintes
La ligne ne contient pas plus de 200 caractères.

### Exemple

entrée :

    bonjour

sortie :

    ruojnob


## Solution

```python
def retourne(chaîne: str) -> str:
    """Renvoie 'chaîne' retournée.
    >>> retourne("bonjour")
    ruojnob
    """
    if chaîne == "":
        return ""
    else:
        return retourne(chaîne[1:]) + chaîne[0]

chaîne = input()
print(retourne(chaîne))
```

### Commentaires
* Pour le cas de base, chaîne vide, on renvoie une chaîne vide.
* Pour le cas général, chaîne non vide, on renvoie
    * le premier caractère `chaîne[0]` à la fin,
    * et le reste `chaîne[1:]` au début, mais retourné par récursivité.