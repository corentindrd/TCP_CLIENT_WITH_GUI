# RPI PIFACE RADIO BROADCAST

Ce programme est un client TCP de réception de trame venant d'un serveur.  
Il est utilisé afin de récupérer une trame TCP venant d'un serveur installé dans un studio afin d'avoir un retour d'information lorsque l'animateur est à l'antenne.  
Un chronomètre est aussi disponible afin que l'animateur sache son temps de parole.  

Fonctionnement:
- Python 3
- Interface graphique pour supporter tkinter
- Carte IN OUT Piface Digital 2
***

## Prérequis
- Raspberry PI 4 (2,4,8G) ([Raspberry](https://www.kubii.fr/cartes-raspberry-pi/2772-nouveau-raspberry-pi-4-modele-b-4gb-kubii-0765756931182.html))
- PiFace digital 2 ([PiFace](https://shop.mchobby.be/fr/pi-hats/221-piface-digital-2-pour-raspberry-pi-3232100002210.html))
- Carte SD ([Carte SD](https://www.amazon.fr/SanDisk-M%C3%A9moire-microSDHC-Adaptateur-homologu%C3%A9e/dp/B08GY9NYRM/ref=sr_1_7?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3GQ2WS313G7WF&keywords=carte%2Bsd%2Bmicro%2B32&qid=1655934994&sprefix=carte%2Bsd%2Bmicro%2B32%2Caps%2C73&sr=8-7&th=1))
- Alimentation Raspberry ([Alimentation](https://www.kubii.fr/alimentations/2678-alimentation-officielle-usb-type-c-raspberry-pi-3272496300002.html))
- Ecran 16:9 avec entrée HDMI
- Cable micro HDMI vers HDMI
- Raspberry Imager ([Téléchargement](https://www.raspberrypi.com/software/))
- FileZilla pour l'envoi de fichier par FTP ([Téléchargement](https://filezilla-project.org/download.php?type=client))
- Un clavier et une souris pour la première configuration du RPI
***
## MISE EN PLACE DU PROGRAMME
Pour une bonne utilisation du programme en fonction de votre installation il suffit de changer l'adresse IP et le port à la ligne 123 et 148
avec les informations correspondantes de votre serveur TCP.
## INSTALLATION RPI

- Flasher Raspbian Desktop sur la carte SD avec Raspberry Imager.
  - Prendre la version Raspberry pi OS 4 avec Bureau.
  - Activer le SSH afin de rendre la première installation plus simple (CTRL+MAJ+X sur RPI imager pour activer le SSH).
- Brancher votre RPI au secteur tout en aillant installé et branché votre écran, clavier, souris et avoir inséré votre carte SD avec le système d'exploitation.
  - Suivez les instructions du premier démarrage du RPI.
  - Après avoir terminé la configuration du premier démarrage, il faut se rendre dans la framboise en haut à gauche > préférences > configuration du RPI > Display > et passer Screen Blanking à OFF (Mise en veille de l'écran).
- Mettre à jour le raspberry (`sudo apt-get update & sudo apt-get upgrade -y`).
  - Faire un `sudo apt autoremove` si des paquets ne sont plus utilisés.
  - Faire un reboot du RPI après la mise à jour `sudo reboot`.
- Installer la carte PiFace sur le raspberry.
- Installer un serveur FTP sur le RPI pour transmettre le programme en réseau pour ne pas utiliser de clé usb ou disque dur externe.
  - `sudo apt install proftpd`
  - Sur FileZilla, rentrer l'adresse IP du RPI et les identifiants sont les mêmes que ceux rentrés au démarrage du RPI.
  - (Tuto [ici](https://raspberry-pi.fr/installer-serveur-ftp-raspberry-pi/) pour les compléments).
- Mettre le fichier Main.py dans le répertoire afficher sur FileZilla.
  - Utiliser la commande `ls` en ouvrant un terminal sur le RPI pour voir si le fichier est bien présent.
- Activer la fonction SPI du raspberry pour la prise en charge de la carte PiFace.
  - `sudo raspi-config` > Interface Options > SPI > Enable
- Installer PIP pour python 3 s'il n'est pas installé.
  - `sudo apt install python3-pip`
- Installation des librairies requises pour la carte PiFace.
  - `sudo pip3 install pifacecommon`
  - `sudo pip3 install pifacedigitalio`
  - Tuto complet [ici](https://github.com/piface/pifacedigitalio)

#### Lancement automatique au démarrage du RPI :
- Ouvrir un terminal.
`sudo nano /etc/xdg/lxsession/LXDE-PI/autostart`  
Rajouter en bas du fichier `@sudo python3 main.py`
#### ❗ Problèmes connus ❗:
- Le programme ne se lance pas au démarrage du RPI:
  - Le fichier autostart qui à été modifier n'est pas le bon car il y a deux répertoires:    
  `/etc/xdg/lxsession/LXDE-PI/autostart` et `/etc/xdg/lxsession/LXDE/autostart` le premier répertoire est le bon.
  - Le fichier main.py n'est pas dans le bon répertoire, le fichier autostart est défini de base dans le répertoire `/home/pi/`  
  Si le programme est dans un autre répertoire il faut l'indiquer dans le fichier autostart EXEMPLE : `@sudo python3 /home/pi/radio/main.py`
- "No PiFace Digital board detected":
  - Enlever et remettre bien la carte sur le RPI puis relancer le programme
  - Refaire la procédure d'installation des librairies

***
## CHANGELOG
### V1.3.1
#### **Améliorations et divers :**
- Diminution du lag des secondes entre l'heure et les points jaunes.
  - La fonction des heures a été déplacée dans la fonction trigonométrie pour éviter la latence.
  - La fonction "second" a été suprrimée pour éviter la latence.
### V1.3
#### **Principaux ajouts :**
- L'heure du milieu ne disparait plus à certains moments lors du changement de seconde.
  - Le texte n'est désormais plus géré par la fonction canvas de tkinter, il est maintenant géré par la fonction "Label" de tkinter.
- Le programme s'arrête complètement après la fermeture de la page, ce qui n'était pas le cas avant.
  - L'attribut "daemon" de tous les threads a été passé à "True".
#### **Améliorations et divers :**
- La variable "initial_screen" a été créée pour la valeur "1920" qui est la valeur initiale qui permet le calcul de la mise à l'échelle d'écran.
- La fonction datetime pour la trigonométrie des secondes a été améliorée.
### V1.2.1
#### **Améliorations et divers :**
- La variable "canvas_size" n'était pas initialisée.
- La taille de l'heure au centre était trop grande.
- Changement de la taille des secondes et des heures qui était trop grande.
### V1.2.0
#### **Principaux ajouts :**
- L'interface graphique fonctionne même sans la carte électronique PiFace installée

### V1.1
#### **Principaux ajouts :**
- La latence entre les secondes de l'heure et les secondes s'affichant en jaune a été réduite.
- Le titre ONAIR se place automatiquement en haut en fonction de la taille de l'écran.
- Le chronomètre se place automatiquement en bas en fonction de la taille de l'écran.
- L'horloge se met au centre en fonction de la taille de l'écran.
#### **Améliorations et divers :**
- Nettoyage du code sur les fonctions de créations (chronomètre et titres).
- La fonction "chrono.pack" dans le système de réception de trame TCP a été enlevée car le chrono est déjà initialisé au début du programme.
- Suppression de la variable "msgserver" qui ne servait à rien.
- Suppression de la police de l'heure qui était en gras vers une police normale.
- La fonction de lecture des entrées de la carte à été désactivé temporairement en attendant une refonte complète.

### V1.0
- Programme initial
***

## Crédits
- Stéphane Ayreault
- Mathieu Amiaud
- Aurélien Ménard
***

