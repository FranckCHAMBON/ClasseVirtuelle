# [Fléchettes](http://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2209)



Au cours de votre périple, vous rencontrez un groupe d'amateurs de fléchettes. Ces joueurs sont de grands passionnés et aiment jouer sur des cibles de tailles variées. Cependant, leurs cibles se font vieilles et mériteraient bien d'être changées ! Vous profitez donc de votre passage parmi eux pour leur imprimer de nouvelles cibles.

Les cibles à imprimer sont de la forme suivante (ici avec 4 lettres) :

    aaaaaaa
    abbbbba
    abcccba
    abcdcba
    abcccba
    abbbbba
    aaaaaaa

## Ce que doit faire votre programme :

Votre programme doit lire un unique entier : le nombre de lettres `nbLettres` (`1 <= nbLettres <= 26`) à utiliser. Il doit ensuite afficher la cible correspondante (comme indiqué sur la figure ci-dessus).

## Solution

```python
nb_lettres = int(input())
dernière_pos = 2 * (nb_lettres - 1)

def lettre(i, j):
    """renvoie la lettre à placer à la position (i, j)"""
    # on utilise 3 symétries
    if i >= nb_lettres:
        i = dernière_pos - i
        #   axe horizontal
    if j >= nb_lettres:
        j = dernière_pos - j
        #   axe vertical
    k = min(i, j)
    #   axe diagonal
    return chr(k + ord('a'))

for i in range(dernière_pos + 1):
    print("".join([lettre(i, j) for j in range(dernière_pos + 1)]))
```

### Commentaires

* On crée une fonction pour obtenir la lettre pour chaque position (i, j).
    * Les positions vont de `0` à `dernière_pos = 2 * (nb_lettres - 1)` inclus.
    * On utilise trois axes de symétrie.
* Pour finir, on affiche chaque ligne à la suite,
    * chaque ligne est obtenue en joignant la liste des lettres de la ligne.