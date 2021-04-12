import ExtractAndJson.Dossier as ds
import json
import os
from  ExtractAndJson.ExtractCom  import *
import shutil
import ExtractAndJson.linkimage as lki
class ExtracInfoUtile:
    def __init__(self):
        self.TabLinkImage={}
        self.Nom_Dossier="DonneJson"
        self.donne={}
        self.LastTabLinkImage={}
    def getDonneJour(self,linkimage):
        es =ExtractCom(linkimage)
        return es.getCasDict()
    def getJsonTextFichierDuJour(self):
        if lki.fonctionMain("First"):
            self.LastTabLinkImage=ds.getCheminLastImage()
            os.chdir(os.path.abspath("."))
            if not os.path.exists(self.Nom_Dossier):
                try:
                    os.mkdir(self.Nom_Dossier)
                except:
                    print("Impossible de creer le dossier")
            os.chdir(self.Nom_Dossier)
            for keys,vals in self.LastTabLinkImage.items():
                nomfichier=keys[:7]+".json"
                if not os.path.exists(nomfichier):
                    try:
                        fichier =open(nomfichier,"x")
                        fichier.close()
                    except Exception as e:
                        print("Impossible de creer le fichier",e)
                try:
                    self.donne={}
                    try:
                        with open(nomfichier,"r") as rf:
                            self.donne.update(json.load(rf))
                        rf.close()
                    except:
                        pass
                    if keys not in self.donne:
                        os.chdir("..")
                        self.donne[keys]=self.getDonneJour(vals)
                        self.donne[keys]["datecommunique"]=keys
                        os.chdir(self.Nom_Dossier)
                        with open(nomfichier,"w") as wf:
                            json.dump(self.donne,wf)
                            print("donne bien enregistres dans le fichier",nomfichier)
                            wf.close()
                        os.chdir("..")
                    else:
                        print("cet communique a ete deja extraire")
                except:
                    os.chdir("..") 
        else:
            print("le communique a ete deja telecahrge merci")    
    def getJsonTextAllFichier(self):
        if lki.fonctionMain():
            self.TabLinkImage=ds.getCheminImage()
            self.donne={}
            os.chdir(os.path.abspath("."))
            if not os.path.exists(self.Nom_Dossier):
                try:
                    os.mkdir(self.Nom_Dossier)
                except:
                    print("Impossible de creer le dossier")
            else:
                try:
                    shutil.rmtree("DonneJson")
                    os.mkdir(self.Nom_Dossier)
                except:
                    print("Impossible de creer le dossier")
            for keys,value in self.TabLinkImage.items():
                os.chdir(self.Nom_Dossier)
                nomfichier=keys+".json"
                if not os.path.exists(nomfichier):
                    try:
                        fichier =open(nomfichier,"x")
                        fichier.close()
                    except Exception as e:
                        print("Impossible de creer le fichier",e)       
                try:
                    os.chdir("..")
                    self.donne={}
                    for link in value:
                        for tjour,valjour in link.items():
                            print(tjour)
                            self.donne[tjour]=self.getDonneJour(valjour)
                            self.donne[tjour]["datecommunique"]=tjour
                    os.chdir(self.Nom_Dossier)
                    with open(nomfichier,"w") as wf:
                        json.dump(self.donne,wf)
                        print("donne bien enregistres")
                        wf.close()
                except Exception as e:
                    print(e)
                print("mois termine")
                os.chdir("..")
    def afficherObjet(self,ObjetDict):
        print("{")
        for key,val in ObjetDict.items():
            print("\t{")
            print("\t",key," :")
            for key1,val1 in val.items():
                print("\t\t",key1," :"," ",val1)
            print("\t},")
        print("}")
    def LireFichier(self):
        os.chdir(os.path.abspath("."))
        if  os.path.exists(self.Nom_Dossier):
            print("****** Veuiller selectionner Votre fichier pour la lecture******")
            i=0
            for jsonfichier in os.listdir(self.Nom_Dossier):
                i=i+1
                print("\t",i,") ",jsonfichier)
            saisie=0
            while True:
                try:
                    saisie=int(input("Entrer le numero du fichier: "))
                    assert saisie>0 and saisie<=i 
                    liste=os.listdir(self.Nom_Dossier)[saisie-1]
                    try:
                        self.donne={}
                        os.chdir(self.Nom_Dossier)
                        with open(liste,"r") as rf:
                            self.donne.update(json.load(rf))
                        rf.close()
                        self.afficherObjet(self.donne)
                        print("\n\n\t",len(self.donne)," Objets eenregistrer dans le fichier ", liste)
                        os.chdir("..")
                        break;
                    except:
                        print("probleme d ouverture fichier")
                        break
                except AssertionError:
                    print("Veuiller entrer un numero entre 1 et ",i,"Ou bien selectionner les numeros")  
                except ValueError:
                    print("Veuiller entrer un entier svp!!")    
        else:
            print("Veuiller telecharger et extraire les donnes.le dossier est vide")