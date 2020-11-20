# [Affichage de texte, suite d'instructions](http://www.france-ioi.org/algo/chapter.php?idChapter=642)

> Correction alternative de certains problèmes

## Plan de la montagne

### Sujet

Pour vous aider à mener votre parcours vers le haut de la montagne, les villageois vous donnent quelques indications. Plutôt que de les mémoriser, vous décidez d'utiliser votre robot pour les imprimer sur un bout de papier.

> Ce que doit faire votre programme :

Écrivez un programme qui affiche exactement le texte qui suit :

    Tout droit tu grimperas,
    La clé tu trouveras,
    Habile tu seras,
    Quand tu les porteras,
    Et avec le chef tu reviendras !



### Solution officielle

```python
print("Tout droit tu grimperas,")
print("La clé tu trouveras,")
print("Habile tu seras,")
print("Quand tu les porteras,")
print("Et avec le chef tu reviendras !")
```

### Solutions alternatives

On peut afficher le texte demandé en une seule instruction, au lieu de quatre.

1. On peut utiliser `"""` pour délimiter une grande chaîne contenant des sauts de ligne.

```python
print("""Tout droit tu grimperas,
La clé tu trouveras,
Habile tu seras,
Quand tu les porteras,
Et avec le chef tu reviendras !""")
```

2. On peut utiliser `\n` pour insérer les sauts de ligne.

```python
print("Tout droit tu grimperas,\nLa clé tu trouveras,\nHabile tu seras,\nQuand tu les porteras,\nEt avec le chef tu reviendras !")
```

