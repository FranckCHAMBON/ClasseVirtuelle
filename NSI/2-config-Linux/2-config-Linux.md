<!-- slide -->

# Première configuration de *Linux*

Avec l'exemple de *Linux Mint* LMDE 4

<!-- slide vertical=true -->

On supposera qu'une installation toute fraîche vient d'être réalisée. Nous allons :

1. choisir les dépôts pour les sources ;
2. effectuer les mises à jour du système ;
3. installer de nouveaux logiciels.

> Nous verrons comment faire à la souris, mais aussi en ligne de commande.

<!-- slide -->

## Les sources
On peut modifier le choix des serveurs qui offrent les mises à jour. On choisit en général un dépôt proche, ayant un bon débit, et fiable dans le temps.


```bash
francky@debianmintvirtuel:~$ cat /etc/apt/sources.list.d/official-package-repositories.list 
```
```
deb http://packages.linuxmint.com debbie main upstream import backport #id:linuxmint_main

deb https://deb.debian.org/debian buster main contrib non-free
deb https://deb.debian.org/debian buster-updates main contrib non-free
deb http://security.debian.org buster/updates main contrib non-free

deb https://deb.debian.org/debian buster-backports main contrib non-free
```

https://wiki.debian.org/fr/SourcesList#Modifier_les_sources_de_logiciels

<!-- slide -->

<object type="image/svg+xml" data="sortie.svg"></object>
