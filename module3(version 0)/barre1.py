from tkinter import *
from Detail import *
from donnee import *
#from module2 import app

class ChoixDate(Frame):
    """Curseurs pour choisir date"""
    def __init__(self,master, coul ='red'):
        self.master=master
        Frame.__init__(self)
        self.jour, self.mois, self.année, self.coul = 7, 3, 2020, coul
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,label ='Jour :', from_=1., to=31, tickinterval =10,showvalue =0, command = self.setjouruency).pack(side=LEFT)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =15,label ='Mois :', from_=1, to=12, tickinterval =3,showvalue =0, command = self.setmois).pack(side=LEFT)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,label ='année :', from_=2020, to=2030, tickinterval =10,showvalue =0, command = self.setannée).pack(side=LEFT)
    def setCurve(self):
        print(1)
        self.event_generate('<Control-1>')
    def setjouruency(self, f):
        self.jour = f
        self.event_generate('<Control-1>')
    def setmois(self, p):
        self.mois = p
        self.event_generate('<Control-1>')
    def setannée(self, a):
        self.année = a
        self.event_generate('<Control-1>')

    def Detaille(self,date,regio):
        d=Detail(date,regio)
        region=nbrCasParRegion(date)
        d.lab1.configure(text='Nombre de cas : Inconnu')
        d.lab2.configure(text='Nombre de cas communautaires : '+str(region["regio"]))
        d.lab1.configure(text='Nombre de cas contact : Inconnu')
        d.window.mainloop()
    def cas(self,event):
        date= str(self.année)+'-'+str(self.mois)+'-'+str(self.jour)
        region=nbrCasParRegion(date)
        if (event.x>=15 and event.x<35 and event.y>= 140 and event.y<=161 ):
            regio='dakar'
            self.Detaille(date,regio)
        if (event.x>=380 and event.x<400 and event.y>= 280 and event.y<=300 ):
            print("tamba")
        if (event.x>=185 and event.x<205 and event.y>= 40 and event.y<=61 ):
            print("ndar")
        if (event.x>=140 and event.x<160 and event.y>= 110 and event.y<=130 ):
            print("louga")
        if (event.x>=340 and event.x<360 and event.y>= 110 and event.y<=140 ):
            print("matam")
        if (event.x>=380 and event.x<400 and event.y>= 280 and event.y<=300 ):
            print("kaffrine")
        if (event.x>=110 and event.x<130 and event.y>= 220 and event.y<=240 ):
            print("fatik")
        if (event.x>=110 and event.x<130 and event.y>= 190 and event.y<=210 ):
            print("diourbel")
        if (event.x>=160 and event.x<180 and event.y>= 240 and event.y<=261 ):
            print("kaolak")
        if (event.x>=75 and event.x<95 and event.y>= 140 and event.y<=160 ):
            print("thies")
        if (event.x>=110 and event.x<130 and event.y>= 345 and event.y<=355 ):
            print("zig")
        if (event.x>=180 and event.x<200 and event.y>= 340 and event.y<=360 ):
            print("sediou")
        if (event.x>=510 and event.x<530 and event.y>= 320 and event.y<=340 ):
            print("kedougou")
        if (event.x>=285 and event.x<305 and event.y>= 320 and event.y<=340 ):
            print("kolda")
#### Code pour tester la classe : ###
"""
if __name__ == '__main__':
    def afficherTout(event=None):
        lab.configure(text = 'Date choisie :{0} / {1} / {2}'.format(fra.jour, fra.mois, fra.année))
        i=0
        i+=1
        
        #app.ldakar.itemconfigure(text="dfgh")

    root = Tk()
    fra = ChoixDate(root,'navy')
    fra.pack(side =TOP)
    lab = Label(root, text ='Choisir une date en déplaçant les curseurs')
    lab.pack()
    root.bind('<Control-1>', afficherTout)
    root.mainloop()
"""
"""
if __name__ == '__main__':
    def afficherTout(event=None):
        lab.configure(text = 'Date choisie :{0} / {1} / {2}'.format(fra.jour, fra.mois, fra.année))
        i=0
        i+=1
        
        #app.ldakar.itemconfigure(text="dfgh")

    root = Tk()
    fra = ChoixDate(root,'navy')
    fra.pack(side =TOP)
    lab = Label(root, text ='Choisir une date en déplaçant les curseurs')
    lab.pack()
    root.bind('<Control-1>', afficherTout)
    root.mainloop()
"""