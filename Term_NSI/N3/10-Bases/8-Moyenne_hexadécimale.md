# [Moyenne hexadécimale](http://www.france-ioi.org/algo/task.php?idChapter=565&idTask=457)


Écrivez un programme qui lit des nombres en base hexadécimale fournis par l'utilisateur et qui affiche la partie entière de leur moyenne, également en base hexadécimale.

On rappelle que la base hexadécimale (base 16) est composée des chiffres de 0 à 9, puis des lettres de A à F (on se contentera ici de caractères majuscules).

## Contraintes

* `1 <= N <= 100`, où `N` est le nombre de valeurs hexadécimales dont l'utilisateur doit calculer la moyenne.
* `0 <= V <= 10000`, où `V` est la valeur décimale de l'un des nombres hexadécimaux lus.

### Entrée
La première ligne de l'entrée contient un nombre `N` exprimé en base hexadécimale : le nombre de valeurs dont il faut faire la moyenne.

Chacune des `N` lignes suivantes contient un entier, en base hexadécimale.

### Sortie
Vous devez afficher un entier sur la sortie, en base hexadécimale : la partie entière de la moyenne des nombres fournis en entrée.

Attention : le résultat peut comporter plusieurs chiffres.

### Exemple

entrée :

    C
    0
    2
    4
    6
    8
    A
    C
    E
    10
    12
    14
    16

sortie :

    B

## Solution

```python
def int16(chaîne: str) -> int:
    """Renvoie l'entier correspondant à 'chaîne' lu en hexadécimal.

    >>> hex("0")
    0

    >>> hex("A")
    10

    >>> hex("FF")
    255

    """
    n = 0
    for c in chaîne:
        n *= 16
        if "0" <= c <= "9":
            n += ord(c) - ord('0')
        else:
            n += ord(c) - ord('A') + 10
    return n

def hexadécimal(n: int) -> str:
    """Renvoie la représentation de n en hexadécimal.

    >>> hexadécimal(15)
    'F'

    >>> hexadécimal(256)
    '100'

    """
    if n == 0:
        return "0"
    chiffres = []
    while n > 0:
        chiffre = n % 16
        n = n // 16
        chiffres.append(chiffre)
    table = "0123456789ABCDEF"
    return "".join(table[chiffre] for chiffre in chiffres[::-1])


n = int16(input())
somme = sum(int16(input()) for _ in range(n))
print(hexadécimal(somme // n))
```

### Commentaires

* Pour la fonction `int16` :
    * On doit traiter séparément les cas chiffre et lettre.
    * On peut remplacer `n *= 16` par `n <<= 4` (décalage de 4bits à gauche).
    * On peut remplacer les deux `n += ...` par `n |= ...` (ou-bit-à-bit). (*Technique*)
    * Au lieu de créer la fonction `int16(chaîne)`, on pourrait utiliser `int(chaîne, 16)` ; la fonction *built-in* `int` de Python accepte un paramètre optionnel pour le choix de base... Ici, ce serait tricher...
* Pour la fonction `hexadécimal` :
    * Les deux premières instructions du `while` peuvent être remplacée par `n, chiffre = divmod(n, 16)`, mais aussi par `chiffre = n & 15`, suivi de `n >>= 4`, cette dernière méthode étant plus rapide ; ce sont des fonctions élémentaires pour le processeur.
    * L'utilisation de `table` est une astuce à retenir pour les situations où une fonction ne possède qu'une petite table de valeurs possibles sur un domaine de la forme $[\![0..N[\![$.
    