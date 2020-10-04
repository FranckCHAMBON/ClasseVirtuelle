# [Titres palindromiques](http://www.france-ioi.org/algo/task.php?idChapter=566&idTask=2417)


En étudiant un vieux parchemin, on apprend que le livre qui nous intéresse dans la bibliothèque a un titre qui est un palindrome : il peut se lire de gauche à droite ou de droite à gauche (sans s’occuper des espaces).

Vous devez analyser les titres de tous les livres de la bibliothèque et sélectionner ceux qui sont des palindromes.

## Contraintes

Chaque titre de livre est au plus de longueur 100.

### Entrée

La première ligne contient un entier `nbLivres`, le nombre total de livres.

Chacun des `nbLivres` lignes suivantes contient un titre de livre.

Les titres sont composés d’espaces et de lettres majuscules ou minuscules, non accentuées.

### Sortie

Vous devez afficher chaque titre de livre qui est un palindrome.

Pour déterminer si un titre est un palindrome, on ne considérera ni les espaces, ni la casse (majuscule ou minuscule) des lettres.

### Exemple

entrée :

    3
    Lieur a Rueil
    Le chevalier delibere
    Un roc si biscornu

sortie :

    Lieur a Rueil
    Un roc si biscornu

## Solution

```python
def est_palindrome(titre: str) -> bool:
    """Renvoie un booléen,
    True si 'titre' est un palindrome.
    La casse ne compte pas.
    >>> est_palindrome("Laval")
    True
    >>> est_palindrome("ABc")
    False
    """
    ligne = titre.lower() # en minuscule
    début = 0
    fin = len(ligne) - 1
    while début < fin:
        if ligne[début] == ' ':
            début += 1
        elif ligne[fin] == ' ':
            fin -= 1
        else:
            if ligne[début] != ligne[fin]:
                return False
            else:
                début += 1
                fin -= 1
    return True

nb_livres = int(input())
for i_livre in range(nb_livres):
    titre = input()
    if est_palindrome(titre):
        print(titre)
```

### Commentaires

* On place deux variables d'indice, `début` et `fin`, que l'on rapproche progressivement l'un vers l'autre. En fin de boucle, si aucune fausse note n'est détectée, il faut penser à renvoyer `True`.

* Une variante récursive est :
```python
def est_palindrome(ligne: str) -> bool:
    if ligne == "":
        return True
    elif ligne[0] == " ":
        return est_palindrome(ligne[1:])
    elif ligne[-1] == " ":
        return est_palindrome(ligne[:-1])
    elif ligne[0] != ligne[-1]:
        return False
    else:
        return est_palindrome(ligne[1:-1])
```

* Une solution très courte peut être :
    * Lire l'entrée, avec `input`.
    * La transformer en minuscule, avec `lower`.
    * Découper chaque mot autour des espaces, avec `split`.
    * On a une liste de mots, que l'on recolle sans espaces avec `"".join`.
    * On teste alors si le résultat est égal à son symétrique.
    * `truc[::-1]` renvoie une copie de la fin de truc jusqu'au début, à l'envers, par pas de $-1$.

```python
for _ in range(int(input())):
    IN = input()
    INI = "".join(IN.lower().split())
    if INI == INI[::-1]:
        print(IN)
```