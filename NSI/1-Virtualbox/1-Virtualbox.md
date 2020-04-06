<!-- slide -->

# Virtualisation système

**Premières expériences**

La [virtualisation système](https://fr.wikipedia.org/wiki/Virtualisation) consiste, en informatique, à exécuter sur une machine hôte, dans un environnement isolé, des systèmes d'exploitation.

<!-- slide vertical=true -->

![exemple-global](assets/total3.png)

Trois machines virtuelles invitées dans une machine hôte Linux Mint

<!-- slide vertical=true -->

## Pourquoi ?

* C'est un bac à sable pédagogique pour les premières installations d'un système d'exploitation.

* Permet de faire des tests variés, du partage de ressources, de la sécurisation de réseau, du déploiement ...

* Et d'[autres raisons](https://fr.wikipedia.org/wiki/Virtualisation#Int%C3%A9r%C3%AAts) encore.

<!-- slide vertical=true -->

Découvrons avec [VirtualBox](https://fr.wikipedia.org/wiki/Oracle_VM_VirtualBox), un logiciel libre de virtualisation comment installer un **système d'exploitation libre**.

Cette installation vous permettra de travailler à la maison dans les conditions prévues par le B.O. en NSI.

<!-- slide -->

## Vocabulaire

* Machine hôte (*Host*) : c'est l'ordinateur physique qui va "héberger" une ou plusieurs machines virtuelles.

> Votre ordinateur actuel sera prêt si vous disposez d'au moins 1 Go de mémoire vive disponible, et 20 Go de place sur votre disque dur.

<!-- slide vertical=true-->

* Système hôte : c'est le système d'exploitation (_**O**perating_ _**S**ystem_ ; *O.S.*) de la machine hôte. 

> *VirtualBox* est multiplateforme, vous pouvez l'installer avec un système hôte *Windows*, *Linux* ou *MacOS*.

<!-- slide vertical=true-->

* Machine invitée (*Guest*) : c'est la machine virtuelle qui sera allouée et gérée par l'hyperviseur VirtualBox.

> Cette machine aura un disque dur virtuel, un lecteur DVD virtuel, un écran virtuel, un processeur avec un ou plusieurs cœurs virtuels, etc. Cette machine peut capturer votre souris et votre clavier. On pourra aussi y bricoler virtuellement : ajout/suppression de matériel...

<!-- slide vertical=true-->

* Système invité : c'est le système d'exploitation que vous installez sur la machine virtuelle.

> Nous expérimenterons l'installation de différentes versions de *Linux* comme  Debian, Ubuntu, Linux Mint, Manjaro, CentOS, ou Fedora.

> L'installation de versions variées de Windows ou MacOS est possible.

<!-- slide vertical=true-->

* Les suppléments invités (*Guest Additions*) : c'est un pack logiciel à installer sur la machine virtuelle pour optimiser son fonctionnement, comme pour avoir une meilleure résolution d'écran.

> Ce pack n'est pas un logiciel libre et il est interdit de l'utiliser en entreprise ou à l'Université.

> À titre privé, vous avez le droit de l'installer ; nous verrons comment.

<!-- slide -->

## Installation de VirtualBox

Sur la [page de téléchargement](https://www.virtualbox.org/wiki/Downloads) du site officiel, choisir la version correspondant à votre machine hôte.

> En cas de problème avec la version 6.0 pour Windows, vous pouvez tenter la version 5.2 pour Windows.

Bonne installation ...

<!-- slide vertical=true -->

![Vbox vide](assets/VBox-vide.png)

VirtualBox sans aucune machine virtuelle.


<!-- slide -->

## Présentation de Linux

[Linux](https://fr.wikipedia.org/wiki/Linux) est un noyau de systèmes d'exploitation pour :
* passerelle domestique [(*Box Internet*)](https://fr.wikipedia.org/wiki/Box_(Internet)) ;
* objet connecté comme [Raspberry Pi](https://fr.wikipedia.org/wiki/Raspberry_Pi) ;
* smartphone basé sur [Android](https://fr.wikipedia.org/wiki/Android) ;
* ordinateur personnel, (alternative libre à Windows) ;
* la majorité des [serveurs informatique](https://fr.wikipedia.org/wiki/Serveur_informatique) ;
* presque tous les [supercalculateurs](https://fr.wikipedia.org/wiki/Superordinateur) ;
* ordinateur d'entreprise sécurisé : banque, armée, ...

<!-- slide vertical=true -->
### Distribution Linux

Une distribution Linux propose :
* un noyau Linux plus ou moins récent, parfois expérimental, parfois très stable ;
* un ensemble de logiciels plus ou moins complet ;
* un gestionnaire de paquets pour en installer d'autres; et poursuivre les mises à jour ;
* d'autres services comme documentation, forum.

> **Exemples** : Manjaro, Linux Mint, Debian, Ubuntu, Fedora, CentOS, Arch.
<!-- slide vertical=true -->

### Le noyau Linux

Le [noyau Linux](https://fr.wikipedia.org/wiki/Noyau_Linux) a été **créé en 1991 par [Linus Torvalds](https://fr.wikipedia.org/wiki/Linus_Torvalds)**.

> Ses caractéristiques principales sont d'être multitâche et multi-utilisateur. Il respecte les normes POSIX ce qui en fait un digne héritier des systèmes UNIX.

Il est écrit essentiellement en langage C, par des milliers de bénévoles et salariés en travail collaboratif sur Internet.

<!-- slide vertical=true -->

### Les logiciels disponibles

* Des navigateurs web : [Mozilla Firefox](https://fr.wikipedia.org/wiki/Mozilla_Firefox), [Chromium](https://fr.wikipedia.org/wiki/Chromium), ...
* Des applications multimédia : [VLC](https://fr.wikipedia.org/wiki/VLC_media_player), [GIMP](https://fr.wikipedia.org/wiki/GIMP), [OBS](https://fr.wikipedia.org/wiki/Open_Broadcaster_Software), ...
* Des suites bureautiques comme [LibreOffice](https://fr.wikipedia.org/wiki/LibreOffice) ;
* Des interpréteurs pour les langages Bash, Python, OCaml, ...
* Des compilateurs pour les langages C, C++, java, ...
* Des [éditeurs de texte](https://fr.wikipedia.org/wiki/%C3%89diteur_de_texte), et des environnement de développement intégrés, ...
* De nombreux logiciels éducatifs comme [GeoGebra](https://fr.wikipedia.org/wiki/GeoGebra), [GCompris](https://fr.wikipedia.org/wiki/GCompris), [Stellarium](https://fr.wikipedia.org/wiki/Stellarium), ...
* Des [jeux](https://www.dotslashplay.it/) ...

<!-- slide vertical=true -->

### Les gestionnaires de paquets

Ils permettent de gérer les mises à jour et l'installation de logiciels via des paquets :

* `dpkg` avec le format [.deb](https://fr.wikipedia.org/wiki/Deb), pour Debian, Ubuntu, Linux Mint, ...
* `rpm` avec le format [.rpm](https://fr.wikipedia.org/wiki/RPM_Package_Manager), pour Red Hat, Fedora, CentOS, ...
* [pacman](https://fr.wikipedia.org/wiki/Pacman_(Arch_Linux)) est le gestionnaire pour Manjaro, Arch...

<!-- slide vertical=true -->

### Les environnements de bureau

Un [environnement de bureau](https://fr.wikipedia.org/wiki/Environnement_de_bureau) est un ensemble de logiciels qui donne une cohérence graphique à l'ensemble d'une distribution et en permet le réglage.


**Exemples** basés sur GTK : [GNOME](https://fr.wikipedia.org/wiki/GNOME), [Cinnamon](https://fr.wikipedia.org/wiki/Cinnamon_(logiciel)), [Xfce](https://fr.wikipedia.org/wiki/Xfce), ...

**Exemples** basés sur Qt : [KDE](https://fr.wikipedia.org/wiki/KDE), [LXQt](https://fr.wikipedia.org/wiki/LXQt), ...


> [GTK](https://fr.wikipedia.org/wiki/GTK_(bo%C3%AEte_%C3%A0_outils)) et [Qt](https://fr.wikipedia.org/wiki/Qt) sont des bibliothèques graphiques, un ensemble d'outils.

<!-- slide vertical=true -->

### Quelques exemples

[DistroWatch](https://distrowatch.com/) présente les distributions populaires.

 Chaque distribution peut proposer plusieurs gestionnaire de bureaux. Exemples :

* [Manjaro](https://manjaro.org/) : avec Xfce ; [lien direct]()
* [Linux Mint](https://linuxmint.com) : avec Cinnamon ; [lien direct](https://linuxmint.com/download.php)
* [Fedora](https://getfedora.org/) : avec GNOME ; [lien direct](https://getfedora.org/fr/workstation/download/)
* [Debian](https://www.debian.org/) : avec KDE ; [lien direct](https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/)
* [Ubuntu](https://ubuntu.com/) avec LXQt ; [lien direct](https://lubuntu.me/downloads/)

Il suffit de télécharger une image disque (fichier .iso).

<!-- slide -->

## Création d'une machine virtuelle

On poursuit ici l'expérience avec [Linux Mint Debian Edition (LMDE 4)](https://blog.linuxmint.com/?p=3867).
> Mint est, par défaut, basée sur Ubuntu qui, elle-même est basée sur Debian. LMDE est basée directement sur Debian.

<!-- slide vertical=true -->

1. On télécharge l'image disque de 1.9 Go.
    * Avec le [nœud BitTorrent Transmission](https://fr.wikipedia.org/wiki/Transmission_(logiciel)), ou
    * avec le miroir de téléchargement de son choix.
2. On [vérifie l'intégrité](https://linuxmint.com/verify.php) du téléchargement.
    * C'est optionnel ici ; uniquement pour un test.
    * C'est important en production ; sécurité !
    * Un torrent est auto vérifié ; bonne pratique.
3. On dispose d'une image disque :
    * elle pourrait être graver sur un DVD,
    * on pourrait créer une clé USB bootable avec,
    * plaçons-la dans une machine virtuelle !

<!-- slide vertical=true -->

On utilise VirtualBox :
1. On crée une **nouvelle** machine ; <kbd>Ctrl</kbd>+<kbd>N</kbd> ;
2. On l'appellera `Debian Mint`

![Nouvelle machine](assets/création.png)

<!-- slide vertical=true -->

3. On offre au moins 1024 Mo de mémoire vive, **2048 Mo de préférence**, pour la machine invitée.
4. On crée un disque dur virtuel maintenant, de type VDI, dynamiquement alloué.
5. **Modifier son nom**, et **choisir une taille de 20Go**.

![](assets/disque.png)

<!-- slide vertical=true -->

Notre machine virtuelle est crée, elle possède :
* un procésseur virtuel,
* de la mémoire virtuelle,
* une carte vidéo virtuelle et sa mémoire,
* une carte réseau, une carte sons, des ports USB, ...
* un lecteur DVD virtuel vide,
* un disque virtuel vide !

<!-- slide vertical=true -->

Dans la configuration ( <kbd>Ctrl</kbd>+<kbd>S</kbd> ) de cette machine, on va insérer notre disque virtuel téléchargé.

Dans `stockage`, on clique sur `vide` dans le contrôleur IDE, puis (à droite) dans attributs, lecteur optique, on clique sur l'icône de DVD à droite et son menu... `Choisissez un fichier de disque virtuel` ; on sélectionne notre image .iso.

![](assets/choix_disque.png)

<!-- slide vertical=true -->

On peut fermer la configuration et démarrer la machine virtuelle.
* Elle va booter sur le DVD virtuel pour la première fois.
* On va installer le système sur le disque virtuel.
* On retirera le DVD virtuel.
* Aux redémarrages suivants, la machine bootera sur le disque dur.
* Notre machine sera prête !

> L'origine du verbe *booter* est en rapport avec [*bootstrap*](https://fr.wiktionary.org/wiki/bootstrap).

<!-- slide --> 

## 1er Démarrage en *live*

![](assets/boot1.png)

<!-- slide vertical=true -->

* Notre clavier sera capturé dans la machine virtuelle,
* on peut voir l'écran virtuel de démarrage.
* La souris sera également capturée.
* On pourra cocher 'ne plus afficher ce message'.
* `Start LMDE 4`.

Quand La machine a fini de booter :
* On peut la tester, ses logiciels, ses paramètres, ...
* On va installer cet O.S. sur le disque dur virtuel.

<!-- slide vertical=true -->

![](assets/écran1.png)


<!-- slide vertical=true -->

![](assets/total.png)
Cette machine invitée est une application parmi d'autres du système hôte.

<!-- slide vertical=true -->

Dans le menu de VirtualBox, choisir `Écran`, puis `Mode plein écran`.

**Attention**, pour en sortir, on pourra déplacer notre souris tout en bas de l'écran, pour faire apparaître le menu de la machine virtuelle.

> Il y a un raccourci clavier qui pourrait être <kbd>Ctrl(droit)</kbd>+<kbd>F</kbd> .
> Dans ce cas, la touche <kbd>Ctrl(droit)</kbd> est votre touche <kbd>**Host**</kbd>.


<!-- slide --> 

## Installation virtuelle

Il vaut mieux ici être en mode plein écran.

* On double clique (ou bien un seul clic + <kbd>Entrée</kbd>) sur `Install Linux Mint`
* On répond à la langue que l'on souhaite pour l'installation ; c'est au choix !
* On choisit son fuseau horaire.
* On choisit sa disposition de clavier. **Attention**, il vaut mieux choisir `French (alt.)`. Explications à venir... On pourra écrire très facilement les caractères ÇÉÈÖËœŒæÆ×÷¡¿…


<!-- slide vertical=true -->

![](assets/clavier.png)

`French (alt.)` est un très bon choix.

<!-- slide vertical=true -->

* On entre les paramètres de l'administrateur.
* Majuscules et espaces possibles pour le nom.
* Majuscules et espaces **interdites** pour le nom de la machine. [Tiret bas](https://fr.wikipedia.org/wiki/Tiret_bas) ( `_` ) possible.
* Majuscules et espaces **interdites** pour le nom d'utilisateur (*login*).
* On **note soigneusement** un bon mot de passe.
* Pour un premier test, on peut choisir : `Se connecter automatiquement`.

<!-- slide vertical=true -->

![](assets/compte.png)

<!-- slide vertical=true -->

**Pour une première installation avec VirtualBox seulement !!!**

On peut faire une `installation automatisée` ; Effacer un disque et y installer LMDE. On choisit le `VBOX_HARDDISK`.

> Le disque dur en question est le disque virtuel ; aucun problème, il est vide.

**Quand vous ferez une installation sur une machine réelle, soyez prudent, ce sera peut-être différent.**

<!-- slide vertical=true -->

![](assets/type_install.png)

<!-- slide vertical=true -->

![](assets/confirm.png)

`VBOX_HARDDRIVE` est bien notre disque virtuel, il est vide, il lui faut une table des partitions. Toutes les données seront effacées, oui, mais il n'y a aucune en même temps.
* On clique sur `Oui`.

<!-- slide vertical=true -->

On continue avec l'installation du chargeur de démarrage `GRUB`. C'est lui qui donne un menu quand plusieurs systèmes d'exploitation sont disponibles au moment du *boot*.
* Ici, on laisse le choix par défaut. `/dev/sda` désignera le descripteur de notre unique disque virtuel.
    * `dev` est un répertoire Linux en lien avec les périphériques (_**dev**ices_).
    * `sda` est le premier disque dur branché en SCSI sur la carte mère. [(*more info in english*)](https://en.wikipedia.org/wiki/Device_file#Naming_conventions)


<!-- slide vertical=true -->

![](assets/Résumé.png)

Un dernier coup d'œil avant l'installation.

<!-- slide vertical=true -->

![](assets/Install.png)

L'installation va prendre plusieurs minutes.

<!-- slide vertical=true -->

Une fois l'installation terminée :

* On peut redémarrer cette machine virtuelle et la faire booter sur le disque dur virtuel au lieu du DVD virtuel. Il **faut** bien éjecter le DVD virtuel avant le redémarrage. C'est souvent automatique (mais pas toujours). Sinon, on boote à nouveau sur le DVD prêt à refaire une installation...
* Pour vérifier que le DVD a bien été éjecté, aller dans le menu `Périphériques` de la machine virtuelle, puis dans `lecteurs optiques`.

![](assets/eject.png)