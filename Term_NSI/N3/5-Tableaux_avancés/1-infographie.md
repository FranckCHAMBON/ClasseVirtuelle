# [Infographie](http://www.france-ioi.org/algo/task.php?idChapter=564&idTask=1792)


En infographie, lorsque l'on désire créer l'image associée à une scène 3D, il est nécessaire de dessiner les faces qui la composent dans le bon ordre. En effet, certaines faces en recouvrent d'autres et doivent donc être dessinées après ces dernières.

Vous travaillez sur un moteur de rendu simplifié pour lequel les faces à dessiner sont des rectangles dont les côtés sont parallèles aux bords de l'image. Vous connaissez l'ordre dans lequel ces faces rectangulaires doivent être dessinées ainsi que la couleur de chacun et souhaitez écrire un programme qui crée l'image tant attendue.

L'image a `nbLignes` lignes et `nbColonnes` colonnes. Les lignes sont indexées de `0` à `nbLignes - 1` et les colonnes de `0` à `nbColonnes - 1`. La couleur de chaque rectangle est définie par un caractère. Par défaut, chaque pixel est de la couleur `.`.

## Contraintes

* `1 <= nbLignes, nbColonnes <= 100`, le nombre de lignes et de colonnes de l'image.
* `0 <= nbRectangles <= 100`, le nombre de rectangles à dessiner.

## Entrée

* La première ligne de l'entrée contient deux entiers : `nbLignes` et `nbColonnes`.

La seconde ligne contient un unique entier : `nbRectangles`.

Les `nbRectangles` lignes suivantes contiennent chacune quatre entiers `iLig1`, `iCol1`, `iLig2` et `iCol2` décrivant les coordonnées des bords respectivement en haut, à gauche, en bas et à droite du rectangle considéré, ainsi qu'un caractère couleur indiquant la couleur du rectangle.

Les rectangles doivent être dessinés dans l'ordre dans lequel ils sont donnés en entrée.

## Sortie

Votre programme doit afficher `nbLignes` lignes de `nbColonnes` caractères chacune décrivant l'image obtenue.

## Exemple

---

entrée :

```
9 19
4
1 3 7 5 o
5 2 6 16 -
1 12 7 14 u
2 1 2 16 s
```

sortie :

```
...................
...ooo......uuu....
.ssssssssssssssss..
...ooo......uuu....
...ooo......uuu....
..----------uuu--..
..----------uuu--..
...ooo......uuu....
...................
```

## Solution

### Minimaliste

Cette solution est ce qu'il ne faut pas faire !
* Les variables ont des identifiants trop courts, peu expressifs.
* Le code n'est pas structuré, ni réutilisable.

```python
N, M = map(int, input().split())
T = [['.']*M for _ in range(N)]
for _ in range(int(input())):
    xa, ya, xb, yb, c = input().split()
    for i in range(int(xa), int(xb)+1):
        for j in range(int(ya), int(yb)+1):
            T[i][j] = c
for t in T:       
    print("".join(t))
```


### Avec POO

On écrit ici un code expressif qui sera réutilisable.

```python
class Image:
    """objet Image en couleur '.' et 'a', 's', ...
    avec méthodes pour dessiner un rectangle et affichage.
    """

    def __init__(self, nb_lignes, nb_colonnes):
        """l'image sera blanche, pleine de '.'
        """
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        self.__grille = [['.' for _ in range(nb_colonnes)]
                            for _ in range(nb_lignes)]
    
    def affiche(self):
        for ligne in self.__grille:
            print("".join(ligne))
    
    def remplit_rectangle(self, i1, j1, i2, j2, couleur: str):
        """Remplit l'image avec un rectangle
        + de sommets opposés (i1, j1) et (i2, j2),
        + avec la couleur donnée.
        """
        if not all(((0 <= i1 < self.__nb_lignes),
                    (0 <= j1 < self.__nb_colonnes),
                    (0 <= i2 < self.__nb_lignes),
                    (0 <= j2 < self.__nb_colonnes))):
            raise ValueError("Mauvais indice")
        if len(couleur) != 1:
            raise ValueError("couleur doit être un seul caractère")
                   
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                self.__grille[i][j] = couleur


nb_lignes, nb_colonnes = map(int, input().split())
image = Image(nb_lignes, nb_colonnes)

nb_rectangles = int(input())
for _ in range(nb_rectangles):
    t_i1, t_j1, t_i2, t_j2, couleur = input().split()
    i1, j1, i2, j2 = map(int, [t_i1, t_j1, t_i2, t_j2])
    image.remplit_rectangle(i1, j1, i2, j2, couleur)

image.affiche()
```

### Commentaires

Pour la lecture de la ligne qui donne les informations à dessiner, il y a quatre entiers puis un caractère. On ne peut pas faire `map(int, input().split())` en effet une erreur sera levée sur le dernier champ qui ne peut pas être un argument pour `int`.

Nous avons proposé deux méthodes.
1. `xa, ya, xb, yb, c = input().split()`, puis utilisation de `int(xa)` etc... ; le code n'est pas factorisé, on écrit 4 fois `int` !
2. Un code un plus clair, mais avec trois fois « quatre objets semblables », on pourra faire mieux.
```python
    t_i1, t_j1, t_i2, t_j2, couleur = input().split()
    i1, j1, i2, j2 = map(int, [t_i1, t_j1, t_i2, t_j2])
```

Pour faire mieux, c'est hors programme, une histoire de *unpack* de liste. On préfixe une variable avec `*` pour qu'elle se comporte comme une liste qui va absorber des éléments.

```python
    *début_param, couleur = input().split()
    i1, j1, i2, j2 = map(int, début_param)
```


