#importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
#Criar Janela
#Tk é uma função do tipo tkinter
window = Tk()
#configurar nossa janela, e suas caracteristicas
window.title("Login System")
window.geometry("800x400")
window.configure(background="white")
window.resizable(width=False, height=False)
window.iconbitmap(default="images/rocketIcon.ico")
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
UserLabel.place(x=5, y=140)

UserEntry = ttk.Entry(RigthFrame, width=30)
UserEntry.place(x=90, y=140)

PassLabel = Label(RigthFrame, text="Password:" , bg="#fff", font=("Century Gothic", 10), fg="#000")
PassLabel.place(x=5, y=180)

PassEntry = ttk.Entry(RigthFrame, width=30, show="*")
PassEntry.place(x=90, y=180)

def Login():

    User = UserEntry.get()
    Password = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE ( User = ? And Password = ?)
    """, (User, Password))
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if( User in VerifyLogin and Password in VerifyLogin):
            messagebox.showinfo(title="Login ingo" , message="Acess ok . Welcome")
    except:
        messagebox.showinfo(title="Login Info", message="Bad Request. Verify if you are registred at system")
#Botoes

LoginButton = ttk.Button(RigthFrame, text="Login", width=30, command=Login)
LoginButton.place(x=60, y=270)

#defindo/chamando função

def ScreenRegisterBtn():
    #removing widgets login
    LoginButton.place(x=5000)
    ScreenRegister.place(x=5000)
    #Adcionando widget de cadastro
    NameLabel = Label(RigthFrame, text="Name:" ,  bg="#fff", font=("Century Gothic", 10), fg="#000")
    NameLabel.place(x=5,y=70)

    NameEntry = ttk.Entry(RigthFrame, width=30)
    NameEntry.place(x=90,y=70)
    
    EmailLabel = Label(RigthFrame, text="Email:", bg="#fff", font=("Century Gothic", 10), fg="#000")
    EmailLabel.place(x=5, y=100)

    EmailEntry = ttk.Entry(RigthFrame, width=30)
    EmailEntry.place(x=90, y=100)


    def RegisterData():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Password = PassEntry.get()
        
        if (Name == "" and Email == "" and User == "" and Password =="" or Name == "" and Email == ""):
            messagebox.showerror(title="Register Error", message="The Filds can´t be empty")
        else:
            #executando bd e inserindo infos
            DataBaser.cursor.execute("""
                INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
                """, (Name,Email,User,Password))

            #salvando alterações
            DataBaser.conn.commit()
            #mostrando info
            messagebox.showinfo(title="Register Info", message="Register Sucessfull")


    BtnRegister = ttk.Button(RigthFrame, text="Register", width=35, command=RegisterData)
    BtnRegister.place(x=55, y=270)

    def BackToLogin():
        #REmoving widget register
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        BtnRegister.place(x=5000)
        BtnBack.place(x=5000)
        ScreenRegister.place(x=75)
        LoginButton.place(x=60)

    BtnBack = ttk.Button(RigthFrame, text="Back", width=25 ,command=BackToLogin)
    BtnBack.place(x=85, y=310)



ScreenRegister = ttk.Button(RigthFrame, text="Register", width=25, command=ScreenRegisterBtn)
ScreenRegister.place(x=75, y=315)



#terminando rendereização de janela
window.mainloop()