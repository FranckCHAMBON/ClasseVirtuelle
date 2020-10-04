# [Lettre la plus fréquente](http://www.france-ioi.org/algo/task.php?idChapter=566&idTask=467)


On a découvert de vieilles archives au sein de la bibliothèque, de très nombreux manuscrits écrits dans diverses langues. On souhaite étudier plus en détails ces manuscrits mais comme tous les bibliothécaires ne parlent pas toutes ces langues, il faut d’abord déterminer la langue puis choisir le bon bibliothécaire.

Pour déterminer la langue de manière automatique, un des bibliothécaires propose de déterminer la lettre la plus fréquente dans chaque texte. Son hypothèse est que cette lettre sera différente selon les langues.

## Contraintes

La ligne de texte contient moins de 10 000 caractères.

### Entrée

Une seule ligne de texte, composée uniquement de lettres minuscules ou majuscules non accentuées, et d'espaces.

On vous garantit que dans tous les tests, une seule lettre est la plus utilisée, il n'y a pas d'ex-æquo.

### Sortie

Vous devez afficher une ligne sur la sortie, contenant la lettre de l'alphabet la plus présente dans le texte fourni en entrée.

Pour chaque lettre, vous devez compter à la fois ses apparitions en majuscule et en minuscule, mais afficher le résultat en majuscules. Vous devez ignorer les espaces.

### Exemples

#### Exemple 1

entrée :

    Le francais est une langue romane de la famille des langues indo europeennes

sortie :

    E

#### Exemple 2

entrée :

    A lingua portuguesa tambem designada portugues e uma lingua romanica flexiva originada no galego portugues falado no Reino da Galiza e no Norte de Portugal

sortie :

    A

## Solution

```python
def main():
    fréquence = [0] * 26
    for lettre in input():
        if 'a' <= lettre <= 'z':
            fréquence[ord(lettre) - ord('a')] += 1
        if 'A' <= lettre <= 'Z':
            fréquence[ord(lettre) - ord('A')] += 1

    fréquence_max = 0
    for i in range(26):
        if fréquence[i] > fréquence_max:
            fréquence_max = fréquence[i]
            majoritaire = i

    print(chr(ord('A') + majoritaire))
main()
```

### Commentaires
* On a placé la totalité du code dans une fonction `main`, c'est une bonne pratique, c'est obligatoire avec certains langages.
* On a utilisé la comparaison avec l'ordre lexicographique, et Python propose même la double comparaison en même temps, pour tester un encadrement.
