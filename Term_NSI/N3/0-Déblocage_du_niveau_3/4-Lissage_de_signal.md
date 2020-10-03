# [Lissage de signal](http://www.france-ioi.org/algo/task.php?idChapter=656&idTask=2278)

Votre robot dispose de nombreux récepteurs et enregistre tous les signaux qui l'entourent. Cependant vous avez remarqué que certains de ces signaux sont très bruités. Vous décidez donc d'écrire un programme qui atténue le bruit de ces signaux, en effectuant ce que l'on appelle un lissage.

Une opération de lissage d'une séquence de mesures (des nombres décimaux) consiste à remplacer chaque mesure sauf la première et la dernière, par la moyenne des deux valeurs qui l'entourent.

Par exemple, si l'on part de la séquence de mesures suivantes :

    1 3 4 5

On obtient après un lissage :

    1 2.5 4 5

Le premier et dernier nombre sont inchangés. Le deuxième nombre est remplacé par la moyenne du 1er et du 3e, soit (1+4)/2 = 2.5, et le troisième est remplacé par (3+5)/2 = 4.

On peut ensuite repartir de cette nouvelle séquence, et refaire un nouveau lissage, puis un autre sur le résultat, etc.
Votre programme doit calculer le nombre minimum de lissages successifs nécessaires pour s'assurer que la valeur absolue de la différence entre deux valeurs successives de la séquence finale obtenue ne dépasse jamais une valeur donnée, diffMax.

On vous garantit qu'il est toujours possible d'obtenir la propriété voulue en moins de 5000 lissages successifs.

## Contraintes

* `1 <= nbMesures <= 100`
* `0 <= diffMax <= 100.0`
* `-100.0 <= mesurei <= 100.0`

### Entrée

La première ligne de l'entrée contient un entier : `nbMesures`.

La deuxième ligne de l'entrée contient un nombre décimal : `diffMax`.

Chacune des `nbMesures` lignes suivantes contient une mesure, sous la forme d'un nombre décimal.

### Sortie

Vous devez afficher un entier sur la sortie : le nombre minimal de lissages nécessaire.

### Exemple

entrée :

    7
    1.120
    1.292
    1.343
    3.322
    4.789
    -0.782
    7.313
    4.212

sortie :

    13

### Commentaires
Explicitons les résultats (arrondis) obtenus à chaque passage pour l'exemple donné en entrée :

    Après 1  passage : 1.292    2.307   3.066   1.27    6.051   1.715   4.212  
    Après 2  passages: 1.292    2.179   1.7885  4.5585  1.4925  5.1315  4.212  
    Après 3  passages: 1.292    1.54025 3.36875 1.6405  4.845   2.85225 4.212  
    Après 4  passages: 1.292    2.33038 1.59037 4.10688 2.24637 4.5285  4.212  
    Après 5  passages: 1.292    1.44119 3.21863 1.91837 4.31769 3.22919 4.212  
    Après 6  passages: 1.292    2.25531 1.67978 3.76816 2.57378 4.26484 4.212  
    Après 7  passages: 1.292    1.48589 3.01173 2.12678 4.0165  3.39289 4.212  
    Après 8  passages: 1.292    2.15187 1.80634 3.51412 2.75984 4.11425 4.212  
    Après 9  passages: 1.292    1.54917 2.83299 2.28309 3.81418 3.48592 4.212  
    Après 10 passages: 1.292    2.0625  1.91613 3.32359 2.8845  4.01309 4.212  
    Après 11 passages: 1.292    1.60406 2.69304 2.40031 3.66834 3.54825 4.212  
    Après 12 passages: 1.292    1.99252 2.00219 3.18069 2.97428 3.94017 4.212  
    Après 13 passages: 1.292    1.64709 2.58661 2.48824 3.56043 3.59314 4.212  

On constate que le signal vérifie la propriété pour la première fois juste après le 13ème passage. 

## Solution

```python
def est_pas_lisse(mesures, diff_max):
    """Renvoie un booléen, vrai si deux termes consécutifs
    dans la liste 'mesures' ont un écart supérieur à 'diff_max'
    """
    return any(abs(mesures[x] - mesures[x+1]) > diff_max \
        for x in range(nb_mesures-1))
    
def lissage(t):
    """Renvoie la liste t lissée comme dans l'énoncé
    premier et dernier inchangés,
    les autres sont la moyenne des deux qui encadrent.
    """
    return [t[0]] + [(t[x-1] + t[x+1]) / 2 \
        for x in range(1, nb_mesures-1)] + [t[-1]]
    

nb_mesures = int(input())
diff_max = float(input())
mesures = [float(input()) for _ in range(nb_mesures)]

nb_passes = 0
while est_pas_lisse(mesures, diff_max):
    mesures = lissage(mesures)
    nb_passes += 1

print(nb_passes)
```

### Commentaires

* La fonction `est_pas_lisse` utilise la fonction `any` qui renvoie `True` si **au moins un** `True` est présent dans la liste donnée en paramètre. Il existe de même la fonction `all` qui renvoie `True` uniquement si **tous** les éléments de la liste sont égaux à `True`.