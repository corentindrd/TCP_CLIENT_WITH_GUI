import math
import socket
import threading
import time
from datetime import datetime
from timeit import default_timer
from tkinter import *

try:
    import pifacedigitalio as p
except:
    pass

# fonction chrono

def updateTime():

    global chronotitle
    global str_time

    if startchrono == 1:
        now = default_timer() - start
        minutes, seconds = divmod(now, 60)
        hours, minutes = divmod(minutes, 60)
        str_time = "%02d:%02d:%02d" % (hours, minutes, seconds)
        chronotitle['text'] = str_time
        chronotitle.place(relx=0.5, rely=0.9, anchor=CENTER)
        root.after(1000, updateTime)
    else:
        chronotitle['text'] = str_time

# fonction création secondes

def trigo():
    while True:
        second = int(datetime.now().strftime("%S"))

        if second == 0:
            C.delete("second")
        else:
            second = second - 15
            for angle in range(-15, 45):
                if angle <= second:
                    angle = ((angle * 6) * math.pi) / 180
                    x = rayon + ((rayon * 0.80) * math.cos(angle))
                    y = rayon + ((rayon * 0.80) * math.sin(angle))
                    x1 = int(x) - 5
                    y1 = int(y) - 5
                    x2 = int(x) + 5
                    y2 = int(y) + 5
                    C.create_oval(x1, y1, x2, y2, fill='#FFAA00', tags="second")
                    C.place(relx=0.5, rely=0.5, anchor=CENTER)
            hour.config(text=datetime.now().strftime("%H:%M:%S"))

# fonction serveur tcp
def onair():
    global connected
    global sock
    global title
    global start
    global startchrono

    while True:
        try:
            message = sock.recv(1024).decode("UTF-8")
            if message.find("10,1") != -1:
                title.config(text="ON AIR", font=("Avenir-Black", title_size), bg='#ff0000', fg='white')
                startchrono = 1
                start = default_timer()
                updateTime()
                try:
                    p.digital_write(0, 1)
                except:
                    pass
            elif message.find("10,0") != -1:
                title.config(text="ON AIR", font=("Avenir-Black", title_size), bg='#4D0000', fg='black')
                startchrono = 0
                updateTime()
                try:
                    p.digital_write(0, 0)
                except:
                    pass

        except socket.error:
            connected = False
            sock = socket.socket()
            print("Connexion perdue... reconnexion")
            while not connected:
                try:
                    sock.connect((ipaddress, port))
                    connected = True
                    print("Re-connexion réussie")
                except socket.error:
                    time.sleep(0.5)

# init piface

try:
    p.init()
except:
    pass

# init tkinter

root = Tk()

# récupère les informations de l'écran pour mettre à niveau

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)

#initialisation des variables écran 1920x1080

initial_screen = 1920
title_size = int(172 * screen_width / initial_screen)
chrono_size = int(142 * screen_width / initial_screen)
canvas_size = int(500 * screen_width / initial_screen)
clock_size = int(60 * screen_width / initial_screen)
width = int(515 * screen_width / initial_screen)

#initialisation des variables générales

ipaddress = '192.168.1.86'
port = 65432
rayon = width / 2
connected = True

#création de l'interface tkinter

root.title("On Air interface")
root.geometry(screen_resolution)
root.config(background='#000000000')
root.attributes("-fullscreen", True)

#création du ONAIR

title = Label(root, text="ON AIR", font=("Avenir-Black", title_size), bg='#4D0000', fg='black')
title.place(relx=0.5, rely=0.12, anchor=CENTER)

#création du canvas

C = Canvas(root, bg="black", height=canvas_size, width=canvas_size, highlightthickness=0)

#création du chrono

chronotitle = Label(root, fg='white', bg='black', font=("Avenir-Black", chrono_size))

#création des threads

th1 = threading.Thread(target=onair, daemon=True)
th2 = threading.Thread(target=trigo, daemon=True)

#initialisation du client TCP

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#fonction trigo heures

for angle in range(0, 12):
    angle = ((angle * 30) * math.pi) / 180
    x = rayon + ((rayon * 0.90) * math.cos(angle))
    y = rayon + ((rayon * 0.90) * math.sin(angle))
    x1 = int(x) - 5
    y1 = int(y) - 5
    x2 = int(x) + 5
    y2 = int(y) + 5
    C.create_oval(x1, y1, x2, y2, fill='#0003FF')
    C.place(relx=0.5, rely=0.5, anchor=CENTER)

#création de l'heure

hour = Label(root, text="",fg='#0003FF', bg='black', font=("ds-digital", clock_size))
hour.place(relx=0.5, rely=0.5, anchor=CENTER)

#démarrage des threads

th1.start()
th2.start()

#boucle tkinter

root.mainloop()
