# [Majuscules](http://www.france-ioi.org/algo/task.php?idChapter=566&idTask=438)



Écrivez un programme qui lit une ligne de texte au clavier et qui affiche le contenu de cette ligne en transformant en majuscules tous les caractères minuscules qu'elle contient, et en ré-affichant les autres caractères tels-quels.

## Contraintes

La ligne ne contient pas plus de 10 000 caractères.

Elle ne contient aucun caractère accentué.
### Exemple

entrée :

    Ceci est un texte sans accents, qui sert d'exemple.

sortie :

    CECI EST UN TEXTE SANS ACCENTS, QUI SERT D'EXEMPLE.

## Solution

```python
def majuscule(lettre: str) -> str:
    """Renvoie la version majuscule d'une lettre minuscule,
    Sinon renvoie le même caractère.
    >>> majuscule("a")
    A
    >>> majuscule("B")
    B
    >>> majuscule("!")
    !
    """
    if ord('a') <= ord(lettre) <= ord('z'):
        return chr(ord(lettre) - ord('a') + ord('A'))
    else:
        return lettre

for lettre in input():
    print(majuscule(lettre), end="")
print()
```

### Commentaires
* On pourrait remplacer les trois dernières lignes avec un style **plus fonctionnel** avec : `print("".join(map(majuscule, input())))`
    * `input()` désigne la ligne lue,
    * `map` va appliquer la fonction `majuscule` à chaque élément du second argument donné,
    * `join` va joindre tous ces morceaux en les séparant avec des `""`, donc les coller,
    * `print` affiche le tout.
* On peut avoir une version simple en une ligne, en effet Python inclut de nombreuses fonctions classiques.
    * La méthode `upper` convertit une chaîne de caractères en majuscules. Elle est appliquée ici à la chaîne lue par `input()`. Elle permet d'obtenir des majuscules pour de nombreux caractères accentués ou autres raretés comme `ŒÇÆ` pour `œçæ`, par exemple.
```python
print(input().upper())
```
