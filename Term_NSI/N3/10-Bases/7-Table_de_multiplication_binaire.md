# [Table de multiplication binaire](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=456)

Vous devez écrire un programme qui affiche une table de multiplication, mais dont tous les nombres sont affichés en base binaire.

## Contraintes

* `1 <= T <= 15`, où `T` est le nombre de lignes et de colonnes de la table.

### Entrée
Vous devez lire un entier `T` sur l'entrée : le nombre de lignes (et de colonnes) de la table.

### Sortie
Vous devez afficher `T` lignes sur la sortie, contenant chacune `T` entiers binaires, séparés par des caractères de tabulation ('\t'). Le jème nombre de la ième ligne doit contenir la valeur binaire de i * j.

### Exemple

entrée :

    5

sortie :

    1	10	11	100	101
    10	100	110	1000	1010
    11	110	1001	1100	1111
    100	1000	1100	10000	10100
    101	1010	1111	10100	11001

## Solution

```python
def binaire(n: int) -> str:
    "Renvoie n écrit en binaire."
    return bin(n)[2:]

n = int(input())
for i in range(1, n+1):
    print("\t".join(binaire(i*j) for j in range(1, n+1)))
```

### Commentaires

* On écrit chaque ligne comme étant un collage avec la tabulation `"\t"` comme séparateur.