# Achat de livres

## Sujet

 Votre programme doit commencer par lire la somme d'argent dont vous disposez et lira ensuite le prix d'un livre. Il devra ensuite afficher un entier, le plus grand nombre de livres qu'il vous est possible d'acheter avec cette somme d'argent.

### Exemple

entrée :

    27
    5

sortie :

    5

### Solution officielle

```python
sommeArgent = int(input())
prixLivre = int(input())
print(sommeArgent // prixLivre)
```

### Solution alternative

```python
argent_disponible = int(input()) # en €
prix_1livre = int(input()) # en €
nb_livres = argent_disponible // prix_1livre
print(nb_livres)
```
