# [Bâtiment et allée](http://www.france-ioi.org/algo/task.php?idChapter=566&idTask=2414)

En discutant avec un des bibliothécaires les plus anciens, vous apprenez une information capitale sur **LE** livre que vous cherchez au sein de la bibliothèque.

Pour savoir dans quel bâtiment il est, vous devez prendre la première lettre du nom de l’auteur et la convertir en un entier (A donne 1, B donne 2...).

Pour savoir dans quelle allée du bâtiment, on doit prendre l’âge de son fils aîné quand il a écrit le livre et le convertir en une lettre (1 donne A, 2 donne B....).

## Contraintes

Le nom de l’auteur comprend au plus 50 caractères.

### Entrée

Sur la première ligne, le nom de l’auteur, la première lettre étant une majuscule.

Sur la seconde ligne, l’âge de son fils aîné au moment où le livre a été écrit.

### Sortie

Le numéro du bâtiment et la lettre correspondant à l’allée, sur la même ligne sans espace entre les deux.

### Exemple

entrée :

    Dopelgon
    6

sortie :

    4F

## Solution

```python
auteur = input()
âge = int(input())

lettre1 = auteur[0]
numéro = ord(lettre1) - ord('A') + 1

allée = chr(âge + ord('A') - 1)

print(numéro, end = "")
print(allée)
```

### Commentaires
* On peut proposer une solution en une seule ligne, mais peu lisible, c'est mal :
```python
print(ord(input()[0]) - ord('A') + 1, chr(int(input()) + ord('A') - 1), sep = "")
```
> L'utilisation de `sep = ""` permet d'avoir une **sép**aration vide entre les deux objets affichés.
