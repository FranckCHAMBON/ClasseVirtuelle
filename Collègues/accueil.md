# Outils utiles pour les enseignants

Je vous livre à la première personne mon sentiment sur quelques logiciels que je pratique au quotidien.
J'en ai testé d'autres aussi, et parfois je ne les recommande pas du tout. Ça reste mon sentiment du moment.

## TL;DR

En résumé.
* Je milite pour plus d'utilisation de GeoGebra, au collège, comme au lycée.
* Ensuite, je recommande aux programmeurs débutants :
    * Jupyter pour créer des contenus scientifiques, ou faire de petits scripts Python.
    * Geany pour coder en Python, et résoudre ses premiers problèmes.
* Pour les utilisateurs avancés :
    * VSCodium pour presque tout faire.
* Pour les pros, vous savez déjà...



## GeoGebra

Réflexe à avoir pour presque tout schéma en classe virtuelle (entre autres utilisations), quelle que soit la matière.
* Avec ou sans grille.
* Facilité de dessiner des formes simples, tout comme des **vecteurs**.
* On peut même dessiner des tableaux de variations facilement...
* On peut écrire du texte, et des formules $\LaTeX$.
* Tout le monde connaît GeoGebra, mais il n'est pas assez mis en avant. Son utilisation au collège devrait être prolongée encore au lycée, par les enseignants et les élèves.
* Sur tablette, avec un petit stylet, on ajoute de la précision à ses schémas.

> Bientôt, un petit topo, avec des images.

## Un bon éditeur Markdown

Pour être productif, et pouvoir partager et remobiliser des ressources, il n'y a pas mieux que le **Markdown**.

### Qualités
* C'est un langage de balisage léger, il en est le **plus répandu**.
* On ne peut pas faire plus rapide pour créer une page web telle que celle-ci. On peut créer des documents facilement accessibles en ligne, sur PC ou smartphone ; l'affichage s'adapte, contrairement à un document ayant une mise en page figée, prêt à être imprimé. Qui imprime encore ?
* Un processeur de document comme LibreOffice ou Word entremêlent trop le fond et la forme, et il est difficile d'extraire le fond pour le remobiliser. Ils ne devraient pas être utilisés pour le partage des sources de document, mais juste pour produire *à la rigueur* des documents finis à destination de l'impression.
* Le code source d'un document Markdown est lisible par un humain, ce qui n'est pas le cas des outils évoqués juste avant. On peut même se contenter de travailler en ne voyant que le code source.
* On voit toutes les balises ; tout est explicite. Il n'y a rien de caché.
* Le code source est un fichier texte, et il est très facile :
    * de copier coller rapidement des morceaux,
    * de fabriquer des fonctions pour créer automatiquement du contenu,
    * d'inclure des formules mathématiques,
    * ...
* On peut exporter son travail en HTML avec une feuille CSS de son choix.
* On peut aussi créer des présentations page par page.
* On peut inclure facilement un code source en Python, et avoir un rendu avec la coloration syntaxique automatiquement.
* On peut inclure facilement des éléments embarqués de HTML.
* On retrouve son utilisation de plus en plus dans les forums et autres applications sur les réseaux sociaux, en particulier [GitHub](https://github.com/) et [StackExchange de la langue française](https://french.stackexchange.com/)
* De nombreuses applications existent pour créer ou visualiser, comme [StackEdit](https://stackedit.io/), ou bien **CodiMD** qui est basé sur [HackMD](https://hackmd.io/#)



### Défauts
* Il existe quelques variantes du Markdown ; le langage n'est pas totalement unifié. Il y a aussi plusieurs moteurs de rendus.
    * Nous ne présenterons donc que **la partie commune**.

### Quel éditeur ?

Plusieurs possibilités.

1. Pour tester la première fois, un éditeur en ligne est idéal. C'est bien de ne pas être seul...
    * [StackEdit](https://stackedit.io/) ; idéal pour les tous premiers jets.
    * Les cellules Markdown dans un [carnet Jupyter en ligne](https://jupyter.org/try).
        * Cliquer sur `Try JupyterLab`, ou bien `Try Jupyter Notebook` (ancienne version)
        * Attendre un peu.
        * Cliquer sur `File`, `New Notebook`, `Python 3`
        * On a des cellules de `Code` (Python 3), mais on peut les changer en `Markdown`.

2. Pour commencer à créer.
    * Vous pouvez suivre mon [premier cours sur Jupyter](https://htmlpreview.github.io/?https://raw.githubusercontent.com/FranckCHAMBON/Python-Lycee/master/Python-Carnets/Python-Jupyter-1.html).
    * Créer vos propres carnets avec Jupyter !

3. Ensuite, vous êtes à l'aise avec Markdown ; on peut utiliser son éditeur préféré.
    * Cela peut être un éditeur minimaliste, comme [Micro](https://micro-editor.github.io/), que je recommande en mode minimaliste.
    * Cela peut être [Geany](https://www.geany.org/), en lui ajoutant le *plugin* Markdown. Un éditeur généraliste léger à recommander aux débutants.
    * Un éditeur puissant comme [VSCodium](https://vscodium.com/). C'est l'éditeur idéal du moment pour l'utilisateur un peu avancé. Ma [présentation de VSCodium](https://franckchambon.github.io/ClasseVirtuelle/NSI/5-%C3%89diteurs/vscodium.html).
    * Ou bien votre éditeur préféré, avec lequel vous êtes à l'aise.

## Un bon éditeur Python

Ma [présentation assez complète de Python au lycée](https://htmlpreview.github.io/?https://github.com/FranckCHAMBON/Python-Lycee/blob/master/Python-Presentation/Python-Presentation.html).

En résumé :

### En ligne ; sans inscription
* [Python Tutor](http://pythontutor.com/visualize.html#mode=edit) ; pratique pour voir pas à pas un tout petit script.
* [Ideone](https://ideone.com/) ; complet et pratique pour préparer une entrée standard à l'avance.

Il existe d'autres solutions, mais avec inscription, je les disqualifie, en attendant des solutions intégrées aux ENT d'établissement. À suivre : Capytale.

### Sur tablette
* [QPython](https://play.google.com/store/apps/details?id=org.qpython.qpy)
* [Termux](https://termux.com/)

### Sur PC
* Utiliser FranceIOI, Prologin, ...
* Jupyter, et Thonny pour les débutants complets.
* Ensuite Geany est très bien en premier éditeur généraliste.
* Enfin, VSCodium pour les élèves en NSI.

## Outils variés

* [termtosvg](https://github.com/nbedos/termtosvg) un outil génial pour enregistrer une session de code dans un terminal, du bash, du Python, ou tout ce qui peut se faire dans un terminal. Enregistrement **léger** en SVG. On peut le faire lire, mettre en pause, et sélectionner du code. Et c'est très joli !
* [scrcpy](https://github.com/Genymobile/scrcpy) idéal pour connecter une tablette, ou un téléphone sur un PC. On en prend le contrôle avec clavier et souris, on a un partage d'écran à proposer en visio. C'est un super outil.

> Je présente plusieurs outils en détail dans mon cours [IHM en mode texte](https://franckchambon.github.io/ClasseVirtuelle/NSI/Termux/0-termux.html), il est encore inachevé...
