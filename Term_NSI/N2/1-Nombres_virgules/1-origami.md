# Origami

## Sujet

L'épaisseur d'une feuille de papier est de 110 micromètres c'est à dire 0,110 millimètres. Si on la plie 15 fois sur elle-même et que l'épaisseur double à chaque fois, quelle sera l'épaisseur finale si on l'exprime en centimètres ? Votre programme devra calculer et afficher cette valeur (qui n'est pas forcément entière).

## Solution officielle

```python
epaisseur = 0.11
for loop in range(15):
    epaisseur = epaisseur * 2
print(epaisseur / 10)
```

## Solution alternative

On indique les unités en commentaires, et on utilise la puissance.

```python
épaisseur = 0.110 # en mm
épaisseur *= 2 ** 15 # multiplié par 2 à la puissance 15
print(épaisseur / 10) # en cm
```

