# [Chiffrement par décalage](http://www.france-ioi.org/algo/task.php?idChapter=556&iOrder=18)

## Sujet

Alors que vous avez enfin trouvé le livre que vous cherchiez, il s’avère qu’il était complètement chiffré. Vous avez déjà réussi à déchiffrer la première page du livre, et celle-ci vous a indiqué le système de chiffrement utilisé dans le reste du livre.

La clé de chiffrement est ici un simple nombre, qu’on appelle `D`, pour « décalage ». On remplace alors chaque lettre de l’alphabet par la lettre située `D` places plus loin dans l’alphabet, considéré de manière circulaire.

Ainsi, si le décalage est de 2, alors

* `A` devient `C`
* `B` devient `D`
* ...
* `X` devient `Z`
* `Y` devient `A`
* `Z` devient `B`

La clé utilisée pour chiffrer le texte change à chaque page et pour la page numéro $X$ elle vaut

* $3 × X$ si $X$ est pair
* $-5 × X$ si $X$ est impair

À vous de déchiffrer tout le livre !

### Contraintes

Chaque ligne contient au plus 1000 caractères.

### Entrée

* La première ligne contient un entier `nbPages`, le nombre total de pages du livre.

* Les `nbPages - 1` lignes suivantes contiennent chacune le texte des pages numéro `2, 3, 4,..., nbPages`.

Le texte peut contenir des lettres, chiffres ou caractères de ponctuation, mais pas d’accents.

### Sortie

* Vous devez afficher le texte déchiffré pour chacune des pages.

* Chaque lettre codée doit être remplacé par la lettre décodée. Les autres caractères (ponctuation, `_`, espaces, chiffres), sont laissés tels quels.

* Vous devez respecter la casse : si une lettre était en majuscule (ou minuscule), elle doit le rester !

### Exemple

---

entrée :

```
4
Ikio kyz rg ykiutjk vgmk ja robxk
Npeep alrp pde wl alrp yfxpcz 3
Qf hauou pazo xm cgmfduqyq bmsq !
```

sortie :

```
Ceci est la seconde page du livre
Cette page est la page numero 3
Et voici donc la quatrieme page !
```

## Solution

```python
def déchiffre(lettre: str, clé: int) -> str:
    """
    Déchiffre la `lettre` en fonction de la `clé`.
    
    >>> déchiffre('A', 2)
    'C'
    
    >>> déchiffre('z', 2)
    'b'
    
    """
    def tourne_autour(lettre, pivot, clé):
        indice = ord(lettre) - ord(pivot)
        indice_déchiffré = (indice - clé) % 26
        return chr(ord(pivot) + indice_déchiffré)
    
    if 'a' <= lettre <= 'z':
        return tourne_autour(lettre, 'a', clé) # déchiffrement
    elif 'A' <= lettre <= 'Z':
        return tourne_autour(lettre, 'A', clé) 
    else:
        return lettre    # aucun changement

nb_pages = int(input())
for page in range(2, nb_pages + 1):
    ligne = input()
    clé = (-5 * page) if page % 2 == 1 else (3 * page)
    print("".join((déchiffre(lettre, clé) for lettre in ligne)))
```

