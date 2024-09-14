from tkinter import *

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
        self.root.title("Calculadora 25.001 Auto by Mayra Pereira")
        self.root.configure(background= "#363636")
        self.root.geometry("480x450")
        self.root.resizable(False, False)

    ## FRAME PRINCIPAL
    def frame(self):
        self.frame1 = Frame(self.root, relief="solid", bg="#4F4F4F")
        self.frame1.place(relx=0.025, rely=0.010, relheight= 0.98,relwidth=0.95)
    
    ##BOTÃO DE CALCULO 
    def buttons(self):
        self.action_bt = Button(self.frame1, text="Calcular")
        self.action_bt.place(relx=0.2, rely=0.67, relheight=0.15, relwidth=0.15)
        
    ## DEFININDO BOTÃO DE LIMPEZA
    def del_button(self):
        self.del_bt = Button(
                        self.frame1, 
                        text="Clear", 
                        bd=1, 
                        bg="#4F4F4F"
                        )
        self.del_bt.place(relx=0.87, rely=0.82, relheight=0.09, relwidth=0.09)
       
    ## DEFININDO DEMAIS BOTÕES
    def checkbutton(self): 
        var = IntVar()
        self.check = Radiobutton(
                        self.frame1, 
                        text="20%", 
                        variable=var, 
                        value=0, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font="bold",
                        )
        self.check2 = Radiobutton(
                        self.frame1, 
                        text="10%", 
                        variable=var, 
                        value=1, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font="bold"
                        )
        self.check.place(relx=0.20, rely=0.35, relheight= 0.12 ,relwidth=0.12)
        self.check2.place(relx=0.35, rely=0.35, relheight= 0.12 ,relwidth=0.12)
        
    ## ENTRADA QUE RECEBE O VALOR
    def entry(self):
        self.entrycalc = Entry(
                        self.frame1, 
                        bd=0, 
                        font="bold"
                        )
        self.entrycalc.icursor(0)
        self.entrycalc.place(relx=0.46, rely=0.56, relheight= 0.1 ,relwidth=0.15)

    ## LABEL QUE RETORNA O RESULTADO
    def label(self): 
        var = StringVar()
        label = Label(
                        self.frame1, 
                        textvariable=var,
                        relief=RAISED, 
                        font="bold"
                    )
        var.set("PREÇO DE -> ")
        label.place(relx=0.34, rely=0.78, relheight= 0.1 ,relwidth=0.29)


Apliccation()
