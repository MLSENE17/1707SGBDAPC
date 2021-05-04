from barre import *
from Detail import *
from donnee import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk,ImageGrab  # pip install pillow
import os
class thirdpage(Frame):
    def __init__(self):
        self.window = Tk()
        #self.window.geometry("820x620")
        #self.window.resizable(0,0)
        self.window.configure(bg="#41B77F")
        self.window.title("DataExplorer")
        self.ta_variable = 90

        #Initialisation des compoosants
        #self.frame0 = Frame(self.window, bg='#41B77F')
        self.btemp =Label(self.window, text='Choisir une date', bg='#41B77F',fg="white", font=("Arial", 15))
        
        #Création des composants
        self.create_widgets()
        
        #empaquetage
        self.btemp.grid(row=0,pady=10)
        #self.frame0.pack(side=TOP,fill=X)
        
    def create_widgets(self):
        self.create_barre_temporelle()
        self.create_canvas()
        self.create_gencarte_button()
        self.create_telcarte_button()
        self.create_teldonnee_button()
        self.create_exit_button()
        
    def afficherTout(self,event=None):
        self.lab.configure(text = 'Vous avez choisi les dates du dèbut au :{0} / {1} / {2}'.\
                format(self.fra.jour, self.fra.mois, self.fra.année))
    
    def test(self,event):
            """Fonction mise a jour carte nationale"""
            date= str(self.fra.année)+'-'+str(self.fra.mois)+'-'+str(self.fra.jour)
            region=nbrCasParRegion(date)
            stat=totalCas(date) 
            self.canvas.itemconfigure(self.ldakar,text="{} cas".format(region["dakar"]))
            self.canvas.itemconfigure(self.ldiourbel,text="{} cas".format(region["diourbel"]))
            self.canvas.itemconfigure(self.lndar,text="{} cas".format(region["saint-louis"]))
            self.canvas.itemconfigure(self.llouga,text="{} cas".format(region["louga"]))
            self.canvas.itemconfigure(self.lmatam,text="{} cas".format(region["matam"]))
            self.canvas.itemconfigure(self.lkolda,text="{} cas".format(region["kolda"]))
            self.canvas.itemconfigure(self.lkaolak,text="{} cas".format(region["kaolack"]))
            self.canvas.itemconfigure(self.ltamba,text="{} cas".format(region["tambacounda"]))
            self.canvas.itemconfigure(self.lkaff,text="{} cas".format(region["kaffrine"]))
            self.canvas.itemconfigure(self.lthies,text="{} cas".format(region["thies"]))
            self.canvas.itemconfigure(self.lzig,text="{} cas".format(region["ziguinchor"]))
            self.canvas.itemconfigure(self.lsed,text="{} cas".format(region["sedhiou"]))
            self.canvas.itemconfigure(self.lkedougou,text="{} cas".format(region["kedougou"]))
            self.canvas.itemconfigure(self.lfatik,text="{} cas".format(region["fatick"]))
            self.canvas.itemconfigure(self.nat,text="A ce jour, le Sènègal compte: \n +{} tests\n +{} nouveaux cas\n +{} cas contact\n +{} cas communautaires\n +{} guèris\n +{} dècès".format(stat["totalTest"],stat["totalNouvCas"],stat["totalCasContact"],stat["totalCommunautaire"],stat["totalGueris"],stat["totalDeces"]))

    def save(self):
        x=Canvas.winfo_rootx(self.canvas)
        y=Canvas.winfo_rooty(self.canvas)
        w=Canvas.winfo_width(self.canvas)
        h=Canvas.winfo_height(self.canvas)
        ImageGrab.grab((x+60,y+105,1600,900)).save("cbas.png")


    def create_barre_temporelle(self):
        self.fra = ChoixDate(self.window,'navy')
        self.fra.grid(row=1,column=0,columnspan=2,padx=20)
        self.lab = Label(self.window, text ='Vous avez choisi les dates du dèbut au 07/03/2020')
        self.lab.grid(row=1,column=2,columnspan=2,padx=10)
        self.window.bind('<Control-1>', self.afficherTout)
        #root.mainloop()
    
    def create_canvas(self):
        
        self.image = Image.open("Regions_du_Senegal.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas=Canvas(self.window,width=1080,height=450)
        self.canvas.create_image(0,0,anchor=NW,image=self.photo)
        #--------------------------------- A ReECRIRE---------------------------------------
        self.nat=self.canvas.create_text(800,30,font=('Courrier',15),text=" A ce jour, les statistiques nationaux sont nulles")
        
        sdakar= self.canvas.create_bitmap(25,150,bitmap="questhead",foreground="red")
        self.ldakar = self.canvas.create_text(25, 170,text="0 cas")
        
        sndar= self.canvas.create_bitmap(195,50,bitmap="questhead",foreground="red")
        self.lndar = self.canvas.create_text(195,70, text="0 cas")
        
        slouga= self.canvas.create_bitmap(150,120,bitmap="questhead",foreground="red")
        self.llouga = self.canvas.create_text(150,140, text="0 cas")

        smatam= self.canvas.create_bitmap(350,120,bitmap="questhead",foreground="red")
        self.lmatam = self.canvas.create_text(350,140, text="0 cas")

        stamba= self.canvas.create_bitmap(390,290,bitmap="questhead",foreground="red")
        self.ltamba = self.canvas.create_text(390,310, text="0 cas")

        skaff= self.canvas.create_bitmap(240,230,bitmap="questhead",foreground="red")
        self.lkaff = self.canvas.create_text(240,270, text="0 cas")

        sfatik= self.canvas.create_bitmap(120,230,bitmap="questhead",foreground="red")
        self.lfatik = self.canvas.create_text(120,270, text=" cas")

        skaolak= self.canvas.create_bitmap(170,250,bitmap="questhead",foreground="red")
        self.lkaolak = self.canvas.create_text(170,270, text="0 cas")

        sdiourbel= self.canvas.create_bitmap(120,200,bitmap="questhead",foreground="red")
        self.ldiourbel = self.canvas.create_text(175,205, text="0 cas")

        sthies= self.canvas.create_bitmap(85,150,bitmap="questhead",foreground="red")
        self.lthies = self.canvas.create_text(85, 170, text="0 cas")

        skolda= self.canvas.create_bitmap(295,330,bitmap="questhead",foreground="red")
        self.lkolda = self.canvas.create_text(295,370, text="0 cas")

        szig= self.canvas.create_bitmap(120,355,bitmap="questhead",foreground="red")
        self.lzig = self.canvas.create_text(120,385, text="0 cas")

        ssed= self.canvas.create_bitmap(190,350,bitmap="questhead",foreground="red")
        self.lsed = self.canvas.create_text(190,375, text="0 cas")

        skedougou= self.canvas.create_bitmap(520,330,bitmap="questhead",foreground="red")
        self.lkedougou = self.canvas.create_text(520,390, text="0 cas")
        #--------------------------------- ---------------------------------------
      
        





        self.canvas.bind("<Button-1>",self.fra.cas)
        #self.canvas.bind("<Button-1>",test)
        self.canvas.grid(row=2,columnspan=4,pady=30,padx=100)  


    def create_gencarte_button(self):
        gc = Button(self.window, text="Carte d'évolution journaliere", font=("Courrier", 10), bg='white', fg='#41B77F')
        gc.bind("<Button-1>",self.test)
        gc.grid(row=3,column=0)
        
    def create_telcarte_button(self):
        telca = Button(self.window, text="Télécharger carte", font=("Courrier", 10), bg='white', fg='#41B77F',command=self.save)
        telca.grid(row=3,column=1)
        
    def create_teldonnee_button(self):
        teldon = Button(self.window, text="Télécharger Données", font=("Courrier", 10), bg='white', fg='#41B77F')
        teldon.grid(row=3,column=2)
        
    def create_exit_button(self):
        dex = Button(self.window, text="Quitter", font=("Courrier", 10), bg='white', fg='#41B77F',command=self.window.quit)
        dex.grid(row=3,column=3)




if __name__ =="__main__":
    app=thirdpage()
    def afficher(event=None):
        app.ta_variable+=10
    app.window.mainloop()
    #app.window.quit()

