# IHM mode texte - Partie 2 {ignore=true}
> Édition de code dans un terminal


@import "abstract.md"


## Sommaire de la partie 2 {ignore=true}

[TOC]

## Introduction

### Les éditeurs en mode texte

Il existe plusieurs éditeurs en mode texte, que l'on peut intégrer dans un terminal. Les plus connus sont, par ordre alphabétique :
 * Emacs
 * micro
 * nano
 * Vim

Emacs et Vim seront peut-être un choix judicieux pour une utilisation intensive, plus tard, mais pas pour découvrir l'édition de code.

**micro** se présente comme le successeur de nano et offre des raccourcis claviers plus usuels et aussi plus de possibilités.

Nous utiliserons donc **micro** pour cette activité, et montrerons quelques possibilités utiles.

### Objectifs
* Éditer un fichier texte, ou un script.
    * Faire des sélections.
    * Utiliser le couper/copier/coller.
    * Utiliser plusieurs curseurs.
    * Utiliser une fonction pour remplacer du texte par un autre.
* Obtenir sur un même écran, une fenêtre d'édition de code et une fenêtre de terminal de commande.
* Comprendre la notion de _buffer_.

## Raccourcis claviers (_bindings_) de **micro**

### La liste principale
<kbd>Alt</kbd>+<kbd>G</kbd> affiche les raccourcis classiques, les plus importants :
* <kbd>Ctrl</kbd>+<kbd>Q</kbd> pour quitter (_**Q**uit_)
* <kbd>Ctrl</kbd>+<kbd>S</kbd> pour sauvegarder (_**S**ave_)
* <kbd>Ctrl</kbd>+<kbd>O</kbd> pour ouvrir (_**O**pen_)
* <kbd>Ctrl</kbd>+<kbd>Z</kbd> pour annuler (_Undo_)
* <kbd>Ctrl</kbd>+<kbd>Y</kbd> pour refaire (_Redo_)
* <kbd>Ctrl</kbd>+<kbd>F</kbd> pour rechercher (_**F**ind_)

### D'autres classiques
Il y a aussi les autres classiques à connaître concernant les selections :
* <kbd>Ctrl</kbd>+<kbd>A</kbd> pour tout sélectionner
* <kbd>Ctrl</kbd>+<kbd>X</kbd> pour couper la sélection
* <kbd>Ctrl</kbd>+<kbd>C</kbd> pour copier la sélection
* <kbd>Ctrl</kbd>+<kbd>V</kbd> pour coller la sélection

Et concernant la duplication ou la suppression
* <kbd>Ctrl</kbd>+<kbd>D</kbd> pour dupliquer une ligne ou la sélection
* <kbd>Ctrl</kbd>+<kbd>K</kbd> pour supprimer une ligne

Ces deux derniers ne sont pas utilisés par tous les éditeurs, mais par plusieurs comme Sublime Text, Geany, micro et d'autres.

### Avec les sélections
* Quand on appuie sur <kbd>Maj.</kbd> (i.e. la touche <kbd>SHIFT</kbd>, ou <kbd>⇧</kbd>) : déplacer le curseur avec les flèches ou la souris construit une sélection.
* Quand on appuie sur <kbd>Ctrl</kbd> : déplacer le curseur avec les flèches se fait mot par mot au lieu de caractère par caractère. On peut le combiner avec <kbd>Maj.</kbd> pour construire rapidement une sélection de mots.
* Les touches <kbd>Début</kbd> (ou <kbd>_Home_</kbd> ou <kbd>🡬</kbd>) et <kbd>Fin</kbd> (ou <kbd>_End_</kbd>) sont aussi utiles.

> **Tous** ces raccourcis claviers sont à connaître ; on les retrouve dans de nombreux logiciels, c'est aussi une raison pour recommander l'utilisation de **micro**.

### Multi-curseur

Une facilité que l'on retrouve avec certains éditeurs est le multi-curseur. En appuyant sur <kbd>Ctrl</kbd> et en cliquant dans un texte, on fait apparaître un curseur de plus, c'est utile pour modifier plusieurs lignes à la fois, en ajout/suppression.

On sort du mode multi-curseur en appuyant sur <kbd>Échap</kbd>.

### La notion de _buffer_

_Buffer_
: Un _buffer_ est (pour son aspect visible) un panneau rectangulaire qui affiche le contenu d'un fichier en cours d'édition. Un _buffer_ est surtout l'état en mémoire vive de ce fichier ; on peut le sauvegarder sur support permanent comme un disque dur ou la mémoire _flash_ d'une tablette. On peut aussi recharger le _buffer_ si la version enregistrée est différente ; par exemple si le fichier a été modifié par un autre programme.

## Le mode commande de **micro**

Il est possible de partager l'écran de micro en deux parties ou plus, un partage vertical ou horizontal du _buffer_ actuel (la fenêtre active).

Il est possible d'effectuer des recherches et des remplacements de texte dans un document.

Il est possible d'avoir un buffer avec une invite de commande Bash à l'intérieur de micro, et bien d'autres choses.

> À partir d'un buffer, on entre sur <kbd>Ctrl</kbd>+<kbd>E</kbd> pour obtenir l'invite de commande de micro. C'est un **CLI** ! L'invite de commande de micro est `>`.

Quelques commandes micro disponibles :
* `> vsplit`
* `> hsplit`
* `> replace machin chose`
* `> term`


---

À compléter...