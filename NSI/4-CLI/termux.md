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

## Créer un environnement virtuel Python

### Exemple pour TermtoSVG

Créer un environnement virtuel permet d'installer des paquets Python, accessibles uniquement pour certains projets et pas d'autres ; éviter les conflits de versions.

```bash
python3 -m venv .enregistrement
```

Cela crée une copie de Python que l'on peut modifier par l'ajout de paquets.

Pour activer cet environnement :

```bash
source .enregistrement/bin/activate
```

> On constate que le **prompt** est modifié pour indiquer qu'on est dans l'environnement.

Ensuite, on peut utiliser le gestionnaire de paquets Python : `pip`

#### Première utilisation

```bash
pip install --upgrade pip
```

Première mise à jour **très importante** du gestionnaire lui-même !

#### Quelques paquets à installer

* `pkg install clang`
* `pkg install libxml2 libxslt`

```bash
pip install termtosvg
```

> ⚠️ Un peu long sur tablette.


Un example d'utilisation :
```bash
termtosvg example.svg -t window_frame_js
```

* Le fichier de sortie est `example.svg`
* L'option `-t` sert à choisir un modèle de cadre pour le terminal, faire `termtosvg -h` pour d'autres options.

#### Pour sortir de l'environnement virtuel

```bash
deactivate
```

Cette commande repositionne à l'état précédent.

## Utilisation de MkDocs

> Objectif : créer un site web avec Python et markdown.

1. On crée un environnement virtuel `.web`

```bash
python3 -m venv .web
```

2. On l'active
```bash
source .web/bin/activate
```

3. On met à jour `pip` de cet environnement

```bash
pip install --upgrade pip
```

4. On installe MkDocs

```bash
pip install mkdocs
```
