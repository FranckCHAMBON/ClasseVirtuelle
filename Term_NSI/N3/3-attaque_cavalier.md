# [Attaque du cavalier](http://www.france-ioi.org/algo/task.php?idChapter=564&iOrder=3)


Vous devez écrire un programme qui détermine dans une partie d'échecs, si un cavalier peut prendre une pièce de l'adversaire.

Rappelons que les échecs se jouent sur un plateau carré de 8 cases par 8. Un cavalier se déplace en avançant d'une case horizontalement ou verticalement, puis en allant en diagonale, sans revenir en arrière. Le cavalier peut se déplacer même si la case intermédiaire de son déplacement contient une pièce (amie ou ennemie). La figure suivante montre toutes les possibilités de déplacements de deux cavaliers :

![attaque cavalier](attaque_cavalier.gif)

## Entrée
On vous donne la description d'un plateau de jeu sous la forme de 8 lignes de 8 caractères. Les lettres majuscules représentent les pièces blanches, les minuscules les pièces noires, et les `.` représentent les cases vides. Les cavaliers sont représentés par la lettre `c` (ou `C`), et les autres pièces par d'autres lettres de l'alphabet.

## Sortie
Votre programme doit afficher `yes` si l'un des cavaliers blancs peut se déplacer vers une case contenant une pièce noire (donc la prendre) et `no` dans le cas contraire.

## Exemple

---

entrée :

```
tc.drf.t
ppp.pppp
...p...c
.....f..
..C..P..
..P.D.P.
PP.....P
T.F.RFCT
```

sortie :

```
yes
```

---

## Commentaires
Dans cet exemple, le cavalier blanc situé vers le centre peut prendre le pion noir (`p`) situé deux cases au-dessus, et une case à droite.

Remarque : on considère le roi noir comme n'importe-autre quelle pièce, même si dans les règles des échecs, on ne peut pas "prendre" le roi.

## Solution

```python
N = 8

def est_cavalier_blanc(case):
    return case == 'C'

def est_case_non_vide(case):
    return case != '.'

# les mouvements du cavalier
vecteurs = \
 [(1, 2), (2,1), (-1,2), (-2,1), (1,-2), (2,-1), (-1,-2), (-2,-1)]

# variante
vecteurs = [(1,2), (2, 1)]
vecteurs.extend([(-di, dj) for (di, dj) in vecteurs])
vecteurs.extend([(di, -dj) for (di, dj) in vecteurs])
assert len(vecteurs) == 8

def est_valide(i, j):
    return (0 <= i < N) and (0 <= j < N)

def est_noire(pièce):
    return 'a' <= pièce <= 'z'

def attaque_cavalier_blanc(échiquier):
    for i in range(N):
        for j in range(N):
            if est_cavalier_blanc(échiquier[i][j]):
                for di, dj in vecteurs:
                    idi, jdj = i + di, j + dj
                    if est_valide(idi, jdj):
                        menacée = échiquier[idi][jdj]
                        if est_case_non_vide(menacée):
                            if est_noire(menacée):
                                return True
    return False

# Lecture
échiquier = [input() for _ in range(N)]

# Écriture
print('yes' if attaque_cavalier_blanc(échiquier) else 'no')
```

### Commentaires
* On a utilisé de nombreuses fonctions, mêmes courtes ; remarquer comme elles explicitent le code. Reprenez cet exemple.
* Avec un style POO, on aurait écrit :
    + `if menacée.est_case_non_vide():` c'est mieux !
    + `if menacée.est_noire():` c'est mieux aussi !!
    + `if échiquier[i][j].est_cavalier_blanc():` l'ordre est plus logique. Pour des programmes complexes, la POO apporte un code bien plus compréhensible. Il sera plus verbeux, c'est vrai aussi.
