# [Décryptage](https://prologin.org/train/2011/semifinal/decryptage)

> Niveau 1

## Énoncé

Scooby-Naire, le chien de Joseph Marchand, est très intelligent. Il arrive à communiquer avec son maître en tapant ses messages sur le clavier. Malheureusement, ses grosses pattes ne lui permettent pas d'être précis et il appuie sur les touches alentour.

En revanche, le vocabulaire de Scooby-Naire étant assez limité, Joseph Marchand peut facilement tester les messages les plus courants. Pour l'y aider, vous devez écrire un programme qui renvoie `1` si la chaîne passée en paramètre peut-être contenue dans le message, `0` sinon.

### Entrée

* Sur la première ligne, un entier $M$ représentant la taille du message de Scooby-Naire.
* Sur la deuxième ligne, le message de Scooby-Naire.
* Sur la troisième ligne, un entier $N$ représentant la taille de la chaîne à tester.
* Sur la dernière ligne, la chaîne à tester.

### Sortie

+ `1` si la chaîne à tester est contenue dans le message de Scooby-Naire, `0` sinon.

### Contraintes

* Les messages ne dépassent pas $2\,000$ caractères.

#### Contraintes d'exécution
* Utilisation mémoire maximum : 500 kilo-octets
* Temps d'exécution maximum : 100 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    68
    Moi je le dis clairement: K est carrement trop fort, c'est mon idole
    15
    K est mon idole

Exemple de sortie

    1

---

Exemple d'entrée

    34
    TATA YOYO IL MA TAPE ON VA LE TUER
    10
    TTY MA TUE

Exemple de sortie

    1

---

Exemple d'entrée

    15
    JOSEPH MARCHAND
    3
    JEU

Exemple de sortie

    0

---

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 3 - Décryptage
https://prologin.org/train/2011/semifinal/decryptage
"""

# 0. Cœur du problème
def est_extrait(texte:str, partie: str) -> bool:
    """Renvoie True ou False selon que
    `partie` est un extrait de `texte`

    >>> est_extrait("Un morceau complet", "U orc cplt")
    True

    >>> est_extrait("Un morceau complet", "Z")
    False

    >>> est_extrait("Un morceau complet", "nU")
    False

    >>> est_extrait("J'ai dit ho", "diiit")
    False

    """
    l_texte = len(texte)
    l_partie = len(partie)
    i_texte = 0
    i_partie = 0
    while i_partie < l_partie:
        # on cherche le caractère partie[i_partie] dans texte
        while (i_texte < l_texte) and (texte[i_texte] != partie[i_partie]):
            i_texte += 1
        if i_texte == l_texte:
            return False
        else: # on a : texte[i_texte] == partie[i_partie]:
            i_partie += 1
            i_texte += 1
    return True

import doctest
doctest.testmod()


# 1. Lecture
taille_message_chien = int(input())
message_chien = input()
taille_message_test = int(input())
message_test = input()

# 2. Écriture
print("1" if est_extrait(message_chien, message_test) else "0")
```

> ⚠️ Nouveau, une version récursive élégante.

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 3 - Décryptage
https://prologin.org/train/2011/semifinal/decryptage
"""

# 0. Cœur du problème
def est_extrait(texte:str, partie: str) -> bool:
    """Renvoie True ou False selon que
    `partie` est un extrait de `texte`

    >>> est_extrait("Un morceau complet", "U orc cplt")
    True

    >>> est_extrait("Un morceau complet", "Z")
    False

    >>> est_extrait("Un morceau complet", "nU")
    False

    >>> est_extrait("J'ai dit ho", "diiit")
    False

    """
    if partie == "":
        return True
    if texte == "":
        return False
    if partie[0] == texte[0]:
        return est_extrait(texte[1:], partie[1:])
    else:
        return est_extrait(texte[1:], partie)

import doctest
doctest.testmod()


# 1. Lecture
taille_message_chien = int(input())
message_chien = input()
taille_message_test = int(input())
message_test = input()

# 2. Écriture
print("1" if est_extrait(message_chien, message_test) else "0")
```

Explications :
1. Si `partie` est vide, on a fini, et c'est bon.
2. Si `texte` est vide, `partie` est non vide, et donc c'est pas bon.
3. Sinon, les deux sont non vides ; on peut comparer leur premier caractère ; il existe.
    1. Si c'est le même, par récursivité, on cherche le caractère suivant dans le reste des deux.
    2. Sinon, on cherche le même premier caractère de `partie` dans la suite de `texte`.
