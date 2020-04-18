---
export_on_save:
  html: true

presentation:
  width: 1920
  height: 1200
  theme: solarized.css
  margin: 0.1

  progress: true
---

<!-- slide -->

# Navigateurs Web

## Vocabulaire

* [**Internet**](https://fr.wikipedia.org/wiki/Internet) : le réseau physique accessible au public de tous les ordinateurs du monde reliés par une connexion réseau (cable ou sans fil). Il est utilisé au départ :
    * (1972) pour le courrier électronique,
    * (1988 avec IRC) la messagerie instantanée,
    * (1989) le web, qui a popularisé Internet,
    * (1999 avec Napster) le partage de fichier en pair à pair,

* [**Web**](https://fr.wikipedia.org/wiki/World_Wide_Web) (ou *World Wide Web*), inventé en 1989-1990 par **Tim Berners-Lee** suivi de Robert Cailliau, fonctionne sur Internet et permet de consulter des pages avec de l'hypertexte.

* [**Navigateur Web**](https://fr.wikipedia.org/wiki/Navigateur_web) *(Web browser*) : un logiciel conçu pour consulter et afficher le Web. Techniquement, c'est au minimum un client HTTP.

> Chrome, Firefox, Opera, Safari et d'autres sont des navigateurs Web.
> Google, Qwant, Yahoo!, DuckDuckGo et d'autres sont des moteurs de recherche.


<!-- slide vertical=true -->

[Quelques navigateurs](https://fr.wikipedia.org/wiki/Liste_de_navigateurs_web) :

* [**Chrome**](https://www.google.com/chrome/) est un produit de l'entreprise [Google](https://fr.wikipedia.org/wiki/Google), célèbre pour son moteur de recherche éponyme ; *ne pas confondre*. Google (le G de [GAFAM](https://fr.wikipedia.org/wiki/GAFAM)) a dépassé les 1000 milliards de dollars de capitalisation boursière. [Alphabet](https://fr.wikipedia.org/wiki/Alphabet_(entreprise)) est depuis août 2015 la maison mère de Google.

* [**Safari**](https://fr.wikipedia.org/wiki/Safari_(navigateur_web)) est un produit de l'entreprise [Apple](https://fr.wikipedia.org/wiki/Apple) (le premier A de GAFAM), navigateur installé par défaut sur tous les ordinateurs Mac.

* [**Opera**](https://fr.wikipedia.org/wiki/Opera) est un navigateur gratuit (mais pas entièrement libre) et multiplateforme. Plutôt peu utilisé. Il se base désormais sur [Chromium](https://fr.wikipedia.org/wiki/Chromium) (la base de travail de Chrome).

* [~~Internet Explorer~~](https://fr.wikipedia.org/wiki/Internet_Explorer) (ou IE) est un navigateur produit par l'entreprise [Microsoft](https://fr.wikipedia.org/wiki/Microsoft) (le M de GAFAM) qui conseille depuis février 2019 ne plus l'utiliser.

* [**Edge**](https://fr.wikipedia.org/wiki/Edge_(navigateur_web)) est le remplaçant de IE par Microsoft, il se base également sur Chromium.

* [**Firefox**](https://www.mozilla.org/fr/firefox/new/) est un produit de la [fondation Mozilla](https://fr.wikipedia.org/wiki/Mozilla), association à but non lucratif, qui produit des logiciels libres et respectueux de la vie privée.

* [**Chromium**](https://fr.wikipedia.org/wiki/Chromium) est la base de Chrome, et ne contient pas, lui, de mouchards.


> Nous donnerons des conseils pour Firefox et certains seront adaptables à Chromium.

<!-- slide -->

## Moteurs de recherche

Que l'on utilise Firefox, Chromium, Opera, Edge, ou un autre navigateur web, on peut utiliser des moteurs de recherche variés. [Les plus connus sont](https://fr.wikipedia.org/wiki/Liste_de_moteurs_de_recherche) :

* [Alta Vista](https://fr.wikipedia.org/wiki/AltaVista) très utilisé avant les années 2000. **Fermé**
* [Google](https://fr.wikipedia.org/wiki/Google_(moteur_de_recherche)) actuellement en position de quasi monopole.
* [Yahoo!](https://fr.wikipedia.org/wiki/Yahoo!), [Bing](https://fr.wikipedia.org/wiki/Bing_(moteur_de_recherche)), [Qwant](https://fr.wikipedia.org/wiki/Yahoo!) sont connus en France et à l'étranger.
* d'autres connus plutôt en Chine ou en Russie.

Pour assurer la protection de ses données, il est nécessaire d'utiliser un [moteur qui respecte sa confidentialité](https://fr.wikipedia.org/wiki/Liste_de_moteurs_de_recherche#Moteurs_de_recherche_assurant_la_confidentialit%C3%A9_des_recherches) :

* [Starpage](https://fr.wikipedia.org/wiki/Startpage) ne stocke aucune information personnelle. Acquis depuis 2019 par une entreprise publicitaire.
* [DuckDuckGo](https://fr.wikipedia.org/wiki/DuckDuckGo), ne stocke rien non plus, mais peut relayer des liens publicitaires.
* [Qwant](https://fr.wikipedia.org/wiki/Qwant) est [**recommandé**](https://fr.wikipedia.org/wiki/Socle_interminist%C3%A9riel_de_logiciels_libres) par l'État français, mais n'est pas libre.

> Nous suivrons **ici** les recommandations, même si les deux précédents semblent souvent plus pertinents en réponses.

<!-- slide vertical=true -->

La bonne gestion des ses données personnelles est essentielle. Le [RGPD](https://fr.wikipedia.org/wiki/R%C3%A8glement_g%C3%A9n%C3%A9ral_sur_la_protection_des_donn%C3%A9es) est pensé pour vous protéger.
> [Si vous êtes le produit, ce n’est pas gratuit.](https://www.laquadrature.net/2016/08/17/si-vous-etes-le-produit/)

La réciproque "Si c'est gratuit, c'est vous le produit" est fausse ; il existe des logiciels libres et gratuits qui ne vous étudient pas.

> Par contre, Google, Facebook, et d'autres proposent des services gratuits qui leur rapportent **beaucoup** !

<!-- slide vertical=true -->

On peut avoir plusieurs moteurs de recherche, en avoir un par défaut et d'autres en utilisation ponctuelle.

Avec Firefox sous Linux Mint, on peut en [ajouter](https://www.linuxmint.com/searchengines.php), comme
* [IMDb](https://www.linuxmint.com/searchengines/anse.php?sen=IMDB&c=y) pour le cinéma (IMDb appartient à Amazon);
* [Github](https://www.linuxmint.com/searchengines/anse.php?sen=Github&c=y) pour le dépôt de code (Github appartient à Microsoft)
* [Facebook](https://www.linuxmint.com/searchengines/anse.php?sen=Facebook&c=y) un réseau social (le F de GAFAM)
* [Google](https://www.linuxmint.com/searchengines/anse.php?sen=Google&c=y) qui n'est pas inclus par défaut.

Mais on peut aussi surtout ajouter et utiliser des moteurs qui respèctent votre vie privée :
 * [Qwant](https://www.linuxmint.com/searchengines/anse.php?sen=Qwant&c=y)
 * DuckDuckGo et StartPage sont déjà inclus.

>**Conseils** : 
>* choisir un de ces trois en moteur de recherche par défaut,
>* n'utiliser Google qu'à certaines occasion, dans une fenêtre de navigation privée.
