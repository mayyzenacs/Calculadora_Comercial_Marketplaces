
## IMPORTANDO BIBLIOTECAS IMPORTANTES
from tkinter import *
from PIL import Image, ImageTk
from mode import Calculator
import base64
import io
from encoded_image import encoded_logo

root = Tk()

## INICIALIZAÇÃO 
class Apliccation(): 

    def __init__(self):
        self.root = root
        self.calc = Calculator()
        self.screen()
        self.frame()
        self.buttons()
        self.del_button()
        self.checkbutton()
        self.label()
        self.entry()
        self.take()
        self.copy_button()
        self.copy_text()
        self.offer_label()
        self.logo()
        root.mainloop()
    

    ## DEFININDO FUNDO PRINCIPAL
    def screen(self):
        self.root.title("Calculadora de Preço Comercial Auto by Mayra Pereira")
        self.root.configure(background= "#363636")
        self.root.geometry("480x450")
        self.root.iconbitmap("icon.ico")
        self.root.resizable(False, False)


    ## DEFININDO O LOGO NO TOPO
    def logo(self):
        self.bg_image = PhotoImage(data=encoded_logo)
        self.bg_image_label = Label(self.root, image=self.bg_image, bd=0, bg="#000000")
        self.bg_image_label.place(relheight=0.20, relwidth=1, anchor=CENTER, relx=0.5, rely=0.1)


    ## FRAME PRINCIPAL
    def frame(self):
        self.frame_back = Frame(self.root, relief="solid", bg="#4F4F4F")
        self.frame_back.place(relx=0.5, rely=0.59, relheight= 0.78,relwidth=0.95, anchor=CENTER)

        self.str = Label(
                        self.frame_back, 
                        text="Calculadora automática de preços comerciais para Marketplaces", 
                        bg="#4F4F4F", 
                        font=("verdana", 9, "bold")
                        )
        self.str.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.035, anchor=CENTER)
       

    ## DEFININDO RADIO BUTTONS DE OPÇÃO
    def checkbutton(self): 
        self.choice = Label(self.frame_back, text="Selecione qual porcentagem utilizar", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.choice.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.10, anchor=CENTER)

        self.var = IntVar()
        self.check = Radiobutton(
                        self.frame_back, 
                        text="10%", 
                        variable=self.var, 
                        value=0, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold"),
                        )
        self.check2 = Radiobutton(
                        self.frame_back, 
                        text="20%", 
                        variable=self.var, 
                        value=1, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check3 = Radiobutton(
                        self.frame_back, 
                        text="35%", 
                        variable=self.var, 
                        value=2, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check.place(relheight= 0.12, relwidth=0.22, relx=0.2, rely=0.19, anchor=CENTER)
        self.check2.place(relheight= 0.12, relwidth=0.22, relx=0.5, rely=0.19, anchor=CENTER)
        self.check3.place(relheight= 0.12, relwidth=0.22, relx=0.7, rely=0.19, anchor='w')


    ## DEFININDO A ENTRADA QUE RECEBE O VALOR
    def entry(self):
        self.result_text = Label(self.frame_back, text="Preço final", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.result_text.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.28, anchor=CENTER)

        self.entrycalc = Entry(
                        self.frame_back, 
                        bd=0, 
                        font=("verdana", 15, "bold")
                        )
        self.entrycalc.icursor(0)
        self.entrycalc.place(relheight= 0.1 ,relwidth=0.22, relx=0.5, rely=0.38, anchor=CENTER)
        

    # CHAMA O VALOR DO RATION BUTTON
    def take(self):
        option = self.var.get()
        valor = self.entrycalc.get().replace(",",".")   
        self.return_result = self.calc.calc(option, valor)

        self.checker_label(self.calc.checker())
        self.offer_label()


        ## POSICIONA O VALOR FINAL NO FRAME
        result = StringVar()
        result.set(self.return_result)
        self.label_return = Label(self.frame_back, textvariable = result, font=("verdana", 15, "bold"))
        self.label_return.place(relx=0.25, rely=0.56, relheight=0.25, relwidth=0.30)        
        

    ## INSERINDO BOTÃO DE CALCULO 
    def buttons(self):
        self.action_bt = Button(self.frame_back, text="Calcular", bg="#DCDCDC", bd=0, command=self.take)
        self.action_bt.place(relx=0.069, rely=0.51, relheight=0.15, relwidth=0.15)


    ## LABEL QUE RETORNA O RESULTADO
    def label(self): 
        var = StringVar()
        label = Label(
                        self.frame_back, 
                        textvariable=var,
                        relief=RAISED, 
                        bg="#4F4F4F",
                        font=("verdana", 15, "bold"),
                        bd = 0
                    )
        var.set("PREÇO DE")
        label.place(relx=0.55, rely=0.45, relheight= 0.1 ,relwidth=0.31, anchor='ne')
        

        ## DEFINE O CHECADOR
        self.checker = Label(self.frame_back, text="Checador", bg="#4F4F4F", font=("Verdana", 12, "bold"))
        self.checker.place(relx=0.59, rely=0.49, relwidth=0.4, relheight=0.06, anchor="w")


        ## DEFINE O TEXTO DE OFERTA
        self.value_checker = Label(self.frame_back, text="-3%", bg="#4F4F4F", font=("Verdana", 12, "bold"))
        self.value_checker.place(relx=0.63, rely=0.69, relwidth=0.34, relheight=0.06, anchor="w")


    ## DEFININDO LABEL DO CHECKER DE VALOR
    def checker_label(self, checker_value):
        checker_result = ""
        checker_result = StringVar()
        checker_result.set(checker_value)
        self.check_value = Label(self.frame_back, textvariable = checker_result, font=("verdana", 15, "bold"))
        self.check_value.place(relx=0.69, rely=0.58, relwidth=0.2, relheight=0.1, anchor="w")


    ## DEFININDO LABEL DE OFERTA
    def offer_label(self):
        offer_value = StringVar()
        offer_value.set(f"{self.calc.offer():.2f}")
        self.offer_price = Label(self.frame_back, textvariable=offer_value , bg="#4F4F4F", font=("Verdana", 12, "bold"))
        self.offer_price.place(relx=0.63, rely=0.78, relwidth=0.34, relheight=0.06, anchor="w")


    ## DEFININDO O BOTÃO DE COPIAR
    def copy_text(self):
        self.copy_bt = Button(self.frame_back, text="Copiar", bg="#DCDCDC", bd=0, command= self.copy_button)
        self.copy_bt.place(relx=0.069, rely=0.69, relheight=0.15, relwidth=0.15)

        self.copy_msg = Label(self.frame_back, text="", bg="#4F4F4F")
        self.copy_msg.place(relx=0.27, rely=0.82, relheight=0.05, relwidth=0.25)

        self.copy_bt.bind("<Button-1>", lambda arg: self.copy_msg.config(text="texto copiado"))
        self.copy_bt.bind("<ButtonRelease-1>", lambda arg: self.root.after(1000, lambda: self.copy_msg.config(text="")))


    ## FUNÇÃO DE USO DO BOTÃO COPIAR
    def copy_button(self):
        copy = self.return_result
        self.root.clipboard_clear()
        self.root.clipboard_append(copy)


    ## DEFININDO BOTÃO DE LIMPEZA
    def del_button(self):
        self.del_bt = Button(
                        self.frame_back, 
                        text="Clear", 
                        bd=1, 
                        bg="#4F4F4F",
                        command= self.clear
                        )
        self.del_bt.place(relheight=0.09, relwidth=0.09,relx=0.5, rely=0.94, anchor=CENTER)


    ## FUNÇÃO DO BOTÃO LIMPAR
    def clear(self):
        self.entrycalc.delete(0, END)
        
     
Apliccation()

    
