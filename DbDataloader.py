from ttkwidgets import CheckboxTreeview
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import os
class DbDataloader:
    def __init__(self,modeTransaction,master,getDaySlected):
        self.ville={}
        os.chdir("DonneCommune")
        with open("AllCommunes.json","r") as rf:
            self.ville.update(json.load(rf))
        rf.close()
        os.chdir("..")
        self.Alldayselected = getDaySlected
        #Variable pour les donnees 
        self.donneJsonselected={}
        self.donne={}
        self.modeTransaction=modeTransaction
        print(self.getAllDonneSelected())
    def getAllDonneSelected(self):
        os.chdir("DonneJson")
        for keys,vals in self.Alldayselected.items():
            nomfichier=keys+".json"
            self.donne={}
            try:
                with open(nomfichier,"r") as rf:
                    self.donne.update(json.load(rf))
                rf.close()
            except:
                    pass
            for day in vals:
                self.donneJsonselected[day]=self.donne[day]
                if self.donneJsonselected[day]["localite"]:
                    self.localite={}
                    #self.donneJsonselected[day]["localite"]=self.gerCasDebut(self.donneJsonselected[day]["localite"],self.donneJsonselected[day]["nbrecommunautaire"])
                    for key,val in self.donneJsonselected[day]["localite"].items():
                        if key in self.ville:
                            if self.ville[key].upper() not in self.localite:
                                self.localite[self.ville[key].upper()]=0
                            self.localite[self.ville[key].upper()]=self.localite[self.ville[key].upper()]+val
                    self.donneJsonselected[day]["localite"]=self.localite
        os.chdir("..")
        return self.donneJsonselected
