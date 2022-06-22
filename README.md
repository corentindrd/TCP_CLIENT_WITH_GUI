# RPI PIFACE RADIO BROADCAST

Ce programme est un client TCP de réception de trame venant d'un serveur.  
Il est utilisé afin de récupérer une trame TCP venant d'un serveur installé dans un studio afin d'avoir un retour d'information lorsque l'animateur est à l'antenne.  
Un chronomètre est aussi disponible afin que l'animateur sache son temps de parole.  

Fonctionnement:
- Python 3
- Interface graphique pour supporter tkinter
- Carte IN OUT Piface Digital 2
***

## ⚠️ Important
Le programme fonctionne seulement si la carte PiFace est bien détectée par le raspberry (automatique dans le programme)
***
## Prérequis
- Raspberry PI 4 (2,4,8G) ([Raspberry](https://www.kubii.fr/cartes-raspberry-pi/2772-nouveau-raspberry-pi-4-modele-b-4gb-kubii-0765756931182.html))
- PiFace digital 2 ([PiFace](https://shop.mchobby.be/fr/pi-hats/221-piface-digital-2-pour-raspberry-pi-3232100002210.html))
- Carte SD ([Carte SD](https://www.amazon.fr/SanDisk-M%C3%A9moire-microSDHC-Adaptateur-homologu%C3%A9e/dp/B08GY9NYRM/ref=sr_1_7?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3GQ2WS313G7WF&keywords=carte%2Bsd%2Bmicro%2B32&qid=1655934994&sprefix=carte%2Bsd%2Bmicro%2B32%2Caps%2C73&sr=8-7&th=1))
- Alimentation Raspberry ([Alimentation](https://www.kubii.fr/alimentations/2678-alimentation-officielle-usb-type-c-raspberry-pi-3272496300002.html))
- Ecran 16:9 avec entrée HDMI
- Cable HDMI
- Raspberry Imager ([Téléchargement](https://www.raspberrypi.com/software/))
***
## INSTALLATION

- Flasher Raspbian Desktop sur la carte SD avec Raspberry Imager
- Installer la carte PiFace sur le raspberry
- Mettre à jour le raspberry (`sudo apt-get update & sudo apt-get upgrade -y`)
- Installation des libraries requises
  - Python3
  - PiFace
***
# CHANGELOG
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


