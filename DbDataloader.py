from ttkwidgets import CheckboxTreeview
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import os
import mysql.connector as db
class DbDataloader:
    def __init__(self,modeTransaction,master):
        self.conn=self.dbConnect()
        self.ville={}
        os.chdir("DonneCommune")
        with open("AllCommunes.json","r") as rf:
            self.ville.update(json.load(rf))
        rf.close()
        os.chdir("..")
        self.Alldayselected = {}
        #Variable pour les donnees 
        self.donneJsonselected={}
        self.donne={}
        self.modeTransaction=modeTransaction
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
        #connected to database
    def dbConnect(self):
        try:
                conn= db.connect(host= "localhost",
                                            user="admin_CovidModeler",
                                            password="dic2tr",
                                            database="covidModeler")
        except db.errors.InterfaceError as e:
                print("Error %d: %s" % (e.args[0],e.args[1]))
                sys.exit(1)
        return conn
        
        #Enregistrement par lot
    def insertParLot(self):
        for key, val in self.getAllDonneSelected().items():
            curseur= self.conn.cursor()
            request= "SELECT * FROM communique WHERE date_communique= %s"
            date=(key,)
            curseur.execute(request, date)
            result=curseur.fetchall()
            if result:
                #communique existe(Ecraser ou Ignorer)
                choix= messagebox.askyesno("Askquestion", "Cliquer Oui pour Ecrasez Non Ignorez")
                if choix == True:
                    #Ecraser données
                    pass
            else:
                #Enregistrez données dans la base
                request= """INSERT INTO communique(nbre_test, nbre_nouveaux_cas, nbre_cas_contact, nbre_cas_communautaires,
                                                    nbre_gueris, nbre_deces, nom_fichier_source, 
                                                    date_heure_extraction, date_communique)
                                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                nouveauCas=val["nbrecommunautaire"]+val["nbrecontact"]
                value=(val["nbretest"], nouveauCas, val["nbrecontact"], val["nbrecommunautaire"], val["nbregueris"], val["nbredeces"], val["nomfichiersource"], val["date_heure_extraction"], key)
                curseur.execute(request, value)
                self.conn.commit()
                self.insertCasLocalite(val["localite"], key)
            curseur.close()
    #inserer cas par localite
    def insertCasLocalite(self, localite, dateCommunique):
        curseur= self.conn.cursor()
        for key, val in localite.items():
            request= "SELECT commune_id, depart_id FROM commune WHERE nom_localite like %s"
            nom_localite=(key, )
            curseur.execute(request, nom_localite)
            result=curseur.fetchone()
            if result:
                commune_id= result[0]
                depart_id= result[1]
                request= """INSERT INTO cas_localite(commune_id, depart_id, nbre_cas, date_communique)
                                                    VALUES(%s, %s, %s, %s)"""
                value=(commune_id, depart_id, val, dateCommunique)
                curseur.execute(request, value)
                self.conn.commit()
            else:
                request= "SELECT depart_id FROM departement WHERE nom_localite like %s"
                nom_localite=(key, )
                curseur.execute(request, nom_localite)
                result=curseur.fetchone()
                depart_id= result[0]
                request= """INSERT INTO cas_localite(depart_id, nbre_cas, date_communique)
                                                    VALUES(%s, %s, %s)"""
                value=(depart_id, val, dateCommunique)
                curseur.execute(request, value)
                self.conn.commit()
        curseur.close()



