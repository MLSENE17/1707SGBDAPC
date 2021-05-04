from tkinter import *
from flottante import *
class Detail():
    #fenetre qui est crèè quand on fait une clique sur une règion
    def __init__(self,master,date, region):
        self.window = Toplevel(master)
        # fenetre blocante : empeche l’ouverture de fenetres identiques
        self.master=master
        master.wait_visibility(self.window)
        self.window.grab_set()
        self.window.title('Rèpartition de '+region)
        self.window.configure(bg="#41B77F")
        self.date=date
        self.region=region
        self.lab1 =Label(self.window, text='Nombre de cas ', bg='#41B77F',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.lab2 =Label(self.window, text='Nombre de cas communautaires', bg='#41B77F',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.lab3 =Label(self.window, text='Nombre de cas contact ', bg='#41B77F',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.frame0 = Frame(self.window, bg='#41B77F')

         # creation des composants
        self.create_detail_button()
        # empaquetage
        self.lab1.grid(row=0,pady=10,padx=10,sticky=W)
        self.lab2.grid(row=1,padx=10,sticky=W)
        self.lab3.grid(row=2,pady=10,padx=10,sticky=W)
        self.frame0.grid(row=3)
    def create_detail_button(self):
        B1 = Button(self.frame0,text="Details", font=("Arial", 10),command=self.flottantp)
        B1.pack(side=RIGHT)


    def flottant(self,master,date,regio):
        pe=flottante(master,date,regio)
        region=nbrCasParRegion(date)
        pe.window.mainloop()
    
    def flottantp(self):
        self.flottant(self.master,self.date,self.region)

