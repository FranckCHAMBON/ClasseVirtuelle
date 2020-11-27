# DS1 - Exercice 1
Écrire un script qui affiche :
    42000 41000 40000 ... 3000 2000 1000 Fini

Votre script devra être écrit soigneusement.

## Correction

On propose ici trois possibilités ; il en existe encore d'autres...

### Avec boucle `while`

```python
nombre = 42000
while nombre > 0:
    print(nombre, end=" ")
    nombre = nombre - 1000
print("Fini")
```

### Avec `range` à un paramètre

```python
nombre = 42000
for loop in range(42):
    print(nombre, end=" ")
    nombre = nombre - 1000
print("Fini")
```

### Avec `range` à trois paramètres

```python
for nombre in range(42000, 0, -1000):
    print(nombre, end=" ")
print("Fini")
```
