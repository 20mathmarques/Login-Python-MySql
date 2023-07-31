#importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#Criar Janela
#Tk é uma função do tipo tkinter
window = Tk()
#configurar nossa janela, e suas caracteristicas
window.title("Login System")
window.geometry("800x400")
window.configure(background="white")
window.resizable(width=False, height=False)
# window.attributes

#== Carregando logo
logo = PhotoImage(file="images/logo.png")

#== Widgets

#Frame da Esquerda
LeftFrame = Frame(window, width=500, height=400, bg="#5E23D9", relief="raised")
LeftFrame.pack(side=LEFT)
#Conteúdo da esquerda
TitleLogo = Label(LeftFrame, text="WelCome!!", font=("Arial ", 40), bg="#5E23D9", fg="white")
#setando lugar do titulo
TitleLogo.place(x=100, y=40)
LogoLabel = Label(LeftFrame, image=logo, bg="#5E23D9")
#setando lugar do logo
LogoLabel.place(x=100, y=120)

##Frame da Direita
RigthFrame = Frame(window, width=300, bg="#fff", height=400, relief="raised")
RigthFrame.pack(side=RIGHT)

UserLabel = Label(RigthFrame, text="Username:", font=("Century Gothic", 10),  fg="#000", bg="#fff",)
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RigthFrame, width=30)
UserEntry.place(x=90, y=100)

PassLabel = Label(RigthFrame, text="Password:" , bg="#fff", font=("Century Gothic", 10), fg="#000")
PassLabel.place(x=5, y=160)

PassEntry = ttk.Entry(RigthFrame, width=30)
PassEntry.place(x=90, y=160)

#Botoes

LoginButton = ttk.Button(RigthFrame, text="Login", width=30)
LoginButton.place(x=60, y=270)

RegisterButton = ttk.Button(RigthFrame, text="Register", width=25)
RegisterButton.place(x=75, y=315)

#terminando rendereização de janela
window.mainloop()