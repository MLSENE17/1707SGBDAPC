from ttkwidgets import CheckboxTreeview
import tkinter as tk
from tkinter import messagebox
import json
import os
class DataLoader(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.anne={}
        self.master=master
        self.master.minsize(900,680)
        self.master.resizable(width=False,height=True)
        self.tree = CheckboxTreeview(master,height=25)
        os.chdir("DonneJson")
        with open("donne.json","r") as rf:
            self.anne.update(json.load(rf))
        rf.close()
        os.chdir("..")
        self.Nomfichier=os.listdir("DonneJson")
        self.Nomfichier.sort(reverse=True)
        self.create_widgets()
    #Fonction pour lire les fichiers json deja dans le module DataAcquisition
    def lireFichier(self):
        label_welcome1 = tk.Label(self.master,text="Prévisualiser les données",
        borderwidth = 7,
        width = 40,
        relief="groove"
        )
        label_welcome1.grid(row = 1, column = 0, pady = 2)
        label_welcome2 = tk.Label(self.master,text="Selectionner le fichier pour la lecture")
        label_welcome2.grid(row = 2, column = 0, pady =2 )
        listbox = tk.Listbox(self.master, width=40, height=20,selectmode=tk.SINGLE)
        i=0
        for fichier in self.Nomfichier:
            if "2" in fichier:
                listbox.insert(i, fichier)
                i=i+1
        def afficherObjet(Obj):
            try:
                os.chdir("DonneJson")
                textFichier={}
                with open(Obj,"r") as rf:
                    textFichier.update(json.load(rf))
                rf.close() 
                if textFichier:
                    texte="{\n"
                    for key,val in  textFichier.items():
                        b ="\t{\n"
                        c="\t"+str(key)+" :\n"
                        d=""
                        for key1,val1 in val.items():
                            d=str(d)+"\t\t"+str(key1)+" :"+" "+str(val1)+"\n"
                        e="\t},\n"
                        texte=texte+b+c+d+e
                    texte=texte+"}\n"
                texte=texte+"\n\n\t"+str(len(textFichier))+" Objets eenregistrer dans le fichier "+Obj 
                os.chdir("..")
                return texte
            except Exception as e:
                print(e)
                messagebox.showerror(title="Erreur !!!", message="Fichier "+Obj+" introuvable")
        def selected_item():
            try:
                if  listbox.get(listbox.curselection()):
                    textes=afficherObjet(listbox.get(listbox.curselection()))
                    if textes:
                        fil = tk.Toplevel(self.master)
                        # fenetre blocante : empeche l’ouverture de fenetres identiques
                        self.master.wait_visibility(fil)
                        fil.grab_set()
                        # end fenetre blocante
                        fil.geometry("600x600")
                        fil.title("Fichier :"+listbox.get(listbox.curselection()))
                        yscroll = tk.Scrollbar(fil)
                        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
                        xscroll = tk.Scrollbar(fil, orient=tk.HORIZONTAL)
                        xscroll.pack(side=tk.BOTTOM, fill=tk.X)
                        text1 = tk.Text(fil,wrap=tk.NONE,height=30, width=100,yscrollcommand=yscroll.set,
                        xscrollcommand=xscroll.set)  
                        text1.config(state="normal")
                        text1.insert("1.0",textes)   
                        text1.pack(side=tk.LEFT) 
                        yscroll.config(command=text1.yview)   
                        xscroll.config(command=text1.xview)             
                        fil.mainloop()
                        fil.quit()
            except :
                messagebox.showerror(title="Erreur !!!", message="Vous selectionner un fichier d`abord")
        listbox.grid(row = 3, column = 0, pady =2 )
        btn = tk.Button(root, text='Lire Le Fichier', command=selected_item)
        btn.grid(row = 3, column = 1, pady =6 )
    #Fonction pour cocher les dates ensuite enregistrer vers la bases de donnee
    def CaseCocher(self):  
        def getCheckDict(obj):
            selectDate={}
            for t in obj:
                try:
                    selectDate[t[:7]].append(t)
                except:
                    selectDate[t[:7]]=[]
                    selectDate[t[:7]].append(t)
            return  selectDate
        def hello():
            if self.tree.get_checked():
                #si il choisi oui (en transanction)
                choice= messagebox.askyesnocancel("askquestion","Les données seront chargées par lot et en mode transactionnel ou pas")
                dateselected= getCheckDict(self.tree.get_checked())
                print( dateselected)
                if choice==True:
                    messagebox.showinfo("Info","Chargement des donne par lot et transaction")
                else:
                    #si il choisi no 
                    if choice==False:
                        messagebox.showinfo("Info","Chargement des donne par lot directement")
            else:
                messagebox.showerror(title="Erreur !!!", message="Cocher une case au moins !!!")
        label_welcomec = tk.Label(self.master,
        text="La liste des fichiers json obtenus avec leur arborescence",
        borderwidth = 7,
        relief="groove")
        label_welcomec.grid(row = 1, column = 3, pady = 8)
        vsb = tk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        vsb.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.insert("", "end", "ALL", text="SELECT ALL")
        for key,val in self.anne.items():
            self.tree.insert("ALL", "end", key, text=key)
            for i in val:
                self.tree.insert(key,"end", i, text=i)
        self.tree.grid(row = 3, column = 3, pady = 2)
        button_name=tk.Button(self.master,text="Enregistrer les donnees",command=hello,activeforeground = "blue",
        activebackground = "red",width=20)
        button_name.grid(row = 3, column = 4, pady = 2)
    def create_widgets(self):
        self.lireFichier()
        self.CaseCocher()
if __name__ == '__main__':
    root = tk.Tk()
    app = DataLoader(master=root)
    app.mainloop()
    root.quit()