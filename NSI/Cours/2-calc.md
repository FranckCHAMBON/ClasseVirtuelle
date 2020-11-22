## :fa-calculator: La console Python comme calculatrice

### Travail avec des entiers

Python est capable de travailler avec des nombres aussi grands que la mémoire de la machine le permet.

> :fa-bolt: Attention, l'affichage de nombres très grands peut prendre beaucoup de temps. Les calculs en représentation binaire peuvent être très rapides en revanche !

#### Opérations élémentaires  `+` `-` `*`

Rien de particulier à signaler, si ce n'est que :

- les priorités sont bien respectées,
- on peut aussi utiliser des parenthèses,
- les multiplications doivent être explicites.

#### Division entière et modulo `//` `%`

Commençons à travailler avec des entiers.

- L'opérateur du quotient de la division entière est `//`
- Pour obtenir le reste dans la division entière, on utilise l'opérateur modulo `%`

```python
In [1]: 1984 % 100
Out[1]: 84

In [2]: 1984 // 100
Out[2]: 19
```

> :fa-bolt: Il ne faut pas oublier de doubler le caractère /
> Sinon, l'opération donnera un flottant. (Voir ensuite)

#### Puissance `**`

Exemple du calcul de un milliard sept.

```python
In [3]: 10**9 + 7
Out[3]: 1000000007
```

#### :fa-key: Chiffres d'une puissance d'entiers

> - Quels sont les trois derniers chiffres de $456^{78}$ ? (*Ne faire afficher que ceux-là !*)
> - :fa-shield: Quel est le 50^ième^ chiffre en partant des unités de 1337 à la puissance 42 ?
>
>> :fa-bolt: Le calcul modulaire est massivement employé en informatique, en particulier en sécurité comme la cryptographie.

#### Comparaisons `<` `<=` `==` `<>` `!=` `>=` `>`

On a les opérateurs de comparaison :

- `<` strictement inférieur à
- `<=` inférieur ou égal à
- `==` égal à
- `<>` différent de
- `!=` différent de (*variante*)
- `>=` supérieur ou égal à
- `>` strictement supérieur à

Ces opérateurs retournent un booléen : soit Vrai (*True*), soit Faux (*False*).

> Exemples, avec une identité remarquable et un calcul de factorielle avec un résultat très grand.

```python
In [4]: (50 + 3)**2 == 50**2 + 2*50*3 + 3**2
Out[4]: True

In [5]: from math import factorial

In [6]: factorial(2019) < 10**5000
Out[6]: False
```

> :fa-info: **La factorielle** (*factorial*  en anglais) d'un entier $n$ est le produit $1\times 2\times 3\times 4\times \cdots \times n$. On la note $n!$
>> Exemple : $5! = 1\times 2\times 3\times 4\times 5 = 120$.
>
> `from math import factorial` , cette ligne importe la fonction factorielle depuis le module math.
> On constate ici que $2019!$ possède plus de 5000 chiffres.

### Travail avec les flottants

> :fa-bolt: Les [flottants](https://fr.wikipedia.org/wiki/IEEE_754) (_**float**ing point numbers_) ressemblent à des nombres décimaux, mais n'en sont pas du tout !

#### Les choses simples avec les flottants

- Le point est le séparateur décimal du nombre affiché.
- Ces nombres sont stockés en binaire (et non en décimal) avec une précision un peu meilleure qu'avec une calculatrice, mais pas arbitraire non plus.
- On peut entrer directement un nombre en écriture scientifique en utilisant la notation [e](https://en.wikipedia.org/wiki/Scientific_notation#E-notation)
  - exemple : `-1.602e-19` pour $-1,602 \times 10^{-19}$, la charge en coulomb d'un électron.
  - **Attention**, le nombre stocké sera l'approximation binaire du nombre décimal entré, et sera souvent différent !

```python
In [7]: from math import pi

In [8]: pi / 2
Out[8]: 1.5707963267948966

In [9]: 1.2**1000
Out[9]: 1.5179100891722457e+79

In [10]: 7.3 + 2
Out[10]: 9.3

In [11]: 21 / 3
Out[11]: 7.0

In [12]: 18 / 6.02e23
Out[12]: 2.990033222591362e-23
```

> Une approximation de $\frac \pi 2$ donnée avec une quinzaine de chiffres décimaux significatifs.
> La [division](https://fr.wikipedia.org/wiki/Division) entre flottants s'obtient avec l'opérateur `/`
> Un calcul d'une puissance d'un flottant. Le résultat est donné en écriture scientifique $\approx 1,\!5179\times10^{79}$
> On peut mélanger un entier et un flottant  dans une opération, l'entier sera d'abord converti en flottant avant le calcul.
> Si on utilise l'opérateur `/`, les opérandes entières sont converties en flottant avant le calcul, et le résultat sera un flottant, même si la division entière a un reste nul.
> Le dernier exemple donne [le calcul du volume moyen d'une molécule d'eau](https://en.wikipedia.org/wiki/Avogadro_constant) en ml, soit environ  30 Å^3^.

#### Les points plus délicats

On retrouve comme sur de nombreuses calculatrice (et c'est normal) les points suivants :

- Il existe des limites aux nombres flottants, avec un plus petit flottant strictement positif, un plus grand flottant positif, et de même avec les négatifs.
- Le nombre affiché (un décimal) n'est souvent pas égal au nombre représenté en machine, et parfois différent du nombre entré au départ !
- Pour simplifier, il y a, en gros, une quinzaine de chiffres significatifs, et des exposants entre -1000 et +1000, environ.

```python
In [13]: 0.5**1000
Out[13]: 9.332636185032189e-302

In [14]: 0.5**2000
Out[14]: 0.0

In [15]: 2.0**1000
Out[15]: 1.0715086071862673e+301

In [16]: 2.0**2000
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

OverflowError: (34, 'Numerical result out of range')
```

> La première opération donne un résultat très petit.
> La deuxième, tellement petit, qu'il est arrondi à exactement zéro.
> La troisième donne un résultat très grand, écrit en écriture scientifique.
> La quatrième provoque une erreur, le résultat étant trop grand. Notons que `2**2000` ne provoque pas d'erreur ; c'est un entier qui, lui, dispose de toute la mémoire de l'ordinateur et pourrait être bien plus grand encore sans perdre de précision.

#### Les points techniques

À aborder en seconde lecture.
> [La cinquième va vous étonner.](http://www.legorafi.fr/2017/10/17/7-proverbes-de-sagesse-chinoise-que-nous-navons-pas-su-traduire/)

```python
In [17]: 0.1 + 0.2 == 0.3
Out[17]: False
```

> - $0.1$ est stocké en machine par un nombre qui n'est pas exactement égal à $0.1$, mais par un nombre en binaire très proche. De même pour $0.2$ et $0.3$.
> - Le test d'égalité est réalisé sur les nombres binaires, pas sur les nombres affichés en décimal !
> - Une calculatrice a normalement le même comportement, sauf si elle travaille avec les nombres réellement décimaux (sauf bug).

Ci-dessous deux calculatrices ayant apparemment la même version de *MicroPython*.

@import "assets/Mathice1a.jpeg" {height="200px" title="Casio 35+" alt="MicroPython mis à jour"}
@import "assets/Mathice2.png" {height="200px" title="Casio 90+" alt="MicroPython buggé"}

Pourtant, celle de droite (réponse *True*) se trompe. L'erreur a probablement été corrigée. La bonne réponse, étonnante certes, est *False*.

Regardons comment obtenir le type d'un objet.

```python
In [18]: type(1)
Out[18]: int

In [19]: type(1.)
Out[19]: float

In [20]: 1. is 1
Out[20]: False

In [21]: 1. == 1
Out[21]: True
```

> :fa-bolt: Explication
>
> - `1` est de type entier, (*<b>int</b>eger*)
> - `1.` ou bien `1.0` est de type flottant, (*<b>float</b>ing point number*)
> - Ce **ne sont pas** les mêmes objets en interne pour Python. *is* répond alors *False* pour faux.
> - À la comparaison, il se passe un phénomène de changement de type (transtypage). Pour être comparé à un flottant, un entier est automatiquement changé en flottant. Et là, la comparaison s'avère égale, donc le test d'égalité renvoie *True* (pour vrai). Nous avons aussi évoqué ce phénomène pour une opération entre un flottant et un entier.

Les opérateurs de Python travaillent avec différents objets, de type différent. En fonction du type utilisé, l'opération effective sera différente. Ainsi, on retrouvera les opérateurs `+` `-` `*` `**` `<` `<=` `==` `<>` `!=` `>=` `>` qui fonctionnent aussi avec les flottants. On y ajoute `/` pour la division, faite entre flottants (ou complexes).

> Pour ceux qui savent ce qu'est un nombre complexe, les mêmes opérateurs fonctionnent avec les nombres complexes. Si une opérande est complexe, alors l'autre est transtypée avant calcul en complexe.

```python
In [22]: 0.1 + 0.0045
Out[22]: 0.1045

In [23]: 5.4 + 2.7
Out[23]: 8.100000000000001

In [24]: 5,4 + 2,7
Out[24]: (5, 6, 7)
```

- Le premier exemple montre ce qu'il se passe fréquemment : l'affichage décimal de la somme de deux représentations binaires de flottants (issus de décimaux) est égal à la somme des décimaux d'origine. *Cette phrase était complexe ; reformulons*. Dit autrement : l'addition de deux décimaux, provoque en machine l'addition de deux nombres binaires qui ne sont pas égaux aux décimaux, mais la somme calculée (qui sera un nombre en binaire) peut s'écrire souvent en décimal comme la somme des décimaux d'origine.
- Dans le second exemple, on constate que ce n'est pas une généralité.
- Dans le troisième exemple, Python a affiché les trois éléments d'un *tuple*, le second étant 4+2, égal à 6. Nous verrons les tuples plus tard. Ici, il n'y a pas d'erreur à l'exécution, on parlera éventuellement d'erreur sémantique.

#### :fa-key: Nombre de particules dans l'Univers visible
Une introduction aux variables en *Python* !

Cet exercice résolu a pour but de montrer quelques bonnes pratiques et possibilités.

- On utilise des noms de variables longs.
- On peut utiliser les écritures scientifiques.

---

On fera les approximations suivantes :

- notre Soleil est une étoile moyenne, de masse 2×10^33^ g.
- un proton (constituant essentiel des étoiles) a une masse de 1,7×10^-24^ g.
- Notre propre Galaxie (la Voie Lactée, une galaxie moyenne) contient environ 100 milliards d'étoiles.
- La masse d'une galaxie provient essentiellement des étoiles.
- On estime à mille milliards le nombre de galaxies de l'Univers visible.

> Quel est l'estimation du nombre de protons de l'Univers visible ?

---

Une solution :

```python
In [29]: masse_soleil = 2e33

In [30]: masse_proton = 1.7e-24

In [31]: nb_proton_par_étoile = masse_soleil / masse_proton

In [32]: nb_étoile_par_galaxie = 100e9

In [33]: nb_proton_par_galaxie = nb_proton_par_étoile * nb_étoile_par_galaxie

In [34]: nb_galaxie_de_Univers = 1000e9

In [35]: nb_proton_de_Univers = nb_proton_par_galaxie * nb_galaxie_de_Univers

In [36]: nb_proton_de_Univers
Out[36]: 1.1764705882352941e+80

In [37]: f"Il y a environ {nb_proton_de_Univers:.2e} protons dans l'Univers visible."
Out[37]: "Il y a environ 1.18e+80 protons dans l'Univers visible."
```

> **Commentaires :**
>
> - Nous voyons l'intérêt d'utiliser des variables avec un nom qui a du sens. C'est l'objet de notre prochaine partie. En mathématiques, on utilise souvent des variables à une lettre, parfois d'un autre alphabet, parfois indicée. Cette pratique est à bannir en *Python*.
> - La dernière instruction montre une façon moderne d'afficher les variables au sein de texte formaté, les *f-string*. **Il faudra d'abord étudier les chaînes de caractères simples**. La précision à trois chiffres significatifs n'est donnée uniquement que pour montrer la syntaxe. Raisonnablement la réponse étant un ordre de grandeur comparable à 10^80^.
