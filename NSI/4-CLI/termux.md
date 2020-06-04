# Utilisation de Termux

## Installation
* via F-Droid :
* via play-Store :

## Premier lancement

On arrive sur une invite de commande bash.
```bash
$
```

### Mise à jour des dépôts de paquets.

```bash
pkg update
```

### Mise à jour des paquets

```bash
pkg upgrade
```

### Installation de paquets

#### Pour Python

L'interpréteur du langage s'obtient avec :

```bash
pkg install python
```

#### Éditeurs de code

##### Éditeur Nano

```bash
pkg install nano
```

##### Éditeur Micro

```bash
pkg install micro
```

#### Pour jouer

##### `cowsay`

```bash
pkg install cowsay
```

Utilisation :

```bash
$ cowsay "Bonjour  tous"
 ______________
< Bonjour tous >
 --------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
$
```

##### `figlet`

```bash
pkg install figlet
```

Utilisation :

```bash
$ figlet "NSI a Aubrac"
 _   _ ____ ___              _         _
| \ | / ___|_ _|   __ _     / \  _   _| |__  _ __ __ _  ___
|  \| \___ \| |   / _` |   / _ \| | | | '_ \| '__/ _` |/ __|
| |\  |___) | |  | (_| |  / ___ \ |_| | |_) | | | (_| | (__
|_| \_|____/___|  \__,_| /_/   \_\__,_|_.__/|_|  \__,_|\___|

$
```

##### `cmatrix`

```bash
pkg install cmatrix
```

Utilisation :

```bash
$ cmatrix
```

#### Pour travailler

##### Presse-papier
Pour travailler avec le presse-papier ; et faire de copier-coller.

```bash
pkg install xclip
```

> À savoir : pour copier à partir de la tablette, il faut laisser le doigt appuyé jusqu'à avoir le menu de sélection du texte et de copie.

##### `git` contrôle de version

```bash
pkg install git
```

> **Objectif** : pourvoir travailler avec ses fichiers en ligne sur github ou sur gitlab...

##### Outils variés

```bash
pkg install coreutils
```

> Exemple d'utilisation

Pour obtenir la factorisation d'un entier :

```bash
factor 1234567890000007
```

```
1234567890000007: 23 6427 79151 105517
```

###### Enregistrement de session terminal

```bash
pkg install asciinema
```

> Exemple d'utilisation

```bash
asciinema rec votre_fichier.cast
```
