# [Acronymes](http://www.france-ioi.org/algo/task.php?idChapter=556&iOrder=13)

## Sujet

Comme dans tout lieu de travail, les employés de la bibliothèque ont pris l’habitude d’utiliser des acronymes (exemples d’acronymes : IOI, RATP, BEPC, LOL...) pour les titres de livres les plus utilisés, ce qui leur permet de parler plus vite !

Seulement vous ne connaissez pas encore tous les acronymes, aussi lorsqu’on vous demande d’aller chercher un livre sans vous donner le titre complet, vous êtes bien embêté(e) !

Étant donné un acronyme, vous devez trouver tous les titres qui correspondent et les afficher "joliment".

### Contraintes

Tous les titres de livres ainsi que les acronymes contiennent au plus 200 caractères.

### Entrée

* Sur la première ligne, un acronyme, uniquement constitué de lettres majuscules.
* Sur la seconde ligne, un entier `nbLivres`, le nombre de titres de livres.
* Sur les `nbLivres` lignes suivantes les titres de livres, uniquement constitués de lettres ou d’espaces, sans accents.
* Les mots de chaque titre sont toujours séparés par un seul espace.

### Sortie

* Vous devez afficher chaque titre de livre qui correspond à l’acronyme, en mettant toutes ses lettres en minuscules sauf la première lettre de chaque mot, qui doit être en majuscule.

### Exemple

---

entrée :

```
PP
7
PEDro paramO
Poemes PALINDROMES
LA Condition HUMAINE
PERE et fils
petite
Promenade Au phare
peter pan
```

sortie :

```
Pedro Paramo
Poemes Palindromes
Peter Pan
```

---

## Solution

### Méthode lente

```python
acronyme = list(input().lower())
nb_titres = int(input())
for _ in range(nb_titres):
    titre = input().lower()
    mots = titre.split()
    if [mot[0] for mot in mots] == acronyme:
        print(" ".join(map(str.capitalize, mots)))
```

Cette méthode est lente, en effet elle calcule la totalité de l'acronyme d'un titre pour le comparer ensuite ; on pourrait pourtant avoir une réponse anticipée.

Créons une version fonctionnelle, un peu plus technique, mais qui répond plus vite en cas d'incompatibilité.

### Variante fonctionnelle

```python
from itertools import zip_longest

def filtre_titre(titre: str, acronyme: str) -> str:
    """
    Renvoie une version capitalizée de titre,
    uniquement si elle correspond à l'acronyme,
    sinon la chaîne vide ''

    >>> filtre_titre("sALut toI", "ST")
    'Salut Toi'
    
    >>> filtre_titre("Autre chose", "AZERTY")
    ''

    """
    mots = list(titre.split())
    if all(mot[0].upper() == lettre 
            for mot, lettre in zip_longest(mots, acronyme, fillvalue=" ")):
                return " ".join(map(str.capitalize, mots))
    return '' # sinon
    

acronyme = input()
nb_titres = int(input())
for _ in range(nb_titres):
    titre = filtre_titre(input(), acronyme)
    if titre != '':
        print(titre)
```

Les variantes ne sont pas forcément plus rapides, il faut d'abord que l'algorithme soit plus efficace, et là, oui, une variante fonctionnelle a ses avantages. En particulier avec Python, où les fonctions internes sont bien écrites et avec un langage rapide ; le C.

* Ici `zip_longuest` permet de zipper les deux listes, en prolongeant la plus courte, ici avec un caractère nécessairement différent.
