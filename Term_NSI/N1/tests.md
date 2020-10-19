# [Tests et conditions](http://www.france-ioi.org/algo/chapter.php?idChapter=646)

> Correction alternative de certains problèmes

## Bornes kilométriques

### Sujet

 Votre programme doit lire deux entiers, correspondant à deux numéros de bornes kilométriques, et il doit afficher la distance séparant ces deux bornes. Notez que le résultat doit être un nombre positif ou nul.
### Exemples
#### Exemple 1

entrée :

    152
    189

sortie :

    37

#### Exemple 2

entrée :

    814
    786

sortie :

    28

### Solution officielle

```python
numéroMatin = int(input())
numéroSoir = int(input())
écart = numéroSoir - numéroMatin
if écart < 0:
   écart = -écart
print(écart)
```

### Solution alternative

Avec la fonction `abs` : valeur absolue.

```python
numéro_matin = int(input())
numéro_soir = int(input())
écart = abs(numéro_soir - numéro_matin)
print(écart)
```

