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
        self.copy_button()
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
        self.str.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.035, anchor=CENTER)
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
        self.check3 = Radiobutton(
                        self.frame1, 
                        text="35%", 
                        variable=self.var, 
                        value=2, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check.place(relheight= 0.12 ,relwidth=0.22, relx=0.2, rely=0.19, anchor=CENTER)
        self.check2.place(relheight= 0.12 ,relwidth=0.22, relx=0.5, rely=0.19, anchor=CENTER)
        self.check3.place(relheight= 0.12 ,relwidth=0.22, relx=0.7, rely=0.19, anchor='w')


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
        self.test = calc(option, valor)

        variavel = StringVar()
        variavel.set(self.test)
        print(option)
        self.label2 = Label(self.frame1, textvariable = variavel, font=("verdana", 15, "bold"))
        self.label2.place(relx=0.25, rely=0.56, relheight=0.25, relwidth=0.30)

    def copy_button(self):
        texto_copiar = self.test
        self.root.clipboard_clear()
        self.root.clipboard_append(texto_copiar)

        self.copy_bt = Button(self.frame1, text="Copiar", bg="#DCDCDC", bd=0, command= self.copy_button)
        self.copy_bt.place(relx=0.035, rely=0.75, relheight=0.15, relwidth=0.15)
        #self.copy_msg = Label(self.frame1, tex="")
        #self.copy_msg.place(relx=0.5, rely=0.5, relheight=0.100, relwidth=0.100)

        #self.copy_bt.bind("<Button-1>", lambda event: self.copy_msg.config(text=""))
        #self.copy_bt.bind("<ButtonRelease-1>", lambda event: self.copy_msg.config(text=""))


    ##BOTÃO DE CALCULO 
    def buttons(self):
        self.action_bt = Button(self.frame1, text="Calcular", bg="#DCDCDC", bd=0, command=self.take)
        self.action_bt.place(relx=0.035, rely=0.56, relheight=0.15, relwidth=0.15)

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
        label.place(relx=0.55, rely=0.45, relheight= 0.1 ,relwidth=0.29, anchor='ne')


Apliccation()



    
