# Construire et utiliser ses *doctest*

* Lire rapidement la [documentation](https://docs.python.org/fr/3/library/doctest.html)

## Version simpliste

Une fois vos *doctest* écrits, ajouter ceci à la fin de vos déclaration de fonction :
```python
import doctest
doctest.testmod()
```
Et lancer votre code.
> Une absence de message signifie que les tests sont bons.


---

*À suivre*
