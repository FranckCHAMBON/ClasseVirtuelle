# [Lecture binaire](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=442)


Écrire un programme qui lit un nombre positif ou nul en base binaire et qui affiche sa valeur en base 10.

Votre programme doit lire les caractères du nombre un par un, car il peut y avoir jusqu'à 26 chiffres binaires.

### Exemple

entrée :

    101111

sortie :

    47

## Solution

```python
def main():
    binaire = input()
    n = 0
    for bit in binaire:
        n <<= 1
        if bit == '1':
            n += 1
    print(n)
main()
```

### Commentaire

* `binaire` est ici une chaîne de caractères, donc on fait bien un test `bit == '1'` où le `'1'` est bien lui aussi une chaîne de caractères.
* On a proposé une solution où on lit l'entrée de gauche à droite ; voici ci-dessous une solution où on lit l'entrée de droite à gauche.

```python
def main():
    binaire = input()
    n = 0
    puissance = 1
    for bit in binaire[::-1]:
        if bit == '1':
            n += puissance
        puissance <<= 1
    print(n)
main()
```

* Il existe une fonction déjà incluse en Python pour lire du binaire. Il s'agit de la fonction `int`, avec l'argument optionnel `2`, pour signifier que le premier paramètre est en base 2.

```python
binaire = input()
n = int(binaire, 2)
```
