# :grapes: Tas binaire {ignore=true}

## Sommaire {ignore=true}

[TOC]

On considère des arbres binaires particuliers, avec des données toutes de même type, un type qui possède une relation d'ordre. Par exemple : des entiers, on peut les comparer.

## Définition

Un **tas binaire** (ou **tas-max**) est un arbre binaire presque complet à gauche, tel que :
* le nœud racine porte une donnée supérieure ou égale à celle des autres nœuds ;
* ses deux sous-arbres sont aussi des tas.

Un **tas-min** est une structure équivalente mais avec la racine portant une valeur inférieure ou égale à celles de sa filiation.

> La structure de tas binaire est utilisée dans un algorithme de tri efficace (le tri par tas), dans la gestion des files de priorité.

### Exemple

```dot
digraph expression
{
    label = "Tas-max"
    "1" [label="10"];

    "2" [label="8"];
    "3" [label="4"];
    "1" -> "2" ;
    "1" -> "3" ;

    "4" [label="5"];
    "5" [label="6"];
    "2" -> "4" ;
    "2" -> "5" ;

    "6" [label="2"];
    "7" [label="1"];
    "3" -> "6" ;
    "3" -> "7" ;

    "8" [label="4"];
    "9" [label="2"];
    "4" -> "8" ;
    "4" -> "9" ;

    "10" [label="3"];
    "11" [label="",shape=plaintext];
    "5" -> "10" ;
    "5" -> "11" [style=dashed, arrowhead=none];
}
```


```dot
digraph expression
{
    label = "Tas-min"
    "1" [label="1"];

    "2" [label="2"];
    "3" [label="5"];
    "1" -> "2" ;
    "1" -> "3" ;

    "4" [label="2"];
    "5" [label="3"];
    "2" -> "4" ;
    "2" -> "5" ;

    "6" [label="6"];
    "7" [label="10"];
    "3" -> "6" ;
    "3" -> "7" ;

    "8" [label="4"];
    "9" [label="8"];
    "4" -> "8" ;
    "4" -> "9" ;

    "10" [label="4"];
    "11" [label="",shape=plaintext];
    "5" -> "10" ;
    "5" -> "11" [style=dashed, arrowhead=none];
}
```

