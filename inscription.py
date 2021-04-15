from sg import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
def register():
    window1 = Tk()
    window1.geometry("470x220")
    window1.resizable(0,0)
    window1.configure(bg="LightSeaGreen")
    window1.title("Inscription")
    l1 = Label(window1, text="Login:", font=("Arial",15), bg="LightSeaGreen")
    l1.place(x=10, y=10)
    t1 = Entry(window1, width=30, bd=5)
    t1.place(x = 200, y=10)       
    l2 = Label(window1, text="Mot de passe:", font=("Arial",15), bg="LightSeaGreen")
    l2.place(x=10, y=60)
    t2 = Entry(window1, width=30, show="*", bd=5)
    t2.place(x = 200, y=60)
    l3 = Label(window1, text="Confirmer mot de passe:", font=("Arial",15), bg="LightSeaGreen")
    l3.place(x=10, y=110)
    t3 = Entry(window1, width=30, show="*", bd=5)
    t3.place(x = 200, y=110)
    def check():
        if t1.get()!="" and t2.get()!="" and t3.get()!="":
            if t2.get()==t3.get():
                with open("credential.txt", "a") as f:
                    f.write(t1.get()+","+t2.get()+"\n")
                    messagebox.showinfo("Bonjour","Vous avez été enregistré avec succés!!")
            else:
                messagebox.showwarning("Inscription refusée","Mot de passe ne correspond pas!!")
        else:
            messagebox.showerror("Inscription refusée", "Un ou plusieurs champ(s) manquant()!")
        window1.destroy()
                    
    b1 = Button(window1, text="S'inscrire", font=("Arial",15), bg="#ffc22a", command=check)
    b1.place(x=170, y=150)
    window1.mainloop()
