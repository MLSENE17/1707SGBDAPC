from ExtracInfoUtile import *
import Dossier as ds
import json
import os
from  ExtractCom  import *
import shutil
import linkimage as lki
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
class secondPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("DataAcquisition")
        self.window.geometry("480x240")
        self.window.resizable(0,0)
        #self.window.iconbitmap("logo.ico")
        self.window.configure(bg="LightSeaGreen")
        # initialization des composants
        self.frame0=Frame(self.window,bg='LightSeaGreen')
        self.frame1=Frame(self.window,bg='LightSeaGreen')
        self.frame2=Frame(self.window,bg='LightSeaGreen')
        # creation des composants
        self.create_widgets()
        # empaquetage
        self.frame0.pack(pady=15)
        self.frame1.pack()
        self.frame2.pack(side=BOTTOM,fill=X)
        
    def exj(self):
        self.es=ExtracInfoUtile()
        self.es.getJsonTextFichierDuJour()
        #self.bar()

        
    def exa(self):
        self.es=ExtracInfoUtile()
        self.es.getJsonTextAllFichier()

    def create_widgets(self):
        self.create_title()
        self.create_jour_button()
        self.create_jourPB_button()
        self.create_all_button()
        self.create_allPB_button()
        self.exit_button()

    
    def create_title(self):
        label1=Label(self.frame0,text="Bienvenu dans le module DataAcquisition",font=("Arial Bold", 15), bg='LightSeaGreen')
        label1.pack()

    def create_jour_button(self):
        B1 = Button(self.frame1,text="Telecharger et extraire le communique du jour", font=("Arial", 10),command=self.exj)
        B1.pack()
        
    def create_jourPB_button(self):
        bar1 = Progressbar(self.frame1,orient=HORIZONTAL,length=300)
        bar1.pack(pady=10)
        #chaine = Label(frame1, text="poids : 0 MB, vitesse = 0 KB/s")
        #chaine.pack()
        def bar(self):
            import time
            self.bar1['value'] = 20
            root.update_idletasks()
            time.sleep(1)
            
            self.bar1['value'] = 40
            root.update_idletasks()
            time.sleep(1)
            
            self.bar1['value'] = 50
            root.update_idletasks()
            time.sleep(1)
            
            self.bar1['value'] = 60
            root.update_idletasks()
            time.sleep(1)
            
            self.bar1['value'] = 80
            root.update_idletasks()
            time.sleep(1)
            self.bar1['value'] = 100

    
    def create_all_button(self):
        B2 = Button(self.frame1,text="Telecharger et extraire tous les fichiers", font=("Arial", 10),command=self.exa)
        B2.pack(pady=10)
        
    def create_allPB_button(self):
        bar2 = Progressbar(self.frame1,orient=HORIZONTAL,length=300)
        bar2.pack()
        #chaine = Label(self.frame1, text="poids : 0 MB, vitesse = 0 KB/s")
        #chaine.pack()
        
    def exit_button(self):
        B2 = Button(self.frame2, text="Quitter", font=("Arial", 10), command=self.window.quit)
        B2.pack(side=RIGHT)
        
    
    #def start(self):
     #   t=10
      #  x=0
       # while(x<10):
       #     bar1["values"]+=10
        #    x+=1

def dataAcquisition():
    app = secondPage()
    app.window.mainloop()

    