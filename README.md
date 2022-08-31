# CLIENT TCP AVEC INTERFACE GRAPHIQUE

Ce logiciel est un client TCP qui permet de recevoir un message via le protocole TCP venant d'un serveur 
puis de l'interpréter afin d'effectuer une action graphique, logicielle ou mécanique sur un relais par exemple.
Sur windows il comporte en plus un système de sauvegarde de configuration et d'un système d'envoi de mail. 
Des logs sont également gérer et stockés dans le répertoire _C:/User/Program Files/BROADCAST SOLUTION_ .

Ce logiciel à été concu pour une utilisation en radio pour permettre au studio d'envoyé des informations
sur un studio déporté à l'autre bout de la planète. Mais il peut être adapté à toutes situations.

***

## Prérequis
- Raspberry PI 4 (2,4,8G) ([Raspberry](https://www.kubii.fr/cartes-raspberry-pi/2772-nouveau-raspberry-pi-4-modele-b-4gb-kubii-0765756931182.html)).
- (optionnel) PiFace digital 2 ([PiFace](https://shop.mchobby.be/fr/pi-hats/221-piface-digital-2-pour-raspberry-pi-3232100002210.html)).
- Carte SD ([Carte SD](https://www.amazon.fr/SanDisk-M%C3%A9moire-microSDHC-Adaptateur-homologu%C3%A9e/dp/B08GY9NYRM/ref=sr_1_7?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3GQ2WS313G7WF&keywords=carte%2Bsd%2Bmicro%2B32&qid=1655934994&sprefix=carte%2Bsd%2Bmicro%2B32%2Caps%2C73&sr=8-7&th=1)).
- Alimentation Raspberry ([Alimentation](https://www.kubii.fr/alimentations/2678-alimentation-officielle-usb-type-c-raspberry-pi-3272496300002.html)).
- Ecran 16:9 avec entrée HDMI.
- Cable micro HDMI vers HDMI.
- Raspberry Imager ([Téléchargement](https://www.raspberrypi.com/software/)).
- Un clavier et une souris pour la première configuration du RPI.
***

## Compatible avec :
- Raspberry Pi 4 ([Raspberry](https://www.kubii.fr/cartes-raspberry-pi/2772-nouveau-raspberry-pi-4-modele-b-4gb-kubii-0765756931182.html)).
- Carte PiFace digital 2 ([PiFace](https://shop.mchobby.be/fr/pi-hats/221-piface-digital-2-pour-raspberry-pi-3232100002210.html)).
- Médialon Manager ([Téléchargement](https://medialon.com/products/medialon-manager/) )
- Tout système comportant un serveur TCP

## Installation sur Raspberry Pi 4
- Flasher Raspbian Desktop sur la carte SD avec Raspberry Imager.
  - Prendre la version Raspberry pi OS 64bits avec Bureau.
- Brancher votre RPI au secteur tout en aillant installé et branché votre écran, clavier, souris et avoir inséré votre carte SD avec le système d'exploitation.
  - Suivez les instructions du premier démarrage du RPI.
  - (optionnel) Après avoir terminé la configuration du premier démarrage, il faut se rendre dans la framboise en haut à gauche > préférences > configuration du RPI > Display > et passer Screen Blanking à OFF (Mise en veille de l'écran).
- Mettre à jour le raspberry (`sudo apt-get update & sudo apt-get upgrade -y`) :
  - Faire un `sudo apt autoremove` si des paquets ne sont plus utilisés.
  - Faire un reboot du RPI après la mise à jour `sudo reboot`.
- (optionnel) Installer la carte PiFace sur le raspberry.
- **ATTENTION** Activer la fonction SPI du raspberry pour la prise en charge de la carte PiFace :
  - `sudo raspi-config` > Interface Options > SPI > Enable
- Installer PIP pour python 3 s'il n'est pas installé :
  - `sudo apt install python3-pip`
- Installation des librairies requises pour la carte PiFace.
  - `sudo pip3 install pifacecommon`
  - `sudo pip3 install pifacedigitalio`
  - Tuto complet [ici](https://github.com/piface/pifacedigitalio)

- Mise en place du programme sur le RPI :
  - Télécharger la version du programme sur github avec `sudo wget https://raw.githubusercontent.com/corentindrd/RPI_PIFACE_RADIO_BROADCAST/master/main.py`.
  - Changer l'adresse IP par l'adresse de votre serveur dans la variable "ipaddress" en éditant le fichier avec `sudo nano main.py`. 
  - Changer le numéro de port par celui souhaité dans la variable "port" en éditant le fichier avec `sudo nano main.py`.
- Lancement du programme avec `sudo main.py`

## Installation sur Ubuntu
- Télécharger la version du programme souhaitée sur github avec `sudo wget https://raw.githubusercontent.com/corentindrd/RPI_PIFACE_RADIO_BROADCAST/master/main.py`.
- Télécharger tkinter qui n'est pas présent de base sur Ubuntu avec `sudo apt-get install python3-tk`
- Changer l'adresse IP par l'adresse de votre serveur dans la variable "ipaddress" en éditant le fichier avec `sudo nano main.py`. 
- Changer le numéro de port par celui souhaité dans la variable "port" en éditant le fichier avec `sudo nano main.py`.
- Lancement du programme avec `sudo main.py`

#### Lancement automatique au démarrage du RPI :
- Ouvrir un terminal.
`sudo nano /etc/xdg/lxsession/LXDE-PI/autostart`  
Rajouter en bas du fichier `@sudo python3 main.py`
#### ❗ Problèmes connus Raspberry❗:
- Le programme ne se lance pas au démarrage du RPI :
  - Le fichier main.py n'est pas dans le bon répertoire, le fichier autostart est défini de base dans le répertoire `/home/pi/`  
  Si le programme est dans un autre répertoire il faut l'indiquer dans le fichier autostart EXEMPLE : `@sudo python3 /home/pi/radio/main.py`
- "_No PiFace Digital board detected_":
  - Enlever et remettre la carte sur le RPI puis relancer le programme.
  - Refaire la procédure d'installation des librairies.
#### ❗ Problèmes connus windows❗:

***
## CHANGELOG
### V1.4.0
#### **Principaux ajouts (windows) :**
- **Arrivée du programme sur windows :**
  - Système de sauvegarde de configuration
  - Bouton paramètres avec interface graphique ayant la possibilité de changer les informations : réseau (adresse IP et port) , messages provenant du serveur
  - Ajout d'un système d'envoi de mail (fonction actuellement en test) fonctionnant avec GMAIL en créant un mot de passe pour application avec votre adresse GMAIL ([APP Password](https://myaccount.google.com/apppasswords))
  - Ajout d'un bouton qui permet de redémarrer le client
#### **Améliorations et divers (windows) :**
- Ajout d'un bouton quitter en haut à droite 
#### **Principaux ajouts (linux) :**
- Ajout de voyants :
  - Voyant _PiFace_ pour savoir si votre carte PiFace est bien installée et reconnue
  - Voyant _Librairies_ pour savoir si toutes les librairies nécessaires ont bien été chargée et correctement installés
  - Voyant _Serveur_ pour savoir si la connexion au serveur est bien active
### V1.3.3
#### **Principaux ajouts :**
- Refonte complète du système de chronomètre pour diminuer la charge système.
  - Suppression de la fonction _start_chronometer_
  - Suppression de la fonction _stop_chronometer_
  - Suppression de la fonction _resume_chronometer_
  - Ajout de la fonction _updateTime_ qui gère le chronomètre
  - Ajout de la librarie timeit qui est utilisée pour le chronomètre
#### **Améliorations et divers :**
- Nettoyage du code
  - Nettoyage au niveau de l'utilisation de la carte électronique PiFace
  - Suppression de la fonction _input_read_ qui était inutilisée
  - Suppression du _thread 3_ qui était inutilisé
### V1.3.2
#### **Améliorations et divers :**
- Ajout de variables pour simplifier le changement d'informations concernant le serveur distant
  - variable "ipaddress" qui permet de changer l'adresse IP du serveur plus facilement.
  - variable "port" qui permet de changer le port de connexion au serveur plus facilement.
- Le chrono ne s'affiche plus au lancement du programme tant que le serveur n'a pas envoyé l'information ON AIR.
- Nettoyage du code
  - Nettoyage au niveau des importations.
  - Nettoyage au niveau des commentaires.
### V1.3.1
#### **Améliorations et divers :**
- Diminution du lag des secondes entre l'heure et les points jaunes des secondes.
  - La fonction des heures a été déplacée dans la fonction trigonométrie pour éviter la latence.
  - La fonction "second" a été supprimée pour éviter la latence.
### V1.3.0
#### **Principaux ajouts :**
- L'heure du milieu disparaissait à certains moments lors du changement de seconde.
  - Le texte n'est désormais plus géré par la fonction _canvas_ de tkinter, il est maintenant géré par la fonction _Label_ de tkinter.
- Le programme s'arrête complètement après la fermeture de la page, ce qui n'était pas le cas avant.
  - L'attribut "daemon" de tous les threads a été ajoutée et initialisée à "True".
#### **Améliorations et divers :**
- La variable _initial_screen_ a été créée pour la valeur _1920_ qui est la valeur initiale qui permet le calcul de la mise à l'échelle d'écran.
- La fonction datetime pour la trigonométrie des secondes a été améliorée.
### V1.2.1
#### **Améliorations et divers :**
- La variable "canvas_size" n'était pas initialisée.
- Changement des valeurs initiales des éléments qui étaient trop grandes sur certains écrans.
### V1.2.0
#### **Principaux ajouts :**
- Le programme fonctionne même sans la carte électronique PiFace installée.
### V1.1
#### **Principaux ajouts :**
- La latence entre les secondes de l'heure et les secondes s'affichant en jaune a été réduite.
- Disposition des éléments graphiques améliorés
  - Le titre ONAIR se place automatiquement en haut en fonction de la taille de l'écran.
  - Le chronomètre se place automatiquement en bas en fonction de la taille de l'écran.
  - L'horloge se met au centre en fonction de la taille de l'écran.
#### **Améliorations et divers :**
- Nettoyage du code sur les fonctions de créations (chronomètre et titres).
- Suppression de la variable "msgserver" qui ne servait à rien.
- Suppression de la police de l'heure qui était en gras vers une police normale.
- La fonction de lecture des entrées de la carte a été retirée

### V1.0
- Programme initial
***

## Crédits
- Stéphane Ayreault
- Mathieu Amiaud
- Aurélien Ménard
***

