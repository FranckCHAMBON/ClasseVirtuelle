# Listes chaînées

On va utiliser deux classes :
* Une classe `Maillon` qui contient un élément et le suivant dans la liste.
* Une classe `Liste` qui contient un maillon de tête et les méthodes pour la faire vivre.

On commence par construire les méthodes analogues à une pile, ensuite on complètera en deque.

## Première approche, implémenter la pile

```python
class Maillon:
    def __init__(self, élément, suivant):
        self.élément = élément
        self.suivant = suivant

    def __str__(self):
        return str(self.élément)


class Liste:
    def __init__(self):
        self.droite = None
    
    def est_vide(self):
        return self.droite is None
    
    def ajout_droite(self, élément):
        self.droite = Maillon(élément, self.droite)

    def extrait_droite(self):
        if self.est_vide():
            raise ValueError("Liste vide")
        maillon = self.droite
        self.droite = maillon.suivant
        return maillon.élément
    
    def __str__(self):
        affichage = "Contenu : "
        maillon = self.droite
        while maillon is not None:
            affichage += str(maillon) + "::"
            maillon = maillon.suivant
        affichage += " fin."
        return affichage
```

**Exercice 1** : compléter la classe pour obtenir les méthodes de la deque.