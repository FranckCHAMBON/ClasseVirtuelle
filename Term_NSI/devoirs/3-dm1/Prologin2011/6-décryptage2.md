# [Décryptage II](https://prologin.org/train/2011/semifinal/decryptage2)

> Niveau 2

## Énoncé

Scooby-Naire, le chien de Joseph Marchand, est très intelligent. Il arrive à communiquer avec son maître en tapant ses messages sur le clavier. Malheureusement, ses grosses pattes ne lui permettent pas d'être précis et il appuie sur les touches alentour.

De plus, Joseph Marchand, un peu zinzin, s'est trompé et a donné des croquettes pour chat à Scooby-Naire ! Du coup, celui-ci n'est plus trop sûr de l'ordre des lettres dans ses phrases et écrit un peu n'importe comment...

En revanche, le vocabulaire de Scooby-Naire étant assez limité, Joseph Marchand peut facilement tester les messages les plus courants. Pour l'y aider, vous devez écrire un programme qui renvoie 1 si la chaîne passée en paramètre peut-être contenue dans le message, 0 sinon.

### Entrée

+ Sur la première ligne, l'entier $M$ représentant la taille du message de Scooby-Naire.
+ Sur la deuxième ligne, le message de Scooby-Naire.
+ Sur la troisième ligne, l'entier $N$ représentant la taille de la chaîne à tester.
+ Sur la dernière ligne, la chaîne à tester.

### Sortie

`1` si tous les caractères de la chaîne à tester sont contenus dans le message, `0` sinon. Attention : si le caractère `A` est contenu 3 fois dans la chaîne à tester, il doit être contenu au moins autant de fois dans le message de Scooby-Naire.

### Contraintes

+ Scooby-Naire étant paresseux, il n'écrit pas de messages dépassant $2\,000$ caractères.

#### Contraintes d'exécution

+ Utilisation mémoire maximum : 500 kilo-octets
+ Temps d'exécution maximum : 100 millisecondes

### Exemples d'entrée/sortie

---

Exemple d'entrée

    56
    IL FAUT TUER LA VIEILLE TATA, ELLE M'A TUE AVEC SON YOYO
    11
    TTY MA TUER

Exemple de sortie

    1

---

Exemple d'entrée

    91
    Ca ne peut pas matcher, a une lettre pres en plus... De toute facon c'est totalement faux !
    9
    K est nul

Exemple de sortie

    0

---

## Solution

```python
"""
auteur : Franck CHAMBON
Régional 2011 - Problème 6 - Décryptage II
https://prologin.org/train/2011/semifinal/decryptage2
"""

# 0. Cœur du problème
def est_inclus(extrait: str, texte: str) -> bool:
    """Renvoie True si touts les caractères de 'extrait' sont inclus
    dans 'texte', avec multiplicité, mais sans compter l'ordre.
    >>> est_inclus("ABAC", "BRAVO, CHARLIE.")
    1
    >>> est_inclus("ABBAC", "BRAVO, CHARLIE.")
    0
    """
    CONST_ASCII = 128
    def compte(morceau: str) -> list:
        """Renvoie la liste du compte des caractères.
        >>> compte("ABAC")[ord('A')]
        2
        >>> compte("ABAC")[ord('D')]
        0
        """
        compte_morceau = [0 for _ in range(CONST_ASCII)]
        for caractère in morceau:
            i = ord(caractère)
            compte_morceau[i] += 1
        return compte_morceau
    
    
    # version fonctionnelle
    return all(cpt_extrait <= cpt_texte
                    for cpt_extrait, cpt_texte in
                    zip(compte(extrait), compte(texte)))
    
    # version itérative
    compte_extrait = compte(extrait)
    compte_texte = compte(texte)
    for i in range(CONST_ASCII):
        if compte_extrait[i] > compte_texte[i]:
            return False
    return True

# 1. Lecture
taille_message_scooby_naire = int(input())
message_scooby_naire = input()
taille_message_test = int(input())
message_test = input()

# 2. Écriture
print(1 if est_inclus(message_test, message_scooby_naire) else 0)
```

### Commentaire

Il n'était pas précisé dans l'énoncé que les caractères étaient tous en ASCII, donc avec un code (que l'on obtient avec `ord`) compris entre $0$ et $127$ inclus.

Proposons une version avec un dictionnaire, qui est capable de fonctionner avec tous jeux de caractères.

Nous proposerons ensuite une version avec un type nouveau `Counter` qui a été pensé justement pour les dictionnaires qui servent à compter des éléments d'un ensemble.

#### Version itérative avec `dict`
```python
# 0. Cœur du problème
def est_inclus(extrait: str, texte: str) -> bool:
    """Renvoie True si touts les caractères de 'extrait' sont inclus
    dans 'texte', avec multiplicité, mais sans compter l'ordre.
    >>> est_inclus("ABAC", "BRAVO, CHARLIE.")
    1
    >>> est_inclus("ABBAC", "BRAVO, CHARLIE.")
    0
    """
    def compte(morceau: str) -> dict:
        """Renvoie un `Counter` des caractères.
        >>> compte("ABAC") == {'A': 2, 'B': 1, 'C': 1}
        True
        >>> compte("ABBAC") == {'A': 2, 'B': 2, 'C': 1}
        True
        """
        compte_morceau = dict()
        for caractère in morceau:
            if caractère not in compte_morceau:
                compte_morceau[caractère] = 1
            else:
                compte_morceau[caractère] += 1
        return compte_morceau
    
    
    # version itérative
    compte_extrait = compte(extrait)
    compte_texte = compte(texte)
    for caractère in compte_extrait:
        if caractère not in compte_texte:
            return False
        else:
            if compte_extrait[caractère] > compte_texte[caractère]:
                return False
    return True
```

On constate qu'il faut tester l'appartenance d'une clé au dictionnaire...

#### Version itérative avec `Counter`
```python
from collections import Counter

# 0. Cœur du problème
def est_inclus(extrait: str, texte: str) -> bool:
    """Renvoie True si touts les caractères de 'extrait' sont inclus
    dans 'texte', avec multiplicité, mais sans compter l'ordre.
    >>> est_inclus("ABAC", "BRAVO, CHARLIE.")
    1
    >>> est_inclus("ABBAC", "BRAVO, CHARLIE.")
    0
    """
    def compte(morceau: str) -> Counter:
        """Renvoie un `Counter` des caractères.
        >>> compte("ABAC") == {'A': 2, 'B': 1, 'C': 1}
        True
        >>> compte("ABBAC") == {'A': 2, 'B': 2, 'C': 1}
        True
        """
        compte_morceau = Counter()
        for caractère in morceau:
            compte_morceau[caractère] += 1
        return compte_morceau
    
    
    # version itérative
    compte_extrait = compte(extrait)
    compte_texte = compte(texte)
    for caractère in compte_extrait:
        if compte_extrait[caractère] > compte_texte[caractère]:
            return False
    return True
```

Ici inutile de tester l'appartenance ; la valeur $0$ est renvoyée par défaut.

#### Version fonctionnelle avec `Counter`
```python
    #...

    # version fonctionnelle
    compte_extrait = compte(extrait)
    compte_texte = compte(texte)
    return all(compte_extrait[caractère] <= compte_texte[caractère]
                 for caractère in compte_extrait)
```

On constate qu'on peut facilement utiliser `compte_texte[caractère]` qui est par défaut à $0$ si `caractère` n'est pas une clé de `compte_texte`. Chose que nous n'aurions pas pu faire avec un dictionnaire conventionnel.