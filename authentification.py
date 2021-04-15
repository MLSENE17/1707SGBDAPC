from tkinter.ttk import *
from module1 import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
def authentifier():
    window2 = Tk()
    window2.geometry("470x220")
    window2.resizable(0,0)
    window2.configure(bg="LightSeaGreen")
    window2.title("Authentification")
    #window2 = LabelFrame(window2, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
    #window2.pack(fill="both", expand="yes", padx = 150, pady=150)       
    L1 = Label(window2, text="Username", font=("Arial Bold", 15), bg='LightSeaGreen')
    L1.place(x=50, y=20)
    T1 = Entry(window2, width = 30, bd = 5)
    T1.place(x=180, y=20)       
    L2 = Label(window2, text="Password", font=("Arial Bold", 15), bg='LightSeaGreen')
    L2.place(x=50, y=80)
    T2 = Entry(window2, width = 30, show='*', bd = 5)
    T2.place(x=180, y=80)
    def verify():
            #try:
        with open("credential.txt", "r") as f:
            info = f.readlines()
            i  = 0
            for e in info:
                u, p =e.split(",")
                if u.strip() == T1.get() and p.strip() == T2.get():
                    messagebox.showinfo("Connexion avec succés","Tapez OK por etre redirigé vers le module DataAcquisition")
                    
                        #dataexplorer()# a modifier
                    i = 1
                    window2.destroy()
                    dataAcquisition()
                    break
                if i==0:
                    messagebox.showwarning("Réfusé", "SVP,entrez des identifiants valides!!")
                    window2.destroy()
            #except:
                #messagebox.showinfo("Erreur", "SVP,entrez des identifiants valides!!")
            
         
    B1 = Button(window2, text="Conneion", font=("Arial", 15), command=verify)
    B1.place(x=320, y=115)
    window2.mainloop()
