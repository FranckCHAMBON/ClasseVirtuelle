# IHM mode texte {ignore=true}
> Partie 0 - Installations avec **[Termux](https://termux.com/)**.
>> Seule cette partie nécessite une connexion Internet, afin d'installer les différents logiciels.

@import "abstract.md"


## Sommaire de la partie 0 {ignore=true}

[TOC]

## Introduction

### Présentation de Termux pour Android

Cette activité utilise [Termux](https://termux.com/), une application pour tablette ou téléphone Android (tout élève de la région Sud possède une telle tablette). Termux émule un terminal et un environnement Linux proche de *Debian*. Cette application est un **logiciel libre** contrairement à de très nombreuses applications gratuites disponibles pour Android.

* On y installera une version de **Python** et un éditeur de code pour terminal,
* on pourra lancer des commandes système interprétées par **Bash**,
* on découvrira progressivement des possibilités :
    * découverte minimaliste de Bash,
    * édition et exécution de code Python ou autre,
    * utilisation de `doctest` avec Python,
    * création et confrontation de jeux de tests,
    * utilisation de plusieurs langages de programmation.

> Tout élève ayant une tablette Android peut donc faire l'activité. Aucune connexion Internet n'est requise pour les parties suivantes.

### Mise en place sur PC
L'activité peut tout aussi bien se faire sur un poste fixe équipé de Linux, conformément au programme de NSI. Termux ne faisant qu'émuler les outils déjà présents.

> Avec un poste basé sur Debian, l'administrateur n'aura qu'à installer quelques paquets supplémentaires : `tree`, `micro`, `cmatrix`, `cowsay`, `figlet`, `lolcat` et `fortune`.

La seule différence restante sera d'utiliser `python3`, au lieu de `python` dans Termux, pour l'interpréteur de Python 3.

### Alternatives au clavier virtuel

L'utilisation de la tablette sans clavier physique est problématique ; le clavier virtuel n'est pas adapté au travail de saisie.
> Cette activité peut toutefois être réalisée avec le clavier virtuel ; très peu de code est à saisir.

 Plusieurs solutions sont à envisager pour pouvoir utiliser un clavier physique sur la tablette.

#### Tablette connectée à un PC

On montre comment connecter, via le câble USB d'origine, la tablette à tout PC (Windows, MacOS, ou Linux) afin de pouvoir utiliser le clavier physique du PC, ainsi que la souris. Coût nul, si un PC est disponible ; cependant, c'est un peu technique. Cette solution offre des avantages à l'enseignant pour vidéo-projeter ou enregistrer une session.
@import "assets/scrcpy.png"

#### Clavier Bluetooth

Il est tout à fait possible de connecter un clavier Bluetooth à la tablette. Le coût est contenu, mais l'utilisation en classe de nombreuses connections Bluetooth est hasardeuse.
@import "assets/ClavierBT2.png"


#### Clavier USB avec ou sans adaptateur

Il est tout à fait possible de brancher un classique clavier USB type-A directement sur la tablette via un adaptateur USB (Type-C mâle ; Type-A femelle). Le coût est modique. On peut utiliser tout clavier USB, certains sont transportables, et certains sont déjà en USB type-C. **Attention, il faut choisir un modèle de clavier avec un accès facile aux touches de programmation `([{|&\}])`.** 
@import "assets/adapterUSB.jpg"

> Le choix d'un clavier doit être réfléchi ! Il peut être un objet personnel ([humour](http://www.legorafi.fr/2014/03/18/coince-chez-lui-pendant-3-semaines-il-survit-en-se-nourrissant-de-restes-coinces-entre-les-touches-de-son-clavier/)) qu'on garde longtemps.


## Mise en place pour tablette Android

On installe ici les logiciels nécessaires sur tablette, et on fait uniquement des tests rapides.

### 0. *TL;DR*

> ***TL;DR*** signifie *Too Long ; Didn't Read* (_[en](https://en.wikipedia.org/wiki/Wikipedia:Too_long;_didn%27t_read)_).
> On le croise souvent pour annoncer un résumé d'une longue partie que certains pourraient zapper.

Pour les **lecteurs avertis**, voici la mise en place résumée :

* Installer et lancer [Termux](https://termux.com/)
* Mettre à jour `$ apt update`
* Installer des logiciels `$ apt install python micro cowsay figlet fortune man coreutils tree ruby`
* Installer le paquet Ruby `$ gem install lolcat`

Pour les autres, bien suivre toutes les étapes suivantes, et faire chaque test.


### 1. Application Termux

Installation
: Installer l'application [Termux](https://play.google.com/store/apps/details?id=com.termux), avec *Google Play*.

Installation alternative
: Pour les personnes qui refusent d'utiliser *Google Play* pour des raisons de respect de la vie privée (par exemple), il est possible de l'installer via [*F-Droid*](https://f-droid.org/repository/browse/?fdid=com.termux), qui est un magasin d'applications bien plus respectueux.

Vérification
: Lancer l'application Termux.

@import "assets/termux1.png"
`$` est l'invite de commande **Bash**, on dit aussi *prompt* en anglais. C'est là que l'on entre les commandes. Il est inutile de taper sur `$` dans les commandes qui suivent, c'est juste pour indiquer qu'il s'agira d'une commande Bash.

> De même, ensuite on verra `>>>` l'invite de commande Python qu'il ne faudra pas entrer non plus, mais qui signifie que le _prompt_ attend une commande Python...

Important
: Les premières commandes à entrer sont :
    * Pour mettre à jour les dépôts de paquets : `$ apt update` puis répondre <kbd>Y</kbd>.
    * Pour mettre à jour les paquets déjà installés : `$ apt upgrade`

Explication
: `pkg` est la **commande** pour gérer (installation, suppression, ...) les paquets (_**p**ac**k**a**g**e_) systèmes dans Termux. On peut aussi utiliser `apt` comme sur Linux basé sur Debian.
`update` est un **argument**, `upgrade` en est un autre possible. Pour installer (ou supprimer, ou chercher) un paquet, il y a d'autres arguments à `apt`.

> Voyons comment installer le paquet pour Python dans Termux.

### 2. Langage Python

Python est un langage de script, tout comme Bash, mais plus récent (première version publique en février 1991 par Guido van Rossum).

Python est disponible dans Termux, une fois un paquet installé. En effet, sans installer le paquet, voici le résultat :
```
$ python
The program python is not installed. Install it by executing:
 pkg install python
```

> Python n'est pas installé, mais on nous indique comment faire.

Installation
: Dans Termux, entrer `$ apt install python`, puis répondre <kbd>Y</kbd>.

Explication
: `install` est un **argument** de la commande `apt`, pour installer des paquets.
`python` est un autre **argument**, ici le nom du paquet que l'on souhaite installer.

Remarque
: Suivant la plateforme, la commande pour gérer les paquets système porte le nom :
* `pkg` pour Termux (mais `apt` fonctionne aussi ; nous l'utiliserons),
* `apt` pour Debian et dérivés (très utilisés dans le monde éducatif en particulier),
* `rpm` pour Fedora et dérivés,
* `pacman` pour Arch et dérivés,
* `brew` pour MacOS,
* (`choco` ou `winget` ou `scoop` pour Windows).

Vérification
: Entrer à nouveau `$ python`
On obtient une invite de commande Python `>>>`

```
$ python
Python 3.8.3 (default, Jul  8 2020, 22:39:27)
[Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6 on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Exercice
: Effectuer un calcul du genre `>>> 2**127 - 1`

: Vérifier que la réponse est bien `170141183460469231731687303715884105727`

Quitter Python
: Entrer `>>> exit()`
On retrouve alors l'invite de commande Bash `$`.
: On peut aussi taper sur <kbd>Ctrl</kbd>+<kbd>D</kbd>, qui envoye le caractère ASCII ***EOF*** (_End Of File_) ; cela indique la fin de la saisie, tant pour Python que pour Bash.

Exercice
: Vérifier que l'on peut quitter Bash, ou bien avec `$ exit`, ou bien avec <kbd>Ctrl</kbd>+<kbd>D</kbd>. Noter que pour Python, il faut des parenthèses à `exit()`.

> L'utilisation de Python en ligne de commande n'est pratique que pour de très petits scripts ; pour de plus longs scripts, il est bien plus commode de les créer dans un éditeur.

### 3. Éditeurs nano et micro

**[nano](https://fr.wikipedia.org/wiki/GNU_nano)** est un éditeur de code minimaliste pour l'émulateur de terminal.

> Historiquement, il y a les éditeurs **Vi(m)** et **Emacs** qui sont très utilisés. Leur fonctionnement modal les rend puissants, mais aussi complexes pour une première prise en main.

Installation
: Dans Termux, nano est déjà installé, sinon entrer `$ apt install nano`

Exemple d'utilisation
: Dans Termux, pour éditer un fichier `salut.txt` avec nano :
    * Entrer : `$ nano salut.txt`
    * Écrire `Bonjour à tous !` sur la première ligne.
    * Enregistrer (_write **O**ut_) le fichier, avec <kbd>Ctrl</kbd>+<kbd>O</kbd>, et confirmer le nom du fichier.
    * Sortir (_e**X**it_) de nano, avec <kbd>Ctrl</kbd>+<kbd>X</kbd>.

D'autres raccourcis clavier (_bindings_) sont indiqués par défaut ; ils ne sont pas usuels...

@import "assets/nano1.png"


Remarques
: 1- **nano** n'offre pas des raccourcis usuels d'édition, cependant il affiche les plus utiles. C'est un logiciel libre qui reprend les fonctionnalités d'un ancien éditeur minimaliste non libre [pico](https://fr.wikipedia.org/wiki/Pico_(logiciel)).

: 2- **nano** est souvent déjà installé avec Linux, on le retrouve proposé dans de nombreux tutoriels ; il est *neutre* (dans le [conflit historique](https://fr.wikipedia.org/wiki/Guerre_d%27%C3%A9diteurs#%C3%89diteurs_pour_mainframes) Vim vs Emacs), et on peut utiliser à sa place l'éditeur de son choix : Vim, Emacs, xed, ou **micro**...

: 3- L'éditeur **[micro](https://micro-editor.github.io/)** est aussi un éditeur minimaliste, se présente comme successeur de nano, en offrant beaucoup plus de possibilités (meilleure coloration syntaxique et exécution de code), et de simplicités via ses raccourcis clavier. **Recommandé pour tous**.
`$ apt install micro`

`$ micro salut.txt`

@import "assets/micro1.png"

Raccourcis claviers (_bindings_) de **micro**, affichés avec <kbd>Alt</kbd>+<kbd>G</kbd> :
* <kbd>Ctrl</kbd>+<kbd>Q</kbd> pour quitter (_**Q**uit_)
* <kbd>Ctrl</kbd>+<kbd>S</kbd> pour sauvegarder (_**S**ave_)

> Nous utiliserons **micro** dans la partie 2 !


Installons d'autres logiciels plus ou moins utiles, historiquement très utilisés.

### 4. D'autres paquets utiles

#### Art ASCII

##### Cowsay {ignore=true}

[Cowsay](https://fr.wikipedia.org/wiki/Cowsay) est un logiciel libre qui crée de [l'art ASCII](https://fr.wikipedia.org/wiki/Art_ASCII), souvent une vache avec un message.

Installation
: `$ apt install cowsay`

Utilisation basique
: `$ cowsay "Salut"`
```
 _______
< Salut >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```


##### FIGlet  {ignore=true}

[FIGlet](https://fr.wikipedia.org/wiki/FIGlet) est un logiciel libre qui crée des bannières textuelles dans différentes polices d'écriture.

Installation
: `$ apt install figlet`

Utilisation basique
: `$ figlet "Vive la NSI"`

```
__     ___             _         _   _ ____ ___ 
\ \   / (_)_   _____  | | __ _  | \ | / ___|_ _|
 \ \ / /| \ \ / / _ \ | |/ _` | |  \| \___ \| | 
  \ V / | |\ V /  __/ | | (_| | | |\  |___) | | 
   \_/  |_| \_/ \___| |_|\__,_| |_| \_|____/___|    
```

##### fortune {ignore=true}
[fortune](https://fr.wikipedia.org/wiki/Fortune_(logiciel)) est un programme simple qui affiche un message au hasard provenant d'une base de données de citations, reprenant le principe du [biscuit chinois](https://fr.wikipedia.org/wiki/Biscuit_chinois) (_fortune cookie_), d'où le nom.

Installation
: `$ apt install fortune`

Utilisation basique
: `$ fortune`

```
Another dream that failed.  There's nothing sadder.
                -- Kirk, "This side of Paradise", stardate 3417.3
```

La plupart des citations sont délicates à saisir, elles nécessitent une bonne connaissance de la culture _geek_ ; nous nous en servirons pour obtenir un texte vaguement aléatoire.

##### cmatrix {ignore=true}

Pour avoir un fond d'écran dynamique comme dans le film _Matrix_.

Installation
: `$ apt install cmatrix`

Utilisation basique
: `$ cmatrix`

À retenir
: Pour quitter une commande qui ne finit pas, on envoie un signal pour l'interrompre <kbd>Ctrl</kbd>+<kbd>C</kbd>.

##### lolcat {ignore=true}

Pour avoir un peu de couleur dans les exercices à venir, on installe le logiciel `lolcat` qui est écrit avec le langage Ruby. Pour l'avoir dans Termux, on doit l'installer en deux étapes.

Installation
: * `$ apt install ruby` : pour installer le langage de programmation Ruby.
: * `$ gem install lolcat` : pour installer le paquet `ruby` qui donne `lolcat`.

Utilisation basique
: `$ lolcat salut.txt`

@import "assets/lolcat1.png"

`lolcat` est une variante ludique d'un outil système `cat` que nous découvrirons bientôt.

Ajoutons à Termux d'autres outils sytème.





#### Outils système

##### man  {ignore=true}
[man](https://fr.wikipedia.org/wiki/Man_(Unix)) affiche le **man**uel d'une commande passée en paramètre.

Installation
: `$ apt install man`

Utilisation basique
: `$ man fortune`

On obtient une page d'aide du **man**uel d'utilisation de la commande `fortune`. Nous apprendrons à lire en partie les informations contenues ; ça peut être technique.

> :warning: Pour **q**uitter une page de manuel, taper <kbd>Q</kbd>.

##### *GNU Core Utilities*  {ignore=true}
[Un lot](https://fr.wikipedia.org/wiki/GNU_Core_Utilities) d'outils variés souvent très utiles (pour les fichiers, les textes, les *shells*).

Installation
: `$ apt install coreutils`

Utilisation anecdotique, mais utile et efficace
: `$ factor 1234567890000007`
```
1234567890000007: 23 6427 79151 105517
```
On a obtenu la décomposition en facteurs premiers d'un entier. L'algorithme utilisé est plutôt bon !

##### tree {ignore=true}

`tree` est une commande qui nous permet de visualiser l'arborescence de nos répertoires.

Installation
: `$ apt install tree`

Utilisation basique
: `$ tree`

```
.
└── salut.txt

0 directories, 1 file
```


Nous découvrirons plusieurs autres outils très utiles !

Avant cela, voyons comment connecter en USB la tablette à un PC.

### 5. Connexion tablette-PC
Cette section est facultative et plutôt pour les enseignants. Elle permet d'avoir la tablette connectée en USB au PC (Windows, MacOS ou Linux), d'en prendre le contrôle avec le clavier et la souris PC, et d'avoir une fenêtre d'application PC qui clone l'écran de la tablette, pour l'enregistrer ou la diffuser.

#### 5.1. Tablette en mode développeur  {ignore=true}

* Accéder aux paramètres de la tablette,
* aller dans `Système`,
* aller dans `À propos de la tablette`
* Tapoter 7 fois `Numéro de build`
> Un message indique que « vous êtes désormais un développeur ».

#### 5.2. Tablette en mode débogage USB  {ignore=true}
 Il suffit de trouver l’option correspondante dans `{ } Options pour les développeurs`, dans les paramètres système.

 > Penser à le désactiver une fois l'utilisation terminée !

#### 5.3. Logiciel PC `scrcpy`  {ignore=true}

* Suivre [les instructions d'installation](https://github.com/Genymobile/scrcpy) pour votre système PC (Windows, MacOS, ou Linux).
> Pour Linux Debian (sid ou testing), Ubuntu 20.04, Mint 20, il suffit de faire :
> `$ sudo apt install scrcpy`

* Une fois `scrcpy` installé par l'administrateur, connecter votre tablette en USB sur votre PC et lancer `scrcpy` dans votre terminal PC.

@import "assets/scrcpy.png"

> La tablette est désormais pilotable par votre clavier/souris de PC (Windows, MacOS ou Linux). L'écran de la tablette est cloné dans une application PC, on peut l'enregistrer ou le diffuser en direct.

