# RPI PIFACE RADIO BROADCAST

Ce programme est une client TCP de réception de trame TCP venant d'un serveur.

Fonctionnement:
- Python 3
- Interface graphique pour supporter tkinter
- Carte IN OUT Piface Digital 2
***

## ⚠️ Important
Le programme fonctionne seulement si la carte PiFace est bien détectée par le raspberry (automatique dans le programme)
***
## Prérequis
- Raspberry PI 4 (2,4,8G)
- PiFace digital 2
- Carte SD
- Alimentation Raspberry
- Ecran 16:9 avec entrée HDMI
- Cable HDMI
- Raspberry Imager ([Téléchargement](https://www.raspberrypi.com/software/))
***
## INSTALLATION

- Flasher Raspbian Desktop sur la carte SD avec Raspberry Imager
- Mettre à jour le raspberry (`sudo apt-get update & sudo apt-get upgrade -y`)
- Installation des libraries requises
  - Python3
  - PiFace
***
# CHANGELOG
### V1.1
#### **Principaux ajouts:**
- La latence entre les secondes de l'heure et les secondes s'affichant en jaune à été réduit.
- Le titre ONAIR se place automatiquement en haut en fonction de la taille de l'écran.
- Le chronomètre se place automatiquement en bas en fonction de la taille de l'écran.
- L'horloge ce met au centre en fonction de la taille de l'écran.
#### **Améliorations:**
- Nettoyage du code sur les fonctions de créations (chronomètre et titres).
- La fonction "chrono.pack" dans le système de réception de trame TCP a été enlevée car le chrono est déjà initialisé au début du programme.
- Suppression de la variable "msgserver" qui ne servait à rien.
- Suppression de la police de l'heure qui était en gras vers une police normale.

### V1.0
- Programme initial

***


