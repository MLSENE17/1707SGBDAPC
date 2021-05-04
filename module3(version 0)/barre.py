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

    def Detaille(self,master,date,regio):
        master=self.master
        d=Detail(master,date,regio)
        region=nbrCasParRegion(date)
        d.lab1.configure(text='Nombre de cas : Inconnu')
        d.lab2.configure(text='Nombre de cas communautaires : '+str(region[regio]))
        d.lab1.configure(text='Nombre de cas contact : Inconnu')
        d.window.mainloop()
    def cas(self,event):
        date1= str(self.année)+'-'+str(self.mois)+'-'+str(self.jour)
        region=nbrCasParRegion(date1)
        if (event.x>=15 and event.x<35 and event.y>= 140 and event.y<=161 ):
            regio='dakar'
            self.Detaille(self.master, date1, regio)
        if (event.x>=380 and event.x<400 and event.y>= 280 and event.y<=300 ):
            regio='tambacounda'
            self.Detaille(self.master, date1, regio)
        if (event.x>=185 and event.x<205 and event.y>= 40 and event.y<=61 ):
            regio='saint-louis'
            self.Detaille(self.master, date1, regio)
        if (event.x>=140 and event.x<160 and event.y>= 110 and event.y<=130 ):
            regio='louga'
            self.Detaille(self.master, date1, regio)
        if (event.x>=340 and event.x<360 and event.y>= 110 and event.y<=140 ):
            regio='matam'
            self.Detaille(self.master, date1, regio)
        if (event.x>=230 and event.x<250 and event.y>= 220 and event.y<=240 ):
            regio='kaffrine'
            self.Detaille(self.master, date1, regio)
        if (event.x>=110 and event.x<130 and event.y>= 220 and event.y<=240 ):
            regio='fatick'
            self.Detaille(self.master, date1, regio)
        if (event.x>=110 and event.x<130 and event.y>= 190 and event.y<=210 ):
            regio='diourbel'
            self.Detaille(self.master, date1, regio)
        if (event.x>=160 and event.x<180 and event.y>= 240 and event.y<=261 ):
            regio='kaolack'
            self.Detaille(self.master, date1, regio)
        if (event.x>=75 and event.x<95 and event.y>= 140 and event.y<=160 ):
            regio='thies'
            self.Detaille(self.master, date1, regio)
        if (event.x>=110 and event.x<130 and event.y>= 345 and event.y<=355 ):
            regio='ziguinchor'
            self.Detaille(self.master, date1, regio)
        if (event.x>=180 and event.x<200 and event.y>= 340 and event.y<=360 ):
            regio='sedhiou'
            self.Detaille(self.master, date1, regio)
        if (event.x>=510 and event.x<530 and event.y>= 320 and event.y<=340 ):
            regio='kedougou'
            self.Detaille(self.master, date1, regio)
        if (event.x>=285 and event.x<305 and event.y>= 320 and event.y<=340 ):
            regio='kolda'
            self.Detaille(self.master, date1, regio)
