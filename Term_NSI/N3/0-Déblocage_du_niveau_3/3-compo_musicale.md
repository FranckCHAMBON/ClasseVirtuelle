# [Composition musicale](http://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2240)



Écouter de la musique peut être très agréable mais lorsqu'un morceau est vraiment très répétitif, il arrive parfois qu'on s'ennuie un peu. Aussi le professeur de composition musicale du conservatoire a décidé d'imposer une règle très stricte : quand il relit les morceaux composés par ses élèves, dès qu'il voit deux notes identiques côte à côte, il les efface toutes les deux ! Il continue ainsi d'effacer tant qu'il existe deux notes égales consécutives.

Ce travail étant long et fastidieux, il se demande s'il n'est pas possible de l'automatiser.

## Ce que doit faire votre programme :

Les notes de musiques sont représentées par les lettres 'a', 'b', 'c', 'd', 'e', 'f' et 'g'.

Votre programme doit lire une seule ligne de texte représentant le morceau de musique (composé de moins de 500 notes) et doit afficher la version du morceau "corrigée" où tous les doublons sont supprimés tant qu'il en existe.

### Exemple

entrée :

    baaabbacddc

sortie :

    b

### Commentaires

Sur l'exemple donné une suite possible d'élimination des doublons est la suivante :

    baaabbacddc
    baaabbacc
    babbacc
    babba
    baa
    b

## Solution

```python
def doublon(ligne):
    """renvoie la première position dans 'ligne' d'un doublon
    renvoie None sinon
    """
    for i in range(len(ligne)-1):
        if ligne[i] == ligne[i+1]:
            # un doublon est trouvé
            return i
    # aucun doublon trouvé
    return None
    
def élimine(ligne, pos):
    """élimine les notes de 'ligne' en position pos et pos+1"""
    ligne.pop(pos)
    ligne.pop(pos)

def nettoie(ligne):
    """Répète l'élimination des doublons tant qu'il y en a."""
    pos = doublon(ligne)
    while pos is not None:
        élimine(ligne, pos)
        pos = doublon(ligne)

ligne = list(input())
néttoie(ligne)
print("".join(ligne))
```

### Commentaires

* Pour `doublon`, il est classique d'utiliser `None` pour désigner une absence de réponse favorable.
* Pour `élimine`, on enlève l'élément en position `pos`, deux fois, mais ce ne sont pas les même. Une fois l'un enlevé, le suivant devient celui en position `pos`...
* Pour `nettoie`, on répète `élimine` tant que `pos` est différent de `None`.
    * On propose ci-dessous deux variantes pour `nettoie`.
        * la première est une version récursive, dont la compréhension est au programme de terminale.
        * la seconde utilise une nouveauté de Python, et est totalement hors-programme.

```python
def nettoie(ligne):
    "Version récursive"
    pos = doublon(ligne)
    if pos is not None:
        élimine(ligne, pos)
        nettoie(ligne)

def nettoie(ligne):
    "Version avec l'opérateur morse"
    while (pos := doublon(ligne)) is not None:
        élimine(ligne, pos)
```

Cette dernière version n'est possible qu'avec une version de Python, à partir de 3.8. [Elle utilise l'opérateur morse](https://docs.python.org/fr/3/whatsnew/3.8.html).
