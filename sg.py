from tkinter import *
from inscription import *
from authentification import *
from module1 import *

class FirstPage:
    def __init__(self):
        self.window = Tk()
        self.window.title("Covid-19 Progession Modeler")
        self.window.geometry("1080x720")
        self.window.minsize(720,480)
        #self.window.iconbitmap("logo.ico")
        self.window.config(background='#41B77F')
        # initialization des composants
        self.frame0 = Frame(self.window, bg='#41B77F')
        self.frame1 = Frame(self.window, bg='#41B77F')
        self.frame11 = Frame(self.frame1, bg='#41B77F')
        self.frame12 = Frame(self.frame1, bg='#41B77F')
        self.frame2 = Frame(self.window, bg='#41B77F')
        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame0.pack(side=TOP,fill=X)
        self.frame1.pack(pady=150)
        self.frame11.pack()
        self.frame12.pack()
        self.frame2.pack(side=BOTTOM,fill=X)

    def create_widgets(self):
        self.create_inscription_button()
        self.create_title()
        self.create_dAcq_button()
        self.create_dloa_button()
        self.create_dexp_button()
        self.create_EA_button()
        self.help_button()
        self.exit_button()


    def create_title(self):
        label_title = Label(self.frame11, text="Bienvenue sur l'application Covid-19 Progession Modeler", font=("Courrier", 20), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_inscription_button(self):
        ins = Button(self.frame0, text="Inscription", font=("Courrier", 12), bg='white', fg='#41B77F'
                           ,command=register)
        ins.pack(side=RIGHT,padx=5,pady=5)
    
    def create_dAcq_button(self):
        dAcq = Button(self.frame12, text="DataAcquisition", font=("Courrier", 12), bg='white', fg='#41B77F',command=authentifier)
        dAcq.pack(pady=20)
        
    def create_dloa_button(self):
        dloa = Button(self.frame12, text="DataLoader", font=("Courrier", 12), bg='white', fg='#41B77F')
        dloa.pack(pady=20)
        
    def create_dexp_button(self):
        dexp = Button(self.frame12, text="DataExplorer", font=("Courrier", 12), bg='white', fg='#41B77F')
        dexp.pack(pady=5)
    
    def create_EA_button(self):
        EA = Button(self.frame12, text="EvolutionAnalyser", font=("Courrier", 12), bg='white', fg='#41B77F')
        EA.pack(pady=20)
    
    def exit_button(self):
        ex = Button(self.frame2, text="Quitter", font=("Courrier", 12), bg='white', fg='#41B77F')
        ex.pack(side=RIGHT,padx=5,pady=20)    
        
    def help_button(self):
        h = Button(self.frame2, text="Aide", font=("Courrier", 12), bg='white', fg='#41B77F')
        h.pack(side=LEFT,padx=5,pady=5)  


# afficher
if __name__ =="__main__":
    app = FirstPage()
    app.window.mainloop()