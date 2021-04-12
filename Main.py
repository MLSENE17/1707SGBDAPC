from ExtractAndJson import *
from ExtractAndJson.ExtracInfoUtile import *
import os
def maintest():
    while True:
        print("***** Veuiller selectionner dans le menu suivant *****\n")
        print("\t1) Telecharger et extraire tous les fichiers")
        print("\t2) Telecharger et extraire le communique du jour")
        print("\t3) Lire les fichier Json ")
        while True:
            try:
                saisie=int(input("Entrer le numero du fichier: "))
                assert saisie>=1 and saisie<=3
                break
            except AssertionError:
                print("Veuiller entrer un numero entre 1 et 3 Ou bien selectionner les numeros")  
            except ValueError:
                print("Veuiller entrer un entier svp!!")
        "Taper 1 pour quitter ou un autre touche pour continuer"
        es=ExtracInfoUtile()
        if saisie==1:
            es.getJsonTextAllFichier()
        else:
            if saisie==2:
                es.getJsonTextFichierDuJour()
            else:
                es.LireFichier()

        limit = input("Taper 1 pour quitter ou un autre touche pour continuer :")
        if limit=="1":
            break
if __name__ == '__main__':
    os.chdir(os.path.abspath("."))
    os.chdir("ExtractAndJson")
    maintest()
    os.chdir("..")