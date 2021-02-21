# VSCodium {ignore}

Visual Studio Code est un éditeur libre pour ordinateur, très complet, produit par Microsoft, mais qui inclus de la télémétrie (une sorte de mouchard). On peut certes la désactiver, mais par principe, nous ne pouvons pas recommander ces pratiques.

[VSCodium](https://vscodium.com/) est une version de Visual Studio Code **sans télémétrie**, et distribuée avec une licence libre (MIT) plus respectueuse de l'esprit *Open Source*.

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

## Extensions utiles en NSI

Au premier démarrage de VSCodium, on peut aller dans le gestionnaire d'extensions avec (<kbd>Ctrl</kbd>+<kbd>Maj</kbd>+<kbd>X</kbd>).

### Menus en français

Pour franciser VSCodium :
1. Rechercher `french`
2. Installer `French Language Pack for VS Code` de `Microsoft`, sous licence MIT.

### Correction orthographique et grammaticale

1. Rechercher et installer `LTeX`
2. Une fois installée, cliquer sur la roue dentée (paramètres d'extensions)
3. Dérouler vers le bas, et chercher la section `Ltex: language`
4. Dans le menu déroulant, choisir `fr` pour `french`.

### Enjoliveurs
1. Chercher et installer l'extension `Material Icon Theme` ; pour des icônes de fichier.
2. Chercher et installer l'extension `Path Autocomplete` ; pour compléter automatiquement les noms de fichiers.
3. Chercher et installer l'extension `Bracket Pair Colorizer 2` ; pour mieux voir vos parenthèses.


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

### Variées

* Ouvrir un fichier avec une extension particulière, puis le gestionnaire d'extensions. Par exemple un fichier de sous-titres.
    * Le gestionnaire propose des extensions adaptées, comme : `Subtitles Editor`

## Extensions utiles pour le professeur

### Markdown
Pour créer des pages HTML grâce au langage Markdown, et visualiser en direct le rendu HTML.

Rechercher et installer l'extension `Markdown Preview Enhanced`

### Langage HTML
Pour prévisualiser en direct votre rendu HTML/Javascript.

Rechercher et installer l'extension `Browser Preview`

### Enregistrer une vidéo
Il faut avoir `FFmpeg` déjà installé.

Rechercher et installer l'extension `Chronicler`

### Édition de documents LaTeX

Rechercher et installer l'extension `LaTeX Workshop`

### Édition de documents Asymptote

Rechercher et installer l'extension `Asymptote`

### Autres extensions Python

* `Python Type Hint` ; pour l'annotation de type
* `Python Preview` ; pour un clone de *Python Tutor*
