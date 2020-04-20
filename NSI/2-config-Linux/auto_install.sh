echo "Vérification des mises à jour..."
apt-get update && apt-get upgrade && echo "Système à jour !"
echo ==============================================
echo "Installation de chromium et d'extensions pour chromium et Firefox..."
apt-get install -qq -y chromium-browser chromium-browser-l10n
apt-get install -qq -y chromium chromium-l10n chromium-ublock-origin
apt-get install -qq -y webext-https-everywhere webext-privacy-badger
echo ==============================================
echo "Installation d'outils système"
apt-get install -qq -y bleachbit
apt-get install -qq -y numlockx
apt-get install -qq -y virtualbox
apt-get install -qq -y libreoffice
echo ==============================================
echo "Installation d'outils graphiques"
apt-get install -qq -y pinta
apt-get install -qq -y scribus
apt-get install -qq -y inkscape
apt-get install -qq -y mypaint mypaint-brushes mypaint-data-extras
apt-get install -qq -y krita krita-l10n
apt-get install -qq -y xaos
apt-get install -qq -y gnome-maps
echo ==============================================
echo "Installation d'outils mathématiques"
apt-get install -qq -y geogebra
apt-get install -qq -y asymptote texlive texlive-lang-french
apt-get install -qq -y texlive-fonts-extra  texlive-science lmodern
apt-get install -qq -y texmaker pandoc evince
echo ==============================================
echo "Installation d'outils de dévellopeurs"
apt-get install -qq -y fonts-inconsolata
apt-get install -qq -y geany
apt-get install -qq -y g++
apt-get install -qq -y bluefish
apt-get install -qq -y fortunes-fr cowsay lolcat
echo ==============================================
echo "Installation éducatifs et multimédia"
apt-get install -qq -y audacious
apt-get install -qq -y stellarium
apt-get install -qq -y vlc
apt-get install -qq -y obs-studio
echo ==============================================
echo "Installation de VSCodium"
wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | apt-key add -
echo 'deb https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/repos/debs/ vscodium main' | tee --append /etc/apt/sources.list.d/vscodium.list
apt update && apt install codium
