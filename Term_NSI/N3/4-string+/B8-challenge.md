# [Trouver le décalage](http://www.france-ioi.org/algo/task.php?idChapter=556&iOrder=19)

## Sujet

Alors que vous avez enfin trouvé le livre que vous cherchiez, il s’avère qu’il était complétement chiffré. Vous avez réussi à déchiffrer la première page du livre, et celle-ci vous a indiqué un système de chiffrement utilisé dans le reste du livre. Sauf que cela ne marchait pas pour la dernière page du texte, celle qui vous intéresse le plus, car elle indique l’emplacement de la plante secrète !

Le système de chiffrement utilisé est le même que celui des pages précédentes : La clé de chiffrement est ici un simple nombre, qu’on appelle `D`, pour « décalage ». On remplace alors chaque lettre de l’alphabet par la lettre située `D` places plus loin dans l’alphabet, considéré de manière circulaire.

Ainsi, si le décalage est de 2, alors

* `A` devient `C`
* `B` devient `D`
* ...
* `X` devient `Z`
* `Y` devient `A`
* `Z` devient `B`

Seulement, vous ne connaissez pas la clé, aucun indice de vous permet de la trouver !

La seule chose que vous savez, c’est qu’il s’agit d’un texte normal (c’est-à-dire non piégé), et qu’il est écrit en français. À vous d’utiliser les connaissances que vous avez sur ce langage afin de trouver la bonne clé !

### Contraintes

La ligne de texte contient au plus $10\,000$ caractères.

### Entrée

* Une ligne de texte à décrypter.

* Le texte peut contenir des lettres, chiffres ou caractères de ponctuation, mais pas d’accents.

### Sortie

* Vous devez afficher le texte décrypté.

* Chaque lettre codée doit être remplacée par la lettre décodée. Les autres caractères (ponctuation, `_`, espaces, chiffres), sont laissés tels quels.

* Vous devez respecter la casse : si une lettre était en majuscule (ou minuscule), elle doit le rester !

### Exemple

---

entrée :

```
Np epiep fetwtdp fy opnlwlrp op zykp nlclnepcpd.
```

sortie :

```
Ce texte utilise un decalage de onze caracteres.
```

---

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

CONST_fr_indice_freq_max = ord('E') - ord('A')
CONST_taille_alphabet = 26
texte = input()
fréquence_lettre = [0 for _ in range(CONST_taille_alphabet)]
fréquence_max = 0
indice_max = -1
for lettre in texte.upper():
    if 'A' <= lettre <= 'Z':
        indice = ord(lettre) - ord('A')
        fréquence_lettre[indice] += 1
        if fréquence_lettre[indice] > fréquence_max:
            fréquence_max = fréquence_lettre[indice]
            indice_max = indice

clé = (indice_max - CONST_fr_indice_freq_max) % CONST_taille_alphabet

print("".join(déchiffre(lettre, clé) for lettre in texte))
```

