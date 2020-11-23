# Devoir surveillé n°2, terminale NSI

## Sujet

On souhaite avoir un programme qui donne la distance totale d'un trajet entre différents points du plan qui sont les adresses d'amis.

Donner un programme en Python pour réaliser cette tache.

### Description de l'entrée - sortie

L'entrée est donnée par :
* Un entier `nb_amis` qui donne le nombre d'amis à visiter, ou pas.
* Ensuite, il y a `nb_amis` lignes comportant 3 champs : `prénom`, `abscisse` et `ordonnée`, qui renseignent les coordonnées (flottant) d'un ami. *Les amis ont tous un prénom différent qui est composé de caractères sans espace.*
* Ensuite, il y a `nb_lieux` un entier ; le nombre de lieux à visiter.
* Ensuite, il y a `nb_lieux` lignes comportant un `prénom` d'ami à visiter.

En sortie, on voudrait la distance totale du parcours, arrondie à 2 chiffres après la virgule.

### Exemple

entrée

    3
    Fred 5.0 6.0
    Marie -2.0 6.0
    Sophie 5.0 6.0
    2
    Marie
    Sophie

sortie

    7.0