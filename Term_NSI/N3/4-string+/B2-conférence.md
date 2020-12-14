# [Conférence et tics de langage](http://www.france-ioi.org/algo/task.php?idChapter=556&iOrder=12)

## Sujet

Aujourd’hui, comme tous les mois, un célèbre écrivain donne une conférence sur son œuvre. Guère captivé par ce qu’il explique, vous remarquez rapidement qu’il a un certain nombre de tics de langage, en particulier il utilise souvent les mêmes mots, comme “heu”, “je”...

Pour vous occuper, vous décidez de compter combien de fois certains mots sont utilisés dans son discours.

### Contraintes

* Le texte du discours contient au plus $10\,000$ caractères.

Chacun des mots est au plus de longueur $50$.

### Entrée

* Sur la première ligne, un mot. Sur la seconde ligne, le texte du discours.

* Il n’y a pas de ponctuation, les mots et le texte sont uniquement constitués de lettres non accentuées et d’espaces. Par « mot », on entend, comme d’habitude, une suite de caractères ne contenant pas d’espace.

### Sortie

* Vous devez indiquer combien de fois le mot donné est présent dans le texte du discours.

* Quelle que soit la casse du mot qu’on vous donne ou de ses apparitions dans le texte, vous devez toutes les compter !

### Exemple

---

entrée :

```
heu
Je pense heu que heu ce livre est heu le meilleur que j ai ecrit heu depuis heu cinq ans Heu vous avez des questions
```

sortie :

```
6
```

---

## Solution

```python
tic = input().upper()
print(sum(1 for mot in input().upper().split() if mot == tic))
```

Le style est ici fonctionnel.
