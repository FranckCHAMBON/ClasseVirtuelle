# [Hydroélectricité](http://www.france-ioi.org/algo/task.php?idChapter=527&idTask=921)

## Énoncé

Vous souhaitez produire de l'énergie renouvelable en exploitant la force du courant d'une rivière. Un barrage n'est cependant pas la bonne solution, du fait de son impact sur l'environnement (le fait d'inonder toute une zone, de gêner le déplacement des poissons, etc). Vous décidez donc d'installer un système de turbines au fil de l'eau, qui exploitent la force du courant sans bloquer la rivière.

On vous décrit la force du courant mètre par mètre sur toute la longueur des $N$ mètres de la rivière. Vous souhaitez placer des turbines au sein d'une centrale couvrant une zone de $K$ mètres le long de la rivière. Écrivez un programme qui détermine à quel endroit placer cette zone pour que la somme des forces du courant au sein de cette zone soit la plus grande possible.

### Contraintes

* $1 \leqslant N \leqslant 100\,000$, où $N$ est la longueur de la rivière, en mètres.
* $1 \leqslant K \leqslant N$, où $K$ est la longueur de votre centrale hydroélectrique.
* $0 \leqslant C \leqslant 1000$, où $C$ est la force du courant à un endroit donné de la rivière. 

### Entrée

* Sur la première ligne, deux entiers séparés par un espace : $K$ puis $N$.
* La seconde ligne contient $N$ entiers séparés par des espaces : la force du courant le long de chacun des $N$ mètres de la longueur de la rivière.

### Sortie

Affichez un entier : la plus grande somme possible des forces de courant qu'il est possible d'accumuler sur une longueur de $K$ mètres consécutifs de la rivière.

### Exemple

---

entrée :

    3 9
    3 2 5 7 4 2 3 8 4

sortie :

    16

---

## Solution alternative

### Méthode naïve en $\mathcal O(N^2)$
Pour chaque indice avec $i < N - K$, on regarde la somme des forces du courant sur l'intervalle $[\![i ... i + K[\![$

### Méthode efficace en $\mathcal O(N)$

On calcule d'abord un tableau qui donne le cumul des forces du début jusqu'à tout indice $i < N$. Ce tableau se construit en temps linéaire.

Pour connaître la force d'une tranche, il suffit de faire une soustraction. Tester toutes les tranches se fait en temps linéaire.

```python
k, n = map(int, input().split())
cumul = [0]
ajout = cumul.append # <= très bon réflexe ; performance

force_cumulée = 0
for force in map(int, input().split()):
    force_cumulée += force
    ajout(force_cumulée)

tranche_forte = max(cumul[i + k] - cumul[i]
                        for i in range(n - k + 1))

print(tranche_forte)
```

> Il est parfois utile d'utiliser ce genre de technique, **et pas nécessairement avec l'addition**, de faire un cumul des valeurs d'un tableau.
