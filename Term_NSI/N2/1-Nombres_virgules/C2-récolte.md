# Une belle récolte

## Sujet

 Votre programme doit commencer par lire un entier nbPersonnes puis un entier nbFruits. Il doit ensuite afficher "oui" si nbFruits est un multiple de nbPersonnes, et "non" dans le cas contraire.

### Exemple

entrée :

    12
    156

sortie :

    oui

### Solution officielle

```python
nbPersonnes = int(input())
nbFruits = int(input())
if (nbFruits % nbPersonnes) == 0:
   print("oui")
else:
   print("non")
```

### Solution alternative

* On stocke le résultat `est_multiple` dans un booléen ;
* on utilise l'opérateur ternaire pour factoriser le `print` dans notre code.

```python
nb_personnes = int(input())
nb_fruits = int(input())
est_multiple = (nb_fruits % nb_personnes == 0) # un booléen
print("oui" if est_multiple else "non")
```
