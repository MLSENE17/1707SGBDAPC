from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
def alert():
    showinfo("alerte", "Bravo!")
def dataexplorer():
    window = Tk()
    window.geometry("470x220")
    window.resizable(0,0)
    window.configure(bg="LightSeaGreen")
    window.title("DataExplorer")
    menubar = Menu(window)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Carte géographique", command=alert)
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Télécharger en format SQL/CSV", command=alert)
    menu2.add_command(label="Télécharger en format PNG", command=alert)
    menubar.add_cascade(label="Télécharger", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=alert)
    menu3.add_command(label="Quitter", command=quit)
    menubar.add_cascade(label="Aide", menu=menu3)

    window.config(menu=menubar)

