from tkinter import *
from PIL import Image,ImageTk,ImageGrab
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
class flottante:
#fenetre qui est crèè quand on fait une clique sur une règion
    def __init__(self,master):
        self.window = Toplevel(master)
        # fenetre blocante : empeche l’ouverture de fenetres identiques
        master.wait_visibility(self.window)
        self.window.grab_set()
        self.window.title('Graphe d\' èvolution de Dakar')
        self.window.configure(bg="#41B77F")

        
        self.lab1 =LabelFrame(self.window, text='Courbe d\' èvolution des cas ', bg='#41B77F',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.lab2 =LabelFrame(self.window, text='Carte des dèpartements', bg='#41B77F',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.frame0 = Frame(self.window, bg='#41B77F')

        #Création des composants
        self.create_widgets()
        
        #empaquetage
        self.lab1.grid(row=0,column=0,pady=10,padx=20)
        #self.lab2.grid(row=0,column=1,pady=10,padx=20)
        self.frame0.grid(row=1,columnspan=2,pady=10,padx=20)
    
    def create_widgets(self):
        self.create_canvas1()
        self.create_canvas2()
        self.create_telcarte_button()
        self.create_teldonnee_button()
        
    def create_canvas1(self):

        fig = Figure(figsize=(6,4),dpi=100)
        ax = fig.add_subplot(111)
        
        ax.plot(range(10),[2,4,3,6,7,9,0,5,4,1])
        graph=FigureCanvasTkAgg(fig,self.window)
        self.canvas1=graph.get_tk_widget()
        self.canvas1.grid(row=0,column=1,pady=10,padx=20)

    def create_canvas2(self):
        self.canvas2=Canvas(self.lab1)
        self.image = Image.open("./Dakar.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas2.create_image(0,0,anchor=NW,image=self.photo)
        self.canvas2.pack()
    def create_telcarte_button(self):
        telca = Button(self.frame0, text="Télécharger carte", font=("Courrier", 10), bg='white', fg='#41B77F')
        telca.pack(side=LEFT,padx=200)
        
    def create_teldonnee_button(self):
        teldon = Button(self.frame0, text="Télécharger Données", font=("Courrier", 10), bg='white', fg='#41B77F')
        teldon.pack(side=RIGHT,padx=200)


