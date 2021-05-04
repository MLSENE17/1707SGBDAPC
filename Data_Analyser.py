from tkinter import *
import tkinter as tkinter
#def connexion(): 
def Data_Analyser():
    Data_Analyser_fenetre=tkinter.Toplevel(window)
    Data_Analyser_fenetre.geometry("470x220")
    Data_Analyser_fenetre.title("Data_Analyzer")
    Data_Analyser_fenetre.config(bg='#41B77F')
    Tf=tkinter.Label(Data_Analyser_fenetre, text="DataAnalyzer")
    Tf.pack(pady=30)
    Frame1 = Frame(Data_Analyser_fenetre, borderwidth=2, relief=GROOVE)
    Frame1.pack(side=LEFT, padx=30, pady=30)
    Frame2 = Frame(Data_Analyser_fenetre, borderwidth=2, relief=GROOVE)
    Frame2.pack(side=LEFT, padx=10, pady=10, )
    Button(Frame1, text="Cumul mensuel par dep", command=choisir_Annee).pack(padx=40, pady=10)
    Button(Frame2, text="Télechargements").pack(padx=40, pady=10)

    

    Data_Analyser_fenetre.mainloop()

def choisir_Annee():
    choisir_Annee_fenetre=tkinter.Toplevel(window)
    choisir_Annee_fenetre.geometry("470x220")
    choisir_Annee_fenetre.title("cumul")
    choisir_Annee_fenetre.config(bg='#41B77F')
    Tf=tkinter.Label(choisir_Annee_fenetre, text="cumul_mensuel")
    Tf.pack(pady=20)
    Frame3 = Frame(choisir_Annee_fenetre, borderwidth=2, relief=GROOVE)
    Frame3.pack(side=LEFT, padx=30, pady=30)
    Frame4 = Frame(choisir_Annee_fenetre, borderwidth=2, relief=GROOVE)
    Frame4.pack(side=LEFT, padx=10, pady=10)
    def mois():
        print(8)
    def mois1():
        print(8)
    B1=Button(choisir_Annee_fenetre, text="2020", command=mois)
    B1.pack(padx=40, pady=10)
    B2=Button(choisir_Annee_fenetre, text="2021", command=mois1)
    B2.pack(padx=40, pady=10)
    

window=Tk()
window.geometry("470x220")
window.configure(bg="LightSeaGreen")
window.title("Se connecter")
L1 = Label(window, text="Username", font=("Arial Bold", 15), bg='LightSeaGreen')
L1.place(x=50, y=20)
T1 = Entry(window, width = 30, bd = 5)
T1.place(x=180, y=20)       
L2 = Label(window, text="Password", font=("Arial Bold", 15), bg='LightSeaGreen')
L2.place(x=50, y=80)
T2 = Entry(window, width = 30, show='*', bd = 5)
T2.place(x=180, y=80)

    #Bouton de connexion
connexion=Button(window, text="Connexion", font=("Arial", 15), command=Data_Analyser)
connexion.place(x=220, y=115)

#controle a faire avec la BD

window.mainloop()        
