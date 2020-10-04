# [Fréquences d’apparition](http://www.france-ioi.org/algo/task.php?idChapter=566&idTask=2419)

On a découvert de vieilles archives au sein de la bibliothèque, de nombreux manuscrits écrits dans diverses langues. On souhaite étudier plus en détail ces manuscrits mais comme tous les bibliothécaires ne parlent pas toutes ces langues, il faut d’abord déterminer la langue pour pouvoir choisir le bon bibliothécaire.

Pour déterminer la langue de manière automatique, un des bibliothécaires vous propose de déterminer la lettre la plus fréquente dans chaque texte, mais vous savez que cette technique n’est pas assez précise pour donner de bon résultats.

Vous décidez donc plutôt de regarder à quelles fréquences apparaissent chacune des lettres de l’alphabet.

## Contraintes

La ligne de texte contient moins de 10 000 caractères.

### Entrée

Une seule ligne de texte, ne contenant pas de lettres accentuées, mais pouvant contenir des signes de ponctuation ou des chiffres.

### Sortie

Pour chacune des lettres de l’alphabet, il faut afficher, sur une ligne, sa fréquence d’apparition dans le texte définie comme le nombre de fois où la lettre est présente, divisé par le nombre total de lettres du texte (et pas le nombre total de caractères).

### Exemple

entrée :

    Le francais est une langue romane, de la famille des langues indo-europeennes.

sortie :

    0.109375
    0.000000
    0.015625
    0.046875
    0.203125
    0.031250
    0.031250
    0.000000
    0.046875
    0.000000
    0.000000
    0.093750
    0.031250
    0.125000
    0.046875
    0.015625
    0.000000
    0.046875
    0.078125
    0.015625
    0.062500
    0.000000
    0.000000
    0.000000
    0.000000
    0.000000

## Solution

```python
def main():
    effectifs = [0] * 26
    ligne = input().lower()
    for lettre in ligne:
        if 'a' <= lettre <= 'z':
            effectifs[ord(lettre) - ord('a')] += 1
    effectif_total = sum(effectifs)
    for nb in effectifs:
        print(nb / effectif_total)
main()
```

### Commentaires

* On a stocké et construit les effectifs dans une liste de longueur 26, en supposant que toutes ou presque seraient utilisées. Dans le cas où on voudrait faire la même chose sur un ensemble **extrêmement grand**, où la plupart des éléments sont absents, on utilisera un dictionnaire, et les clés seront les éléments présents, et la valeur associées en sera l'effectif.
* On peut itérer directement sur les éléments d'une liste. Le code :
```python
for nb in effectifs:
    print(nb / effectif_total)
```

Remplace avantageusement :

```python
for i_effectif in range(len(effectifs)):
    print(effectifs[i_effectif] / effectif_total)
```
