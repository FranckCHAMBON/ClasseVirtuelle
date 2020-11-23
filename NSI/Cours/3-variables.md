## Variables et affectation

### Présentation de l'affectation

Nous avons vu que l'on pouvait utiliser des variables avec des noms plus longs qu'une lettre à l'opposé de ce que l'on voit souvent en maths ou en sciences. C'est une bonne pratique.

Variable *Python*
: - Une variable possède un nom.
  - Une variable pointe vers un objet, (une donnée) (*cet objet est peut être partagé*).
  - L'objet possède parfois une valeur (ou plusieurs, et des méthodes).
  - Par abus de langage on dit souvent qu'elle a une valeur. C'est pourtant faux en Python !
  - Dans d'autres langages c'est vrai, d'où la confusion.

Affectation simple
: - L'opérateur `=` réalise l'affectation, il n'est pas symétrique.
  - En pseudo-code `a = 5` se note $a \leftarrow 5$.
  - L'affectation désigne ce vers quoi la variable pointe.
  - Dans une affectation simple :
    - le membre de gauche doit être une variable,
    - le membre de droite est d'abord évalué,
    - puis le résultat est affecté à la variable.

```python
In [40]: a = 3         #  un entier de valeur 3 est affecté à a,

In [41]: x = 20 - a*5  # 5 est affecté à x

In [42]: x = 2*x + 1   # 11 est affecté à x

In [43]: y = x*x - 1

In [44]: y
Out[44]: 120
```

> Remarques :

- Par abus de langage on pourra souvent dire que la valeur de `y` est 120. Avec plus de rigueur, on dira que `y` pointe vers un entier de valeur 120.
- Dans la troisième instruction, l'ancienne valeur de `x` est utilisée dans le calcul du membre de droite. Le résultat du membre de droite est stocké, la variable `x` pointe alors vers ce résultat.
- En console, une affectation ne produit pas d'affichage.
- On peut faire des commentaires dans une instruction en commençant par le **croisillon** `#`.
  - Croisillon n'est pas un dièse, et en anglais on dit *sharp*, ou aussi parfois *hash*.
  - Un commentaire n'est pas interprété par Python.

### Affectation plus précisément

Pour une seconde lecture !

Affectation
:  - Le membre de gauche doit être une ou plusieurs variables.
   - Le membre de droite est soit :
      - un littéral (*une donnée écrite dans le code*)
      - une instruction que l'on peut évaluer
      - une autre affectation
   - Le membre de droite est interprété en premier.
   - Le ou les résultats sont affectés à la ou aux variables :
      - s'il n'y a qu'une variable et plusieurs résultats, le tuple des résultats est affecté à la variable ;
      - s'il y a autant de variables que de résultats, dans l'ordre chaque résultat est affecté à une variable ;
      - sinon, une `ValueError` se produit.
      - Pour les utilisateurs avancés, il y a encore plus général, à coup de *pack/unpack* ; voir l'exemple 56, bien plus technique (et totalement hors programme NSI). Encore plus général, le *unpack* existe aussi pour les dictionnaires, souvent écrit `**kwargs` ; un exemple sera donné après la présentation des dictionnaires.

Exemples :

```python
In [50]: a, b = 2, 3, 4
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: too many values to unpack (expected 2)

In [51]: a, b, c, d = 2, 3, 4
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: not enough values to unpack (expected 4, got 3)

In [52]: a, b, c = 2, 3, 4

In [53]: a + b*c
Out[53]: 14

In [54]: a = 2, 3, 4

In [55]: a[0], sum(a), a
Out[55]: (2, 9, (2, 3, 4))

In [56]: a, b, *c, d = 1, *a, 5, 6; print(a, b, c, d)
Out[56]: 1 2 [3, 4, 5] 6
```

**Utilisations pratiques** :

Il est alors possible, en Python, de faire de [l'affectation parallèle](https://fr.wiktionary.org/wiki/affectation_parall%C3%A8le).
> 1] C'est particulièrement pratique pour échanger le contenu de deux variables `x` et `y`.

```python
temp = x
x = y
y = temp
```

Le code ci-dessus peut être remplacé par :

```python
x, y = y, x
```

> 2] Il est possible aussi, en Python, de faire de [l'affectation multiple](https://fr.wiktionary.org/wiki/affectation_multiple) `c = b = a`

#### Le nom d'une variable

On ne peut pas choisir n’importe quel nom pour une variable.
De manière synthétique, on a :

- **Conseil important :** N’utiliser que les caractères : `a→z`, `A→Z`, `0→9` et `_`
- **Obligatoire :** Ne pas débuter par un chiffre
- **Conseil :** `choisir_un_nom_de_variable_lisible`, `choisirUnNomDeVariablePlusLisible`, `nepaschoisirunnomdevariableillisible`, `JE_SUIS_UNE_JOLIE_CONSTANTE`
- *Exemples :* `nombre_dOr`, `a15` sont valides et lisibles.
- *Attention :* `niter`, `nIter`, `NITER` sont trois variables différentes, la seconde étant la plus lisible des trois.
- *Remarque :* les lettres Unicode sont autorisées comme `Çå_Ãĺòŕš`, mais non conseillées.
- *Conseil :* ne pas débuter par `_`, sauf si vous savez/voulez travailler avec des variables privées.
- [Pour en savoir plus sur le snake_case et ses variantes](https://fr.wikipedia.org/wiki/Snake_case).


:fa-bolt: **Exemple méchant authentique**
```python {.line-numbers cmd="python3" output="text"}
value = 42
valuе = 1000
print(value)
# on s'attend à un affichage de 1000 ; logique ! Et NON !!!
```

    42


**Explication :**
- le premier `value` est écrit avec des caractères directement accessibles au clavier, la dernière lettre est un 'e' latin dont le code est 101.
- le second `valuе` se termine par un 'е' cyrillique dont le code est 1077. Visuellement identique, ce n'est pas le même caractère, et donc il y a **deux** variables différentes.
- le 'print' agit sur la première variable... **Le piège est redoutable et totalement invisible.**

*Further reading : [WTFPython](https://github.com/satwikkansal/wtfpython).* ***Warning*** *very difficult.*

Ceci constitue probablement une raison (pour certains) de déconseiller l'utilisation de variables avec lettres Unicode. La véritable raison est ailleurs. Écrire un code qui a vocation à rester dans un cercle restreint - éducatif par exemple, une classe - peut parfaitement utiliser des variables avec des noms qui ont un sens en français et même avec accents. Pour se prémunir du piège précédent, il suffit d'utiliser un explorateur de variables (inclus dans *Spyder*) ; cela aide beaucoup à identifier des noms de variables proches (et qui ne le devraient pas) !

Par contre, un code qui a vocation à être utilisé et partagé largement **doit** :

* Avoir des noms de variables qui ont un sens en anglais.
* N'utiliser que les caractères `a→z`, `A→Z`, `0→9` et `_` dans les noms de variables.
* Avoir des commentaires en anglais.

L'objectif étant d'avoir un code qui soit compris et utilisable par la communauté ; et l'anglais est la norme !

> Dans la suite de ce cours, en français, pour un public francophone, on utilisera des identifiants de variable : 
> * en français ; *pour mieux différencier les mots du langage Python*
> * avec accents ; *tous les accents, on reste cohérents*,
> * avec de rares abréviations, comme `nb` pour 'nombre de'.

### Les mots réservés de Python3

Il y a **35 mots réservés** (dont deux récents) qui ne peuvent pas être utilisés pour des variables.

> |           |           |           |           |         |
> |:----------|:----------|:----------|:----------|:--------|
> |`False`    |`class`    |`finally`  |`is`       |`return` |
> |`None`     |`continue` |`for`      |`lambda`   |`try`    |
> |`True`     |`def`      |`from`     |`nonlocal` |`while`  |
> |`and`      |`del`      |`global`   |`not`      |`with`   |
> |`as`       |`elif`     |`if`       |`or`       |`yield`  |
> |`assert`   |`else`     |`import`   |`pass`     |`async`        |
> |`break`    |`except`   |`in`       |`raise`    |`await`         |
>
> *Remarque* : Seuls `False`, `None` et `True` commencent ici avec une majuscule.

Nous avons déjà vu :

- `False` et `True` : les booléens Faux et Vrai.
- `from` et `import` : pour importer **à partir** d'un module.
- `is` : test d'identité entre objets.

Nous allons bientôt voir :

- `None` : pour une donnée 'sans valeur' ; zéro étant un entier possédant une valeur.
- `del` : pour détruire (*<b>del</b>ete*) une variable et/ou des données.
- `and`, `or`, `not` : opérateurs sur les booléens : **et**, **ou**, **non**.
- `def` ou `lambda`, `return` : pour définir une fonction.
- `pass` : une instruction qui ne fait rien.
- `if`, `elif`, `else` : pour les structures conditionnelles.
- `for`, `while` : pour créer des boucles.
- `break`, `continue` : pour des boucles plus complexes.
- `in` : pour un test d'appartenance.

Nous verrons plus tard certains mots réservés parmi ceux qui restent.

- `assert` : pour le débogage facile.
- `try`, `except`, `raise` : pour la gestion des erreurs.
- `with`, `as` : pour la lecture de module ou de fichier.

Pour les utilisateurs avancés :
- `class` : pour la programmation orientée objet (POO).
- `global`, `nonlocal` : pour modifier la portée d'une variable.
- `yield` : pour la construction d'itérateur.
