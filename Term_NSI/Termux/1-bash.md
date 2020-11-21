# IHM mode texte {ignore=true}
> Partie 1 - Découverte de **[Bash](https://fr.wikipedia.org/wiki/Bourne-Again_shell)**.
@import "abstract.md"


## Sommaire {ignore=true}

[TOC]

## Introduction

### CLI

[Une interface en ligne de commande](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande) (en anglais *command line interface*, couramment abrégé **CLI**) est une **i**nterface **h**omme-**m**achine (IHM) dans laquelle la communication entre l'utilisateur et l'ordinateur s'effectue en mode texte.
> On appelle _shell_ ou émulateur de terminal un logiciel qui permet de lancer des commandes en mode texte.


### Bash

[Bash](https://fr.wikipedia.org/wiki/Bourne-Again_shell) est un langage de script libre, un interpréteur de commandes systèmes que l'on retrouve sous Linux, MacOS (enfin, presque...), Windows (depuis la version 10), et Android (via Termux par exemple). Il tire ses origines d'un logiciel écrit par Stephen Bourne en 1977 ; il garde certains aspects difficiles, mais reste incontournable.

### Objectifs

Cette première série d'exercices n'utilise presque pas l'éditeur, on présente et on s'exerce sur les possibilités basiques de Bash.
* Création, suppression et affichage de fichiers et de répertoires.
* Arguments, options et historique des commandes.
* Caractères d'échappement, métacaractères.
* Redirection de flux.
* Comparaison de fichiers.

Cette approche donne tous les outils nécessaires pour la partie 3 où on va créer des fichiers de tests qui serviront à comparer et confronter des algorithmes différents, ou écrits avec des langages de programmation différents.


### Avertissement

Cette partie pourra paraître dense, technique, avec beaucoup de contenu. Ce n'est pourtant qu'une première approche de Bash qui est un langage délicat à apprendre.
Il est conseillé de bien taper chaque commande proposée, de bien lire les sections « **À retenir** ».
Vous pourrez revenir sur cette partie 1 après avoir travaillé les autres parties qui seront plus simples.

### Quizz introductif
Après avoir étudié la partie 0 (Installations avec Termux), vous devriez pouvoir répondre aux questions suivantes :

1. `$` et `>>>` sont les invites de commandes par défaut de Bash, et Python.
    * Vrai.
    * Faux.

2. Bash et Python sont des langages de script, et Bash est plus ancien.
    * Vrai.
    * Faux.

3. Dans `$ apt install man`, `apt` est une commande et, `install` et `man` sont des arguments.
    * Vrai.
    * Faux.

4. <kbd>Ctrl</kbd>+<kbd>D</kbd> indique une fin de saisie, et <kbd>Ctrl</kbd>+<kbd>C</kbd> indique une interruption.
    * Vrai.
    * Faux.

5. Dans `$ man apt`, `apt` est un argument et, `man` une commande dont on sort avec <kbd>Q</kbd>.
    * Vrai.
    * Faux.

Réponses
: Toutes ces phrases étaient vraies, et constituaient un échauffement.

## Création de répertoire, de fichier

### mkdir, cd, cat, autocomplétion

1. Créer un répertoire (_**m**a**k**e **dir**ectory_) dont le nom est `textes` avec la commande `$ mkdir 'textes'`.
**Note** : les guillemets sont inutiles ici, il n'y a pas d'espace dans le nom du répertoire.
2. Entrer dans ce répertoire (_**c**hange **d**irectory_) avec la commande `$ cd textes`.
**Note** : il suffit d'entrer `$ cd t` puis d'appuyer sur la touche <kbd>Tab ⭾</kbd>, et Bash complète automatiquement `textes`, on parle d'autocomplétion. **Très utile !**
3. Avec `$ nano prénom.txt`, créer un fichier qui contient sur une ligne votre prénom (ou pseudo).
4. Avec **nano**, créer un fichier `métiers.txt` qui contient sur une ou plusieurs lignes des métiers rêvés.
5. Afficher le contenu con**cat**éné avec `$ cat prénom.txt métiers.txt`
**Note** : Penser deux fois à la touche <kbd>Tab ⭾</kbd>

À retenir
: * `mkdir` : Créer un répertoire (_**m**a**k**e **dir**ectory_)
: * `cd` : Changer de répertoire (_**c**hange **d**irectory_)
: * `cat` : Con**cat**éner un ou plusieurs fichiers, pour les afficher.
: * <kbd>Tab ⭾</kbd> : Permet l'autocomplétion.
: * Lorsqu'on utilise un [gestionnaire de fichiers](https://fr.wikipedia.org/wiki/Gestionnaire_de_fichiers) en mode graphique, les actions sont effectuées en arrière-plan par des commandes en ligne.

Nous verrons progressivement comment faire en ligne les actions possibles à la souris avec un gestionnaire de fichiers ; et que les méthodes en ligne sont bien plus puissantes.

## Jouer avec la couleur

### lolcat, man, historique des commandes

1. Reprendre la dernière question de l'exercice précédent, mais avec `lolcat` à la place de `cat`.

> Au lieu de taper `$ lolcat prénom.txt métiers.txt`, il suffit d'appuyer sur <kbd>↑</kbd> afin de remonter dans l'historique de la ligne de commande, retrouver la dernière commande de l'exercice précédent, appuyer sur la touche <kbd>Home</kbd> du clavier, et ajouter `lol`.

2. Essayer la variante `$ lolcat -a prénom.txt métiers.txt`. On dit que `-a` est une **option**, on peut découvrir les options d'une commande avec `man`, ici par exemple `$ man lolcat`.

À retenir
: * `lolcat` n'est qu'une commande jouet.
: * L'historique de la ligne de commande est disponible avec Bash et aussi Python, en utilisant les flèches haut et bas. Il faut penser à s'en servir pour gagner en productivité. De plus <kbd>Ctrl</kbd>+<kbd>←</kbd> et <kbd>Ctrl</kbd>+<kbd>→</kbd> permettent de se déplacer par mot ; rapide !
: * Pour découvrir les **options** et **arguments** d'une commande, on regarde son manuel avec `man`. Il est possible d'avoir les pages du manuel en français en fonction de l'installation système. Il est recommandé d'avoir un minimum de vocabulaire pour lire en anglais les pages de manuel.


## Découvrir les options de commande
### echo, séquences d'échappement

`echo` est une commande qui affiche une ligne de texte, et avec un saut le ligne à la fin.
* `-n` est une option dont l'effet est justement de ne pas ajouter le saut de ligne à la fin.
* `-e` est une option qui permet d'échapper le caractère `\` et de donner un sens à :
    * `\n` : un saut de ligne
    * `\t` : une tabulation horizontale

> Pour découvrir les autres séquences d'échappement, entrer `$ man echo` 

Exercice 1
: Étudier les **4** exemples ci-dessous :

```bash
$ echo Salut
Salut
$ echo -n 'Bizarre ?'
Bizarre ?$ echo 'Non !'
Non !
$ echo -e 'ligne 1\nligne2\n\tmot décalé'
ligne 1
ligne2
        mot décalé
$
```
Remarques
: Dans l'ordre, on a :
    1. Les guillemets sont inutiles ici.
    2. (`-n`) ; Pas de saut de ligne, donc le _prompt_ se retrouve collé à la suite.
    3. Les guillemets sont inutiles ici aussi. Tester !
    4. (`-e`) ; il y a des caractères échappés qui autorisent ici des sauts de ligne et des tabulations. Il en existe d'autres ; voir avec `$ man echo`.

Exercice 2
: Compléter cette commande qui affiche le résultat suivant :

```bash
$ echo ...à vous de remplacer cette partie...
\n	saut de ligne
\t	tabulation
$
```

Une solution est :
```bash
$ echo -e '\\ \bn\tsaut de ligne\n\\ \bt\ttabulation'
```
Expliquer cette solution après avoir bien lu `$ man echo`.

À retenir
: * `\n` représente un saut de ligne.
: * `\t` représente une tabulation horizontale.
: * On retrouve ces échappements dans de très nombreux langages de programmation, ils sont normalisés.


Exercice 3
: Relire la section sur `cowsay` dans la partie 0 - Installations. Lire le manuel avec `$ man cowsay`. En utilisant l'option `-e 'XX'` et aussi l'option `-T` à compléter, obtenir l'affichage du dessin :

```
__________________________
< Je tire aussi la langue. >
 --------------------------
        \   ^__^
         \  (XX)\_______
            (__)\       )\/\
              U ||----w |
                ||     ||
```

> Expliquer avec une phrase le rôle, ici, des options choisies.


## Lister des fichiers et répertoires, les supprimer

### ls, touch, rmdir, rm, pwd, motifs et métacaractères

On a vu comment :
* Créer un répertoire avec `mkdir`
* Changer de répertoire de travail avec `cd`
* Créer un fichier avec `nano` ou `micro`
* Afficher un ou plusieurs fichiers concaténés avec `cat`

Voyons comment faire la **l**i**s**te des fichiers dans un répertoire avec la commande `ls`, et ses options...

Exemple
: Tester les commandes suivantes :
    1. `$ touch machin`
    2. `$ mkdir bidule`
    3. `$ ls`
    4. `$ ls -a`
    5. `$ ls -l`
    6. `$ ls *m*`
    7. `$ rmdir bidule`
    8. `$ rm machin`

Explications
: 1. La commande `touch` crée un fichier vide s'il n'existe pas ; sinon modifie juste sa date de dernier accès. Ici, le fichier `machin` est créé, sans extension ; ce n'est pas un problème.
: 2. Le répertoire `bidule` est créé, il est vide.
: 3. La liste des fichiers et répertoires est donnée.
: 4. L'option `-a` pour _**a**ll_ (tous), affiche aussi les fichiers et répertoires cachés. On note la présence ici de :
        * `.` : le répertoire actuel
        * `..` : le répertoire parent
        * il peut y en avoir d'autres, ces fichiers ou répertoires ont un nom qui commence par un `.`
: 5. L'option `-l` donne des détails **l**ongs sur les propriétaires des fichiers et des répertoires, le groupe auxquels ils appartiennent, ainsi que les droits en écriture, lecture et exécution associés, mais aussi sur les dates de création. Ces nombreux détails sont utiles à l'administration du système. Nous en reparlerons dans la partie 4.
: 6. L'**argument** `*m*` n'est pas une option, c'est un motif qui sert à filtrer les résultats qu'on souhaite afficher. Ici, n'importe quoi `*` (même rien), suivi d'un `m`, suivi de n'importe quoi `*`. Concrètement tout ce qui contient un `m` donc. Dans la partie 4, nous découvrirons davantage les motifs.
: 7. On supprime le répertoire **vide** `bidule`.
: 8. On supprime le fichier `machin`.

Exercice (un peu plus difficile)
: 1. Quelle est la commande pour se déplacer dans le répertoire parent ?
: 2. En étudiant `$ man rmdir`, existe-t-il une commande pour effacer un répertoire non vide ?
: 3. En général, que fait la commande `$ ls m*t*` ?
: 4. Dans un motif, `?` remplace n'importe quel caractère. En général, que fait la commande `$ ls image???.jpg`
: 5. À quoi sert la commande `pwd` ? Penser à `man`.

À retenir
: * On obtient souvent une aide succincte d'une commande avec l'option `-h` ou `--help`, comme avec `$ touch --help`
: * On peut créer un fichier vide avec `touch`.
: * On peut faire la liste des fichiers et répertoires avec `ls` ; il y a des options pour l'administration système, où les droits sur les fichiers ont un rôle important.
: * On peut supprimer (_**r**e**m**ove_) des fichiers avec `rm`.
: * On peut supprimer des répertoires (_**r**e**m**ove **dir**ectory_) avec `rmdir`.
: * On peut utiliser des motifs pour filtrer les résultats, on utilise des [métacaractères](https://fr.wikipedia.org/wiki/M%C3%A9tacaract%C3%A8re) (_wildcard_ ou _joker_) :
    * `*` remplace toute chaîne de caractères, même vide ;
    * `?` remplace un seul caractère.
    * Il y a encore d'[autres techniques](https://en.wikipedia.org/wiki/Glob_%28programming%29) pour filtrer...
: * On peut savoir quel est le répertoire de travail actuel avec `pwd`.

## Changer rapidement de répertoire, arborescence

Entrer toutes les commandes suivantes dans l'ordre et en pensant à la touche <kbd>Tab ⭾</kbd>:
1. `$ cd`
2. `$ mkdir tex`
3. `$ touch tex/pre.sty`
4. `$ mkdir tex/asymtote`
5. `$ touch tex/asymtpte/tri.asy`
6. `$ tree tex*`
7. `$ cd texte`
8. `$ ls`
9. `$ cd ~/tex/asymptote`
10. `$ ls`
11. `$ cd -`
12. `$ ls`
13. `$ cd && rm -rf tex`

Explications :
1. La commande `$ cd`, **sans argument**, déplace le répertoire de travail au répertoire de l'utilisateur, son _home_. Il existe un répertoire parent, mais l'utilisateur n'en est pas propriétaire. À partir de son _home_, l'utilisateur peut être propriétaire de tous les fichiers et répertoires.
2. On crée un répertoire.
3. On crée un fichier dans ce répertoire. Noter le `/` qui sépare ; il indique le chemin à suivre.
4. On crée un sous-répertoire.
5. On crée un nouveau fichier vide `tri.asy` avec un chemin un peu plus long.
6. La commande `$ tree tex*` affiche l'arborescence des répertoires et fichiers, du motif qui commence par `tex` ; pour nous, `tex` et `textes` répondent à ce motif.
7. On change de répertoire avec un chemin **relatif** à notre position.
8. On affiche le contenu ; juste un test.
9. On change de répertoire avec un chemin **absolu** qui fait partir de notre _home_, représentée par le tilde (`~`) obtenu avec <kbd>AltGr</kbd>+<kbd>2é</kbd> sur un clavier Azerty. 
10. On affiche le contenu ; juste un test.
11. On change de répertoire de travail, directement vers le précédent. 
12. On affiche le contenu ; juste un test.
13. On revient au répertoire personnel de l'utilisateur, et (`&&`) on enchaîne avec une autre commande, on supprime le répertoire `tex`, **r**écursivement (`-r`), et en **f**orce (`-f`).


À retenir

: * La commande `tree` affiche de manière graphique l'arborescence ; utile pour visualiser la structure d'arbre des répertoires de votre projet. La racine est en haut !
: * La commande `$ cd` peut s'utiliser sans argument (retour au _home_ de l'utilisateur), ou `$ cd -` qui revient au précédent répertoire de travail. **Utile** lorsqu'on veut naviguer **rapidement** entre deux répertoires non parents.
: * Un chemin est une suite de répertoires, séparés par `/`, finissant par un fichier ou non, et commençant par `~` ou non, ou bien par `/`. Ils indiquent un répertoire ou un fichier distant. S'il commence par `/` ou par `~`, c'est un chemin absolu, sinon il est relatif au répertoire actuel de travail.
: * On peut enchaîner deux commandes avec `&&` ; seulement si la première réussit sans échec, alors l'autre sera lancée. C'est une forme de structure conditionnelle.

Exercice
: Quels sont les significations en général des chemins suivants ? _On attend une phrase, et un exemple pour illustrer._
    1. `~/Images/2020*`
    2. `../*.txt`
    3. `../../projet/doc/src/inf?.???`
    4. `./secret/../secret.txt/clé`

Remarques
: Un nom de fichier ou de répertoire peut contenir zéro, un ou plusieurs points, ainsi avoir une extension n'est pas réservé aux fichiers, et une extension peut être très variée.
: Un fichier **ne peut pas** porter le même nom qu'un répertoire existant dans le même répertoire.

Nous avons pu créer des fichiers vides. Sans utiliser d'éditeur, montrons comment créer un petit fichier non vide, et comment faire un petit ajout à un fichier déjà existant.

## Créer un fichier non vide sans éditeur

### Opérateurs de redirection `>` et `>>`

Tester dans l'ordre les commandes suivantes :
1. `$ echo 3 > test`
2. `$ cat test`
3. `$ echo 1000 >> test`
4. `$ cat test`
5. `$ echo -e "2222\n999999" >> test`
6. `$ cat test`
7. `$ echo oups > test`
8. `$ cat test`
9. `$ rm test`
10. `$ cat test`

Exercice
: Expliquer ce qui se passe pour chacune des commandes `$ cat test`.


> La redirection du résultat affiché vers un fichier n'est pas propre à la commande `echo`, mais est valable pour toute commande qui produit un affichage.

Pour créer un fichier qui récupère l'affichage d'une commande :
* `$ commande [arguments] > fichier`

Pour ajouter à un fichier l'affichage d'une commande :
* `$ commande [arguments] >> fichier`

> Dans ces deux cas, l'affichage n'est pas effectué, il a été redirigé.


Exercice
: Donner et exécuter les commandes pour les actions suivantes :
    1. Aller dans le répertoire `textes` de votre répertoire personnel.
    2. Vérifier votre répertoire de travail actuel.
    3. En une seule commande, créer un fichier `prénom.fig` contenant votre prénom (ou votre pseudo) en FIGlet.
    4. Vérifier avec l'affichage du fichier `prénom.fig` le résultat qui pourrait être :

```bash
 _____                     _    
|  ___| __ __ _ _ __   ___| | __
| |_ | '__/ _` | '_ \ / __| |/ /
|  _|| | | (_| | | | | (__|   < 
|_|  |_|  \__,_|_| |_|\___|_|\_\
```

À retenir
: * L'opérateur `>` permet de rediriger la sortie d'une commande vers un fichier qui est effacé **avant** l'exécution de la commande.
: * L'opérateur `>>` permet de rediriger la sortie d'une commande vers un fichier auquel on ajoute la sortie.

### cat sans argument, redirigé

Exercice 1

: Suivre les instructions :
    1. Taper la commande `$ cat`
    2. Taper du texte, avec des retours à la ligne.
    3. Finir la saisie avec <kbd>Ctrl</kbd>+<kbd>D</kbd> pour signaler ***EOF***, que l'on a déjà rencontré.

On observe que `$ cat` se contente d'afficher directement ce qui est tapé. Au lieu de l'afficher, on peut rediriger la sortie vers un fichier.

Exercice 2

: Suivre les instructions :

    1. Taper la commande `$ cat > surprise`
    2. Taper du texte, avec des retours à la ligne.
    3. Finir la saisie avec <kbd>Ctrl</kbd>+<kbd>D</kbd> pour signaler ***EOF***.
    4. Taper `$ cat surprise`. Penser à l'historique de commande !

À retenir
: * On peut créer un petit fichier sans utiliser d'éditeur. Soit en entrant le texte via `$ cat > fichier`, soit en redirigeant également la sortie d'une autre commande vers le fichier, avec l'opérateur `>`.
: * On peut ajouter, au lieu de le recréer de la même manière avec l'opérateur `>>`.
: * On parle de **sortie standard**.


De la même manière qu'on peut rediriger l'affichage vers un fichier, on peut rediriger l'entrée clavier par un fichier. Ce qui est contenu dans un fichier fera office d'argument à une commande. Voyons donc comment utiliser l'opérateur `<`.

## Utiliser le contenu d'un fichier comme argument

### Opérateur `<`

Dans le répertoire `~/textes`, vous avez deux fichiers `prénom.txt` et `métiers.txt` construits au début de cette activité ; travaillons avec.

1. `$ cd ~/textes`
2. `$ figlet < prénom.txt`
3. `$ figlet < métiers.txt > métiers.fig`
4. `$ lolcat -a métiers.fig`

Exercice
: Expliquer chacune des commandes précédentes par une phrase.

À retenir
: * L'opérateur `<` permet de rediriger l'entrée d'une commande à partir d'un fichier au lieu de lire le clavier.
: * On parle d'**entrée standard**.

## pipeline, branchement de redirection
### Opérateur `|`

On va brancher la sortie d'une commande directement sur l'entrée d'une autre commande, le tout sans passer par un affichage intermédiaire.

L'idée est de faire :
1. `$ commande1 > temporaire`
2. `$ commande2 < temporaire`

Mais sans passer explicitement par le fichier nommé `temporaire`. Une raison étant : le fichier `temporaire` existe-t-il déjà ? Il ne faudrait pas effacer un fichier déjà présent utile à une autre commande ! Une solution serait de fabriquer un nom aléatoire (ou dépendant de l'heure précise), mais rien ne garantit qu'il n'existe pas déjà...

La solution est d'utiliser un _pipeline_ `|` :
* `commande1 | commande2`

La sortie de `commande1` est automatiquement redirigée vers l'entrée de `commande2`, et Bash gère l'utilisation d'un fichier temporaire unique de manière transparente.

Exemple
: Avec l'exercice précédent, on peut remplacer les deux dernières lignes par :
    * `$ figlet < métiers.txt | lolcat -a`

On peut enchaîner des _pipeline_ comme dans l'exemple :
* `$ fortune | cowsay | lolcat`

Exercice
: Tester cet enchaînement de commandes et expliquer le résultat obtenu.

À retenir
: L'opérateur `|` permet de brancher la sortie d'une commande sur l'entrée d'une autre commande. Dans une situation de travail à la chaîne dans une usine, on procède de la façon `$ com1 | com2 | ... | comk`, le travail est découpé en fonctions élémentaires. **Chaque commande étant censée faire une chose simple, mais la faire bien**.

Nous avons évoqué le problème de créer un fichier temporaire avec un nom qui n'existe pas déjà, ou alors le souhait d'enregistrer un travail avec un nom de fichier qui reprend la date et l'heure d'enregistrement. Voyons comment faire.

## À la recherche du temps qui passe
### date, commande pour obtenir aussi l'heure précise

La commande `$ date`, sans argument, affiche la date et l'heure avec un format prédéfini, dans une langue qui dépend d'un paramètre local.
Il est possible d'obtenir l'heure très précise, soit de l'instant actuel, soit d'un autre instant que l'on demanderait. Exemples :
* Quelle sera la date jeudi prochain ? 
* Quelle sera l'heure, dans 9h, avec le fuseau horaire de _Buenos Aires_ ?

Nous ne verrons pas de commandes aussi complexes, juste nous indiquons que c'est techniquement possible.

Étudions un exemple issu de `$ man date` :

```bash
$ date --date='@2147483647'
Tue Jan 19 04:14:07 CET 2038
```

> Dans cet exemple, on demande la date plus de 2 milliards de secondes après l'[epoch](https://fr.wikipedia.org/wiki/Epoch) d'Unix (l'origine du temps en Unix, le 1er janvier 1970 00:00:00 UTC.)
> Le nombre 2147483647 est le plus grand entier représenté dans un conteneur d'entier signé sur 32 bit, on obtient la date du [bug de l'an 2038](https://fr.wikipedia.org/wiki/Bug_de_l%27an_2038).
>
> **En pratique**, on se sert souvent de `date` dans un script pour récupérer l'heure ou la date présente, c'est utile pour nommer un fichier temporaire, par exemple.


Exercice 1
: En étudiant la page donnée par `$ man date`, créer en **une seule** commande un fichier `année.txt` contenant l'année en cours. Cette commande doit rester valable pour les années à venir...

> Aide : Le manuel indique `date +[FORMAT]` ; il suffit de remplacer `[FORMAT]` par une séquence donnée qui correspond à l'année en cours.

Exercice 2
: Proposer en **une seule ligne** une instruction qui affiche **l'heure courante**, avec les minutes, en FIGlet, comme :

```bash
 _ _____  ____   ___  
/ |___  ||___ \ / _ \ 
| |  / (_) __) | (_) |
| | / / _ / __/ \__, |
|_|/_/ (_)_____|  /_/ 
```

### time, pour la durée d'exécution d'une commande

Une commande (Bash, ou autre) peut prendre un certain temps d'exécution.

`$ time `*`commande [arguments]`* exécute la *commande* avec ses *arguments* éventuels et affiche ensuite le temps écoulé.

On peut l'utiliser pour chronométrer l'exécution d'un script Python, ou d'un autre programme compilé.

Exemple classique et important
: `$ time python mon_script.py < mon_entrée > ma_sortie`

: La commande `python` lit un script qui prend `mon_entrée` comme entrée standard (sans avoir besoin de lire au clavier), puis écrit le résultat dans un fichier `ma_sortie`, et enfin affiche à l'écran le temps écoulé.

### timeout, pour limiter une durée d'exécution

Les compétitions d'algorithmique imposent, par exemple, qu'un programme doit résoudre un problème particulier en une durée annoncée.

Pour imposer une limite de temps de 1 seconde au programme présenté plus haut, on peut écrire :

`$ timeout 1 time python mon_script.py < mon_entrée > ma_sortie`

Dans le cadre des entraînements, que l'on retrouve sur FranceIOI par exemple, il est intéressant de vérifier que `ma_sortie` correspond bien à la `sortie_officielle`. Il nous faut donc des outils pour comparer des fichiers.

On rappelle que dans la partie 3, on va justement créer des jeux de tests d'entrée sortie pour nos programmes. Ainsi, on commence à avoir presque tous les outils pour ce faire !


## Autres opérations sur les fichiers

### cp pour copier, cmp pour comparer, mv pour déplacer

La commande `cp` permet de **c**o**p**ier un ou plusieurs fichiers `source` décrit par un nom ou un motif.

Utilisation basique
: `$ cp source destination`

* `source` peut être **un** fichier, et alors `destination` est un répertoire ou un fichier.
* `source` peut être **plusieurs** fichiers (via un motif par exemple), et alors `destination` est un répertoire.

Exemples
: On crée un répertoire pour ces tests, `$ mkdir ~/textes/cptests`
    1. `$ cd ~/textes`
    2. `$ cp *.txt cptests`
    3. `$ cp prénom.txt cptests/prénom.copie.txt`
    4. `$ cmp cptests/prénom.txt cptests/prénom.copie.txt`
    5. `echo 'première copie' > cptests/prénom.txt`
    6. `echo 'seconde copie' > cptests/prénom.copie.txt`
    7. `$ cmp cptests/prénom.txt cptests/prénom.copie.txt`
    8. `$ rm -rf cptests`
    9. `cd -`

Exercice
: Expliquer ce que fait chacune des instructions précédentes. Une nouvelle commande est présentée `cmp` pour comparer des fichiers ; elle est très utile.

À retenir
: La commande `cp` permet de copier (**c**o**p**y) des fichiers.
: La commande `cmp` permet de comparer (**c**o**mp**are) des fichiers.
: La commande `mv` permet de déplacer (**m**o**v**e) des fichiers.
: Il y a aussi une commande `diff` pour avoir plus de détails sur la **diff**érence entre deux fichiers.



## Présentation rapide de quelques filtres
### head, tail, sort, cut
Une commande filtre prend un fichier en argument et renvoie une version modifiée.
* `$ head fichier` renvoie le début d'un fichier,
* `$ tail fichier` renvoie la fin d'un fichier,
* `$ sort fichier` renvoie le fichier trié,
* `$ cut [option] fichier` sélectionne des colonnes du fichier.

Ces commandes possèdent de nombreuses options ; consulter leur manuel pour les découvrir.

## Exercice bilan

* Dans votre _home_, créer un répertoire `exercice`, et y aller.
* En une commande créer un fichier `animal.txt` contenant une ligne : le nom d'un animal de compagnie (fictif).
* Ajouter à ce fichier une ligne de la forme `âge : 21 ans`.
* Ajouter en une fois, à ce fichier, un paragraphe de quelques lignes (au moins deux) évoquant cet animal.
* Avec la commande `head` (regarder son manuel), créer un fichier `nom.txt` qui contient le nom de l'animal.
* Avec la commande `tail` (regarder son manuel), créer un fichier `à_propos.txt` qui reprend uniquement l'anecdote.
* Avec une instruction sur une seule ligne, créer un fichier `âge.txt` qui contient l'âge de l'animal sans la partie `âge :`, mais uniquement `21 ans` dans le cas de l'exemple donné.
* Concaténer les fichiers `animal.txt`, `âge.txt`, et `à_propos.txt` en un fichier `animal2.txt`.
* Utiliser la commande `diff` pour comparer les fichiers `animal.txt` et `animal2.txt`.
* Créer une copie `animal3.txt` de `animal.txt`.
* Ajouter à `animal3.txt` une ligne `Ceci est une copie.`
* Ajouter à `animal3.txt` une autre ligne contenant la date et l'heure courante.
* Utiliser la commande `cmp` pour comparer les fichiers `animal.txt` et `animal3.txt`. Expliquer !
* Ajouter à `animal.txt` une ligne `Ceci est l'original.`
* Utiliser la commande `cmp` pour comparer les fichiers `animal.txt` et `animal3.txt`. Expliquer !
* Utiliser la commande `cmp` pour comparer les fichiers `animal.txt` et `animal.txt` (oui, deux fois le même fichier). Expliquer !
* Faîtes raconter à une vache l'anecdote sur l'animal, le tout en couleur et animé.



---




 cat

```bash
$ cat ~/somme1/essai1.py
```
```
n = int(input())
s = 0
for i in range(n):
    s = s + i
print(s)
```

> Dans cet exemple `~` représente le répertoire _home_ de l'utilisateur ; le caractère tilde s'obtient avec <kbd>AltGr</kbd>+<kbd>2é</kbd>. De là, on regarde dans le répertoire `somme1` et on affiche le fichier `essai1.py`. Le répertoire de travail n'a pas été modifié au passage, cet exemple peut être effectué depuis tout répertoire de l'utilisateur.

Exercice
: Pour jouer un peu, on peut mettre un peu de couleur.
    * `$ apt install ruby` ; on installe le langage de programmation ruby...
    * `$ gem install lolcat` ; qui offre un gestionnaire de paquets ruby, et en particulier le logiciel `lolcat`

```
$ lolcat ~/somme1/essai1.py
(( surprise ))
```

 head, tail

On suppose que l'on est dans le répertoire `somme1` qui contient le fichier `essai1.py` **qui fait 5 lignes**.

```
$ head -n4 essai1.py
n = int(input())
s = 0
for i in range(n):
    s = s + i
$ head -n-4 essai1.py
n = int(input())
s = 0
```

> Dans cet exemple on affiche la tête (_head_) du fichier, d'abord les 4 premières lignes. Puis tout sauf les 4 dernières ; la tête encore.
> Sans le paramètre `-n` la commande `head` affiche les 10 premières lignes par défaut.

Exercice
: Afficher la dernière ligne du fichier `essai1.py`

cmp
On suppose que l'on est dans le répertoire `somme1` qui contient le fichier `essai1.py`.

Exercice
: On va dupliquer le fichier `essai1.py`, faire des modifications et lancer des comparaisons.
* Pour dupliquer : `$ cp essai1.py doublon.py`
* Comparer les deux fichiers : `cmp essai1.py doubon.py` ; aucun affichage signifie que les deux fichiers sont identiques.
* Éditer le fichier `doublon.py`, et ajouter un commentaire en fin de fichier `# sur la ligne 6`
* Tenter à nouveau la comparaison ; `cmp` indique que la comparaison s'est arrêtée sur une fin de fichier (_**EOF** ; End Of File_) et indique la ligne de la première différence, ainsi que le nombre de caractères (_char_) comparés.
* Éditer le fichier `doublon.py`, et remplacer la variable `s` par `somme`.
* Tenter à nouveau la comparaison ; `cmp` indique la ligne de la première différence, ainsi que le nombre de caractères (_char_) comparés.

Remarques
: 1- On va créer des jeux de tests qui seront de gros fichiers, ils seront traités par des scripts Python cousins qui produiront des sorties à comparer. Typiquement, on commence à produire un algorithme par force brute pour résoudre un problème, ensuite on tente de construire un meilleur algorithme, plus rapide, mais peut-être bogué. **Comparer les sorties des jeux de tests sera utile pour corriger l'algorithme**.
: 2- Montrons comment remplacer facilement du texte par un autre à l'intérieur de **micro**. En éditant le script `doublon.py`, entrer <kbd>Ctrl</kbd>+<kbd>E</kbd>, on entre en mode commande, en bas l'invite de commande micro est `>`, on entre à la suite `replace somme truc`. Micro cherche toutes les occurrences de `somme`, il suffit de taper `y` pour chacune à remplacer.

 Exercice : `essai3.py`
> Créer en **une seule** commande un fichier `essai3.py` qui en une ligne a le même fonctionnement que `essai1.py`.

> Aide : comprendre le troisième test dans la _docstring_ dans `essai2.py`.


 Redirections avec _pipeline_

 Exercice : année




....

    1. `$ mkdir calcul`
    1. `$ cd calcul`
    1. `$ mkdir somme1`
    2. `$ cd somme1`
    3. `$ nano essai1.py`

* On a créé (et on y est entré) un répertoire `calcul` puis `somme1` pour notre premier test,
* on peut alors éditer un premier script Python `essai1.py`, par exemple :

```py
n = int(input())
s = 0
for i in range(n):
    s = s + i
print(s)
```

* Pour utiliser ce script, dans Termux, on entre `$ python essai1.py`
    * Le script attend une entrée ; donnons `5` par exemple.
    * Justifier que la sortie affichée est `10`.
* Pour modifier ce script, dans Termux, on entre `$ nano essai1.py`, mais on peut aussi utiliser deux fois la flèche du clavier <kbd>↑</kbd> qui remonte dans l'historique des dernières commandes.




 Édition de script
1. Vérifier votre [répertoire de travail](https://fr.wikipedia.org/wiki/Pwd) avec `$ pwd`
    * `pwd` signifie _**p**rint **w**orking **d**irectory_
    * vous devriez être dans `home/somme1`
1. Vérifier que vous y avez bien le fichier `essai1.py` présent avec la commande `$ ls`
1. Faire une **c**o**p**ie du fichier vu en première partie `essai1.py` en `essai2.py` avec la commande bash `$ cp essai1.py essai2.py`
1. Vérifier à nouveau la **l**i**s**te des fichiers de votre répertoire avec `$ ls`
1. Éditer le fichier `essai2.py` avec **nano** ou **micro**.
2. Modifier ce script Python en suivant le modèle ci-dessous.
```py
def f(n):
    """
    f retourne ...
    Exemples :
    >>> f(2)
    1
    >>> f(5)
    10
    >>> f(100) == sum(range(100))
    True
    """
    s = 0
    ...

n = int(input())
print(f(n))
```
3. Compléter la _docstring_ pour expliquer en français ce que fait la fonction `f`.
3. Justifier la véracité des trois tests.
4. Enregistrer le fichier `essai2.py` et quitter l'éditeur.
5. Lancer dans Bash `$ python -m doctest -v essai2.py`
> Cette dernière commande n'est pas à retenir, mais le principe de _doctest_ oui !
> * Penser à créer des fonctions autant que possible.
> * Penser à créer une _docstring_ pour toute fonction.
> * Penser à y inclure des tests simples sous la forme :
>   * `>>> test_fonction`
>   * `Sortie attendue`
> * Plus d'informations sur _doctest_, [un module Python](https://docs.python.org/fr/3/library/doctest.html).


