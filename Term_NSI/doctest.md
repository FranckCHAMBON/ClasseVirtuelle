# Construire et utiliser ses *doctest*

* Lire rapidement la [documentation](https://docs.python.org/fr/3/library/doctest.html)

## TL;DR

Une fois vos *doctest* écrits, ajouter ceci à la fin de vos déclarations de fonction :
```python
import doctest
doctest.testmod()
```
Et lancer votre code.
> Une absence de message signifie que les tests sont bons.


## Plus en détail

Pour résoudre un problème, on partagera souvent le travail en trois parties :
* La lecture sur l'entrée standard des données.
* Le traitement des données, via une fonction.
* L'affichage du résultat sur la sortie standard.

Le cœur du problème étant le traitement, pour lequel on écrit une fonction, et que l'on documente avec des tests. Tout ça grâce à *doctest*.

* Il est important de bien décrire dans une *docstring* le principe de la fonction. C'est une compétence importante à avoir. Pour soi, mais aussi pour les lecteurs du code que vous partagez, collègues, examinateurs, supérieurs, vous-même du futur...

* Il est important aussi de pratiquer l'annotation de type (quand ils sont simples), cela aide à la compréhension de la description de la fonction. Avec certains langages de programmation, c'est obligatoire, et cela peut aider à éviter de nombreux *bugs*.

* Nous parlerons ici plus en détail des tests à inclure dans la *docstring* qui permettent d'améliorer la description et surtout de faire des vérifications automatiques. Améliorer et préciser certains détails...

### Principe du test

On écrit le comportement attendu en cas d'utilisation de la fonction dans une console.

### Exemples

```python
def indice_lettre_minuscule(lettre: str) -> int:
    """Renvoie l'indice d'une lettre minuscule de l'alphabet.

    >>> indice_lettre_minuscule('a')
    0

    >>> indice_lettre_minuscule('z')
    25

    """
    if len(lettre) != 1:
        raise ValueError("`lettre` doit avoir **un seul** caractère")    
    if not('a' <= lettre <= 'z'):
        raise ValueError("`lettre` doit être en minuscule")

    return ord(lettre) - ord('a')

def lettre_minuscule(indice: int) -> str:
    """Renvoie la lettre minuscule dont `indice` est donné.

    >>> lettre_minuscule(0)
    'a'

    >>> lettre_minuscule(25)
    'z'

    """
    if not(0 <= indice < 26):
        raise ValueError("`indice` doit être de 0 inclus à 26 exclu")
    return chr(ord('a') + indice)

import doctest
doctest.testmod()

# ... suite de votre programme
# * lecture de l'entrée
# * utilisation des fonctions
# * écriture de la sortie
```

**Entraînez-vous à faire un _doctest_ pour chaque fonction simple.** Il doit être court, et essayer de déjouer des pièges possibles...

**Pour aller plus loin**
> ⚠️ On remarquera qu'en console, si la sortie attendue est de type `str`, elle est écrite entre guillemets simples `'` ; vous devez en faire autant dans le *doctest*, exactement comme si c'était une utilisation en console Python.
> * Si la chaîne contient elle-même des guillemets simples, alors elle est affichée entre guillemets doubles.
> * Si la chaîne contient les deux types de guillemets, alors elle est entre guillemets simples, et les guillemets simples intérieurs sont échappés.
>
> Et bien sûr, **lire en détail** la [documentation](https://docs.python.org/fr/3/library/doctest.html)

