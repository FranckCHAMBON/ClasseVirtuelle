# DM de l'élève



## Épreuve régionale


### 42

@import "./E1.py"

#### Commentaires de correction

TB.



### Escalier

@import "./E2.py"

#### Commentaires de correction

TB.



### Grand écart

@import "./E3.py"

#### Commentaires de correction

TB.



### Initiales

@import "./E4.py"

#### Commentaires de correction

Au lieu de passer une liste en paramètre, il vaut mieux la chaîne.
* C'est plus cohérent avec la longueur donnée aussi en paramètre.


### Mot le plus long

@import "./E5.py"

#### Commentaires de correction

Au lieu de passer une liste en paramètre, il vaut mieux la chaîne.
* C'est plus cohérent avec la longueur donnée aussi en paramètre.

`plus_long` : on peut faire mieux avec `plus_grande_longueur`.



### Nombres impairs

@import "./E6.py"

#### Commentaires de correction

OK, mais probablement mieux de renvoyer la liste des nombres, plutôt que l'affichage...
Cela permet un post traitement différent ; si on veut...



### Table de multiplication

@import "./E7.py"

#### Commentaires de correction

TB.
Ici, le *doctest* était pénible, et peu utile...



### Puissance 4

@import "./E8.py"

#### Commentaires de correction

`return (0 <= i <= 5) and (0 <= j <= 6)` est mieux pour `est_dans_grille`.


TB, sauf les lignes trop longues.
* Mettre les commentaires sur la ligne précédente,
* et ne pas dépasser 80 caractères...



### Puzzle

@import "./E9.py"

#### Commentaires de correction

Il faut faire un meilleur test pour faire déborder la pièce s'il n'y a que des zéros au bord... Les zéros ne comptent pas !!!




### Solitaire

@import "./E10.py"

#### Commentaires de correction

Voir commentaires précédents.

De plus `vecteurs` est mieux que `combinaison`.



### Anagrammes

@import "./E11.py"

#### Commentaires de correction

Bien, mais il y a plus simple pour avoir une signature de l'anagramme.
Plutôt qu'un dictionnaire qui compte le nombre de lettres, l'anagramme avec les lettres dans l'ordre alphabétique est une bonne signature ; plus simple à stocker, et pour comparer également.



### Plages du Pacifique

@import "./E12.py"

#### Commentaires de correction

Pour `est_dans_tableau`, voir les autres commentaires similaires !

Même avec les commentaires, le code est peu clair... Ça reste un beau travail d'initiation.



### Plan de métro

Non rendu.




## Qualification


## Cases inaccessibles

@import "./Q1.py"

#### Commentaires de correction

On ne comprend pas bien comment la récursivité s'arrête...
Sinon, c'est bien !!!



## Comparer des chaînes

@import "./Q2.py"

#### Commentaires de correction

C'est bien, tu n'as pas 'triché', mais il y avait plus simple.



## Les trois nombres

@import "./Q3.py"

#### Commentaires de correction

Bonne idée de jouer avec les indices. Tu aurais pu utiliser aussi les indices négatifs.
Voir corrigé.



## Nombre de voyelles

@import "./Q4.py"

#### Commentaires de correction

TB.

