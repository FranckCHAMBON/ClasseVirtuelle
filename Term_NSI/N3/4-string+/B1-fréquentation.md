# [Fréquentation de la bibliothèque](http://www.france-ioi.org/algo/task.php?idChapter=556&idTask=2458)

## Sujet

En ces périodes de restrictions budgétaires, il est important de disposer de statistiques détaillées sur la fréquentation de la bibliothèque, afin de justifier de son importance. Ainsi, et depuis plusieurs mois, les bibliothécaires se relaient afin de comptabiliser combien de personnes sont entrées à la bibliothèque à chaque heure de la journée.

À chaque ligne du registre correspond une journée, les entiers présents sur cette ligne représentant la fréquentation à chaque heure. Cela permet de faire des statistiques détaillées mais on aimerait savoir combien de personnes au total sont venues.

### Entrée

* Un nombre inconnu de lignes, chacune contenant un nombre inconnu d’entiers, ce nombre variant selon les lignes.

* Les entiers sont séparés entre eux par un seul espace et il n’y a pas d’espace en fin de ligne.

### Sortie

* Vous devez indiquer la somme de tous les entiers.

### Exemple

---

entrée :


```
5
2 2
4 4 4
6 6
3 3
```

sortie :

```
39
```

---

## Solution

### Manière propre, pythonesque

```python
def somme_lignes():
    total = 0
    while True:
        try:
            ligne = input()
        except EOFError:
            return total
        total += sum(map(int, ligne.split()))

print(somme_lignes())
```

### Manière fonctionnelle

```python
import sys
print(sum(sum(map(int, ligne.split()))  for ligne in sys.stdin))
```

### Commentaire
* La première méthode est à connaître pour reproduire la gestion des erreurs. Elle permet de s'arrêter (avec une modification), sur la première ligne ne contenant pas d'entier mais d'autres caractères.
* La seconde méthode est bien plus performante.
* **Astuce peu connue** : Utiliser `float` au lieu de `int` est encore plus performant, mais échouerait pour des entiers trop grands ; une somme sur plus de $51~\text{bits}$ serait arrondie et faussée.