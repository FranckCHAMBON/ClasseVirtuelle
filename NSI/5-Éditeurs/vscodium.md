# VSCodium {ignore}

Visual Studio Code est un éditeur libre pour ordinateur, très complet, produit par Microsoft, mais qui inclut de la télémétrie (une sorte de mouchard). On peut certes la désactiver, mais par principe, nous ne pouvons pas recommander ces pratiques, surtout avec le risque induit par certaines extensions qui ne sont pas libres.

[VSCodium](https://vscodium.com/) est une version de Visual Studio Code **sans télémétrie**, et distribuée avec une licence libre (MIT) qui est bien plus respectueuse.

D'autre part, on peut ajouter des extensions ; il y a un point délicat.
* Le *MarketPlace* de Visual Studio Code contient des extensions libres, mais aussi d'autres qui ne le sont pas, et qui peuvent inclure de la télémétrie également... Nous ne pouvons pas le recommander.
* Le *MarketPlace* de **VSCodium ne contient que des extensions libres**, ce qui permet de pouvoir le recommander sereinement.

## Sommaire {ignore}

[TOC]

## Installation

VSCodium est multiplateforme, il suffit de suivre les indications proposées sur le site officiel.
Ci-dessous, une traduction rapide.

### Windows

> Cette section est non testée par votre professeur.

Il existe plusieurs gestionnaires de paquets pour Windows.

#### Avec *Windows Package Manager (WinGet)*
1. À partir de Windows 10 1709 (build 16299), on peut installer le [App Installer](https://www.microsoft.com/en-us/p/app-installer/9nblggh4nns1?activetab=pivot:overviewtab)

2. Ensuite, on peut installer VSCodium avec :
```bash
winget install vscodium 
```

#### Avec *Chocolatey*
1. Installer [Chocolatey](https://chocolatey.org/), si ce n'est pas déjà fait.
2. Ensuite, on peut installer VSCodium avec :
```bash
choco install vscodium 
```

### Mac OS
> Cette section est non testée par votre professeur.

1. Il vous faut avoir le gestionnaire de paquet [Homebrew](https://brew.sh/index_fr), qui s'installe (si ce n'est pas déjà fait) sur votre Mac, dans un terminal, avec :
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Ensuite, on peut installer VSCodium avec :
```bash
brew install --cask vscodium 
```

### Linux (Debian)
1. Ajouter la clé GPG du dépôt
```bash
wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/etc/apt/trusted.gpg.d/vscodium.gpg 
```
2. Ajouter le dépôt
```bash
echo 'deb https://paulcarroty.gitlab.io/vscodium-deb-rpm-repo/debs/ vscodium main' | sudo tee --append /etc/apt/sources.list.d/vscodium.list 
```
3. Mettre à jour et installer
```bash
sudo apt update && sudo apt install codium 
```

## Premier démarrage

```bash
cd ~
mkdir test_vscodium
cd test_vscodium
codium .
```

Dans un terminal Bash,
1. Nous sommes aller à la racine de l'utilisateur,
2. Nous avons créé un nouveau dossier,
3. et y sommes entré,
4. ensuite nous avons ouvert VSCodium dans ce dossier.


![Premier démarrage](assets/1-initial.png)

### Quelques réglages

TODO

## Extensions utiles en NSI

Au premier démarrage de VSCodium, on peut aller dans le gestionnaire d'extensions avec (<kbd>Ctrl</kbd>+<kbd>Maj</kbd>+<kbd>X</kbd>).

### Menus en français

Pour franciser VSCodium :
1. Rechercher `french`
2. Installer [`French Language Pack for VS Code`](https://open-vsx.org/extension/MS-CEINTL/vscode-language-pack-fr)

> Installation automatique via Bash
```bash
codium --install-extension ms-ceintl.vscode-language-pack-fr
```

### Correction orthographique et grammaticale

1. Rechercher et installer [`LTeX`](https://open-vsx.org/extension/valentjn/vscode-ltex)
2. LTeX devrait être automatiquement configuré en français, sinon
    1. Une fois installée, cliquer sur la roue dentée (paramètres d'extensions)
    2. Dérouler vers le bas, et chercher la section `Ltex: language`
    3. Dans le menu déroulant, choisir `fr` pour `french`.

> Installation automatique via Bash
```bash
codium --install-extension valentjn.vscode-ltex
```


### Enjoliveurs
1. Chercher et installer l'extension `Material Icon Theme` ; pour des icônes de fichier.
2. Chercher et installer l'extension `Bracket Pair Colorizer 2` ; pour mieux voir vos parenthèses.


### Python
Rechercher `Python` et installer l'extension de Microsoft. Ceci n'installe pas Python mais fera le lien entre Python déjà installé et VSCodium.

Une fois installée, vous pouvez tester.
1. Créer un fichier `test.py` de type Python.
2. En bas, à gauche, devrait être affiché votre version de python.
3. Éditer `print("Salut à tous !")`
4. Appuyer sur (<kbd>Ctrl</kbd>+<kbd>F5</kbd>)
5. Une fenêtre devrait s'ouvrir, avec le résultat attendu de votre script.

### Meilleure indentation avec Python

Rechercher et installer l'extension `Python Indent`

### Données en table (`.csv`)
En première, on manipule des fichiers `.csv`, et on peut faire aussi les toutes premières expériences de SQL.

Rechercher et installer l'extension `Rainbow CSV`

### Langage SQL
En terminale, on fait une initiation au langage `SQL`

Rechercher et installer l'extension `SQLite`

Rechercher et installer l'extension `ERD Editor`

### Variées

* Ouvrir un fichier avec une extension particulière, puis le gestionnaire d'extensions. Par exemple un fichier de sous-titres.
    * Le gestionnaire propose des extensions adaptées, comme : `Subtitles Editor`


## Extensions utiles pour le professeur

### Complétion automatique de noms de fichier

Rechercher et installer l'extension `Path Autocomplete` ; pour compléter automatiquement les noms de fichiers.

### Markdown
Pour créer des pages HTML grâce au langage Markdown, et visualiser en direct le rendu HTML.

Rechercher et installer l'extension `Markdown Preview Enhanced`

### Langage HTML
Pour prévisualiser en direct votre rendu HTML/JavaScript.

Il faut avoir le navigateur `Chromium` déjà installé.


Rechercher et installer l'extension `Browser Preview`


### Édition de documents LaTeX

Rechercher et installer l'extension `LaTeX Workshop`


### Autres extensions Python

* `Pyright` ; pour le typage statique, entre autres...

## Compléments sur les extensions

### Installer une extension qui n'est pas (encore) sur le MarketPlace libre.

TODO