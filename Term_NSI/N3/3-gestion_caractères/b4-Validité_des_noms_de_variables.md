# [Validité des noms de variables](http://www.france-ioi.org/algo/task.php?idChapter=566&idTask=458)

La jeune Ada, fascinée par votre robot, a écrit plusieurs programmes, mais elle a souvent des difficultés avec les noms de variables : elle a du mal à savoir si un nom de variable est correct ou pas.

Ada utilise, elle, le langage C++ pour programmer et la règle pour les noms de variables dans ce langage est la suivante : le nom de variable doit commencer par une lettre non accentuée ou un caractère `_`, et chacune des lettres suivantes est soit une lettre non accentuée, soit un `_`, soit un chiffre.

## Contraintes

La longueur de chaque nom proposé ne dépassera pas 100 caractères.

### Entrée

La première ligne contient l’entier `nbNoms`. Les `nbNoms` lignes suivantes contiennent chacune un nom de variable possible.

Aucun des noms de variable possibles ne sera un mot-clef du langage. Vous n’avez donc pas à vous en occuper.

### Sortie

Vous devez afficher `nbNoms` lignes sur la sortie, indiquant dans l'ordre où ils sont donnés en entrée, si les noms proposés sont valides.

Affichez le texte "YES" pour un identifiant valide et "NO" pour un identifiant invalide.

### Exemple

entrée :

    5
    Bonjour32
    r~ussi
    _toto_
    passe-partout
    2_fois

sortie :

    YES
    NO
    YES
    NO
    NO

## Solution

```python
def est_valide(nom: str) -> bool:
    """Renvoie si 'nom' est un identifiant valide.

    >>> est_valide("Bon_jour32")
    True

    >>> est_valide("32Bonjour")
    False
    
    """
    if not(('a' <= nom[0] <= 'z') or ('A' <= nom[0] <= 'Z') or (nom[0] == '_')):
        return False
    for i in range(1, len(nom)):
        if not( ('a' <= nom[i] <= 'z') or \
                ('A' <= nom[i] <= 'Z') or \
                (nom[i] == '_') or \
                ('0' <= nom[i] <= '9')):
            return False
    return True
    

nb_noms = int(input())
for _ in range(nb_noms):
    nom = input()
    if est_valide(nom):
        print("YES")
    else:
        print("NO")
```

### Commentaires

* Une ligne de code trop grande peut être coupée avec `\`, et poursuivie à la ligne suivante.
* Utiliser une fonction et pratiquer les retours prématurés est une bonne pratique. Ce n'était pas considéré comme une bonne pratique dans les années 1970 ; cela à changé. Il faut bien penser à gérer tous les cas, et renvoyer un résultat à la fin !
* On peut factoriser le code des 4 dernières lignes avec l'opérateur ternaire conditionnel. On peut aussi se passer de certaines variables.

```python
nb_noms = int(input())
for _ in range(nb_noms):
    nom = input()
    print("YES" if est_valide(nom) else "NO")
    # pas d'erreur, il n'y a pas de ':'
```

```python
# factorisation maximale, mais moins lisible
for _ in range(int(input())):
    print("YES" if est_valide(input()) else "NO")
```