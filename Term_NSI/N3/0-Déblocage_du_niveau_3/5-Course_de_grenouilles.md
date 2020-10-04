# [Course de grenouilles](http://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2279)


Il existe de nombreuses traditions étranges et amusantes sur Algoréa, la grande course de grenouilles annuelle en fait partie. Il faut savoir que les grenouilles algoréennes sont beaucoup plus intelligentes que les grenouilles terrestres et peuvent très bien être dressées pour participer à des courses. Chaque candidat a ainsi entraîné sa grenouille durement toute l'année pour ce grand événement.

La course se déroule en tours et, à chaque tour, une question est posée aux dresseurs. Le premier qui trouve la réponse gagne le droit d'ordonner à sa grenouille de faire un bond. Dans les règles de la course de grenouilles algoréennes, il est stipulé que c'est la grenouille qui restera le plus longtemps en tête qui remportera la victoire. Comme cette propriété est un peu difficile à vérifier, le jury demande votre aide.

## Ce que doit faire votre programme :

`nbGrenouilles` numérotées de `1` à `nbGrenouilles` sont placées sur une ligne de départ. À chaque tour, on vous indique le numéro de la seule grenouille qui va sauter lors de ce tour, et la distance qu'elle va parcourir en direction de la ligne d'arrivée.

Écrivez un programme qui détermine laquelle des grenouilles a été strictement en tête de la course au début du plus grand nombre de tours. Notez que comme on s'intéresse à qui est en tête au début de chaque tour, le bond du dernier tour ne sert à rien car même si la grenouille concernée passe en tête, la course est finie (il est purement honorifique selon la tradition algoréenne).

### Contraintes

* `1 <= nbGrenouilles <= 100`
* `1 <= nbTours <= 1000`
* `1 <= distanceSauti <= 100`

### Entrée

La première ligne de l'entrée contient un entier, le nombre de grenouilles `nbGrenouilles` qui participent à la course. Les grenouilles sont numérotées de `1` à `nbGrenouilles`.

La deuxième ligne de l'entrée contient le nombre de tours `nbTours` de la course.

Chacune des `nbTours` lignes suivantes décrit un tour par deux entiers séparés par un espace. Le premier entier est le numéro de la grenouille qui saute à ce tour, et le deuxième, est la distance parcourue par la grenouille lors de ce saut.

### Sortie

Vous devez afficher un entier sur la sortie : le numéro de la grenouille qui a été strictement en tête au début du plus grand nombre de tours. En cas d'égalité entre plusieurs grenouilles, choisissez celle dont le numéro est le plus petit.

### Exemple

entrée :

    4
    6
    2 2
    1 2
    3 3
    4 1
    2 2
    3 1

sortie :

    2

### Commentaires

Pour l'exemple proposé, indiquons la distance totale parcourue par chaque grenouille au début de chaque tour :

    Grenouille : 1 2 3 4
    Tour 1 :     0 0 0 0
    Tour 2 :     0 2 0 0
    Tour 3 :     2 2 0 0
    Tour 4 :     2 2 3 0
    Tour 5 :     2 2 3 1
    Tour 6 :     2 4 3 1

La grenouille 1 est restée 0 tour strictement en tête, la seconde 2 (les tours 2 et 6), la troisième 2 (les tours 4 et 5) et la quatrième 0. C'est donc la grenouille 2 qui remporte la victoire.

## Solution

```python
def grenouille_tête():
    """Renvoie l'indice entre 0 et nb_grenouilles-1
        de la grenouille seule en tête,
        None sinon, si elle n'est pas seule.
    """
    d_max = -1
    for i in range(nb_grenouilles):
        if dist_parcourue[i] == d_max:
            seule = False
        elif dist_parcourue[i] > d_max:
            d_max = dist_parcourue[i]
            seule = True
            championne = i
    if seule:
        return championne
    else:
        return None

def meilleure_grenouille():
    """Renvoie l'indice entre 1 et nb_grenouille
    de la grenouille ayant le meilleur score,
    en cas d'égalité, le + petit indice
    """
    score_max = 0
    gagnante = 0 # indice entre 0 et nb_grenouilles-1
    for i in range(nb_grenouilles):
        if score[i] > score_max:
            score_max = score[i]
            gagnante = i 
    return gagnante + 1 # indice entre 1 et nb_grenouilles

nb_grenouilles = int(input())
dist_parcourue = [0] * nb_grenouilles
score = [0] * nb_grenouilles
nb_tours = int(input())
for _ in range(nb_tours):
    # pour chaque tour
    championne = grenouille_tête()
    if championne is not None:
        score[championne] += 1
    i_grenouille, distance = map(int, input().split())
    dist_parcourue[i_grenouille-1] += distance
print(meilleure_grenouille())
```

