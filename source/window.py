from tkinter import *
from PIL import Image, ImageTk
from mode import *

root = Tk()

class Apliccation(): 
    def __init__(self):
        self.root = root
        self.screen()
        self.frame()
        self.buttons()
        self.del_button()
        self.checkbutton()
        self.label()
        self.entry()
        root.mainloop()
    
    ## DEFININDO FUNDO PRINCIPAL
    def screen(self):
        self.root.title("Calculadora de Preço Comercial Auto by Mayra Pereira")
        self.root.configure(background= "#363636")
        self.root.geometry("480x450")
        self.root.resizable(False, False)

        self.background_image = Image.open("logo.png")
        self.resized_bg = self.background_image.resize((260,200))
        self.bg_image = ImageTk.PhotoImage(self.resized_bg)
        self.bg_image_label = Label(self.root, image=self.bg_image, bd=0, bg="#000000")
        self.bg_image_label.place(relheight=0.20, relwidth=1, anchor=CENTER, relx=0.5, rely=0.1)

    ## FRAME PRINCIPAL
    def frame(self):
        self.frame1 = Frame(self.root, relief="solid", bg="#4F4F4F")
        self.frame1.place(relx=0.5, rely=0.59, relheight= 0.78,relwidth=0.95, anchor=CENTER)

        self.str = Label(self.frame1, text="Calculadora automática de preços comerciais para Marketplaces", bg="#4F4F4F", font=("verdana", 9, "bold"))
        self.str.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.027, anchor=CENTER)
        self.inst = Label(self.frame1, text="Selecione qual porcentagem utilizar", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.inst.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.10, anchor=CENTER)
        self.instentry = Label(self.frame1, text="Preço final", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.instentry.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.28, anchor=CENTER)

    
    def on_click(self, arg):
        arg.widget.config(bg="#D3D3D3")
    def on_release(self, arg):
        arg.widget.config(bg="#FFFF00")
        
    ## DEFININDO BOTÃO DE LIMPEZA
    def del_button(self):
        self.del_bt = Button(
                        self.frame1, 
                        text="Clear", 
                        bd=1, 
                        bg="#4F4F4F"
                        )
        self.del_bt.place(relheight=0.09, relwidth=0.09,relx=0.5, rely=0.94, anchor=CENTER)
       
    ## DEFININDO DEMAIS BOTÕES
    def checkbutton(self): 
        self.var = IntVar()
        self.check = Radiobutton(
                        self.frame1, 
                        text="20%", 
                        variable=self.var, 
                        value=0, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold"),
                        )
        self.check2 = Radiobutton(
                        self.frame1, 
                        text="10%", 
                        variable=self.var, 
                        value=1, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check.place(relheight= 0.12 ,relwidth=0.22, relx=0.34, rely=0.19, anchor=CENTER)
        self.check2.place(relheight= 0.12 ,relwidth=0.22, relx=0.65, rely=0.19, anchor=CENTER)


    ## ENTRADA QUE RECEBE O VALOR
    def entry(self):
        self.entrycalc = Entry(
                        self.frame1, 
                        bd=0, 
                        font=("verdana", 15, "bold")
                        )
        self.entrycalc.icursor(0)
        self.entrycalc.place(relheight= 0.1 ,relwidth=0.22, relx=0.5, rely=0.38, anchor=CENTER)
        

    # CHAMA O VALOR DO RATION BUTTON
    def take(self):
        option = self.var.get()
        valor = self.entrycalc.get().replace(",",".")
        calc(option, valor)

    ##BOTÃO DE CALCULO 
    def buttons(self):
        self.action_bt = Button(self.frame1, text="Calcular", bg="#DCDCDC", bd=0, command=self.take)
        self.action_bt.place(relx=0.1, rely=0.56, relheight=0.25, relwidth=0.25)

        #ARRUMAR POR ULTIMO !!!!!!!!!!!!!
        self.action_bt.bind("<Button-1>", self.on_click)
        self.action_bt.bind("<ButtonRelease-1>", self.on_release)

    ## LABEL QUE RETORNA O RESULTADO
    def label(self): 
        var = StringVar()
        label = Label(
                        self.frame1, 
                        textvariable=var,
                        relief=RAISED, 
                        bg="#4F4F4F",
                        font=("verdana", 15, "bold"),
                        bd = 0
                    )
        var.set("PREÇO DE")
        label.place(relx=0.54, rely=0.45, relheight= 0.1 ,relwidth=0.29, anchor="nw")


Apliccation()



    
