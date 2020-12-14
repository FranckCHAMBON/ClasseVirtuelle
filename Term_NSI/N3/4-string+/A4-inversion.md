# [Inversion de dictionnaire](http://www.france-ioi.org/algo/chapter.php?idChapter=556)

## Sujet
La bibliothèque contient de nombreux dictionnaires, mais pour certains couples de langues, elle ne dispose que du dictionnaire permettant d’aller de la première langue vers la seconde, et pas du dictionnaire permettant de faire l’inverse.

Étant donné un dictionnaire bilingue, vous devez l’inverser pour construire le dictionnaire inverse.

### Contraintes

Chaque mot contient au plus 50 caractères.

### Entrée

* La première ligne contient l’entier `nbMots`.
* Les `nbMots` lignes suivantes contiennent chacune deux mots séparés par un espace : un mot dans la première langue et un mot dans la seconde.
* Les mots ne contiennent pas d’espaces et sont constitués uniquement de lettres minuscules.
* Les couples de mots sont triés selon l’ordre alphabétique des mots de la première langue.

### Sortie

* Vous devez afficher l’ensemble des couples de mots inversés (d’abord le mot de la seconde langue, puis le mot de la première) triés selon l’ordre alphabétique des mots de la seconde langue.

### Exemple

---

entrée :

```
2
travail work
verite truth
```

sortie :

```
truth verite
work travail
```

---

## Solution

Il est inutile d'utiliser la structure de données `dict` de Python, une liste de `tuple` sera suffisante, on peut trier cette liste de couple facilement en créant la liste avec la seconde langue en premier dans le `tuple`.

```python
nb_traductions = int(input())
traductions = []
for i in range(nb_traductions):
    mot_lang1, mot_lang2 = input().split()
    traductions.append((mot_lang2, mot_lang1)) # stockage inversé

traductions.sort() # tri sur la première composante par défaut

for (mot_lang2, mot_lang1) in traductions:
    print(mot_lang2, mot_lang1)
```
