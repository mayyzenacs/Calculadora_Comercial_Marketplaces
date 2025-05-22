
## IMPORTANDO BIBLIOTECAS IMPORTANTES
import tkinter as tk
from mode import Calculator
from encoded_image import encoded_logo
from PIL import ImageTk, Image

## INICIALIZAÇÃO 
class Apliccation(): 

    def __init__(self):
        self.root = root
        self.calc = Calculator()
        self.screen()
        self.frame()
        self.buttons()
        self.delButton()
        self.checkbutton()
        self.label()
        self.entry()
        self.take()
        self.copyButton()
        self.copyText()
        self.offerLabel()
        self.logo()
        self.radiosFull()
        self.fullCalc()
    

    ## DEFININDO FUNDO PRINCIPAL
    def screen(self):
        self.root.title("Calculadora de Preço Comercial Auto by Mayra Pereira")
        self.root.configure(background= "#363636")
        self.root.geometry("480x450")
        self.root.resizable(False, False)


    ## DEFININDO O LOGO NO TOPO
    def logo(self):
        self.bgImage = Image.open('source/img/logo.png')
        self.bgImageLabel = tk.Label(self.root, image=self.bgImage, bd=0, bg="#000000")
        self.bgImageLabel.place(relheight=0.20, relwidth=1, anchor=tk.CENTER, relx=0.5, rely=0.1)


    ## FRAME PRINCIPAL
    def frame(self):
        self.frameBack = tk.Frame(self.root, relief="solid", bg="#4F4F4F")
        self.frameBack.place(relx=0.5, rely=0.59, relheight= 0.78,relwidth=0.95, anchor=tk.CENTER)

        self.str = tk.Label(
                        self.frameBack, 
                        text="Calculadora automática de preços comerciais para Marketplaces", 
                        bg="#4F4F4F", 
                        font=("verdana", 9, "bold")
                        )
        self.str.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.035, anchor=tk.CENTER)
       

    ## DEFININDO RADIO BUTTONS DE OPÇÃO
    def checkbutton(self): 
        self.choice = tk.Label(self.frameBack, text="Selecione qual porcentagem utilizar", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.choice.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.10, anchor=tk.CENTER)

        self.var = tk.IntVar()
        self.check = tk.Radiobutton(
                        self.frameBack, 
                        text="10%", 
                        variable=self.var, 
                        value=0, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold"),
                        )
        self.check2 = tk.Radiobutton(
                        self.frameBack, 
                        text="20%", 
                        variable=self.var, 
                        value=1, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check3 = tk.Radiobutton(
                        self.frameBack, 
                        text="35%", 
                        variable=self.var, 
                        value=2, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold")
                        )
        self.check.place(relheight= 0.12, relwidth=0.22, relx=0.2, rely=0.19, anchor=tk.CENTER)
        self.check2.place(relheight= 0.12, relwidth=0.22, relx=0.5, rely=0.19, anchor=tk.CENTER)
        self.check3.place(relheight= 0.12, relwidth=0.22, relx=0.7, rely=0.19, anchor='w')


    ## DEFININDO A ENTRADA QUE RECEBE O VALOR
    def entry(self):
        ## ENTRADA DO VALOR INICIAL
        self.entryCalc = tk.Entry(
                        self.frameBack, 
                        bd=0, 
                        font=("verdana", 15, "bold")
                        )
        self.entryCalc.icursor(0)
        self.entryCalc.place(relheight= 0.1 ,relwidth=0.22, relx=0.5, rely=0.38, anchor=tk.CENTER)
        
        self.entryCalc.bind("<Return>", lambda event: self.take())

        self.entryText = tk.Label(self.frameBack, text="Preço", bg="#4F4F4F", font=("Verdana", 15, "bold"))
        self.entryText.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.28, anchor=tk.CENTER)

    # COLETA OS VALORES INSERIDOS
    def take(self):
        option = self.var.get()
        valor = self.entryCalc.get().replace(",",".")   
        self.returnResult = self.calc.calc(option, valor)

        self.offerLabel()

        ## POSICIONA O VALOR FINAL NO FRAME
        self.result = tk.StringVar()
        self.result.set(self.returnResult)
        self.labelReturn = tk.Label(self.frameBack, textvariable = self.result, font=("verdana", 18, "bold"))
        self.labelReturn.place(relx=0.25, rely=0.55, relheight=0.15, relwidth=0.29)        
        

    ## INSERINDO BOTÃO DE CALCULO 
    def buttons(self):
        self.calcBt = tk.Button(self.frameBack, text="Calcular", bg="#DCDCDC", bd=0, command=self.take, font=("verdana", 9, "bold", 'italic'))
        self.calcBt.place(relx=0.059, rely=0.53, relheight=0.12, relwidth=0.14)


    ## LABEL QUE RETORNA O RESULTADO
    def label(self): 
        var = tk.StringVar()
        label = tk.Label(
                        self.frameBack, 
                        textvariable=var,
                        relief=tk.RAISED, 
                        bg="#4F4F4F",
                        font=("verdana", 15, "bold"),
                        bd = 0
                    )
        var.set("PREÇO DE")
        label.place(relx=0.55, rely=0.45, relheight= 0.1 ,relwidth=0.31, anchor='ne')

        ## DEFINE O TEXTO DE OFERTA
        self.offerText = tk.Label(self.frameBack, text="Oferta -3%", bg="#4F4F4F", font=("Verdana", 12, "bold"))
        self.offerText.place(relx=0.25, rely=0.74, relwidth=0.34, relheight=0.06, anchor="w")


    ## DEFININDO LABEL DE OFERTA
    def offerLabel(self):
        self.valueOffer = tk.StringVar()
        self.valueOffer.set(f"{self.calc.offer():.2f}")
        self.offerReturn = tk.Label(self.frameBack, textvariable=self.valueOffer, font=("Verdana", 12, "bold"))
        self.offerReturn.place(relx=0.25, rely=0.81, relwidth=0.29, relheight=0.07, anchor="w")

        

    

    def radiosFull(self): 
        self.fullText = tk.Label(
                        self.frameBack, 
                        text="Cálculo Full", 
                        bg="#4F4F4F", 
                        font=("verdana", 10, "bold")
                        )
        self.fullText.place(relx=0.65, rely=0.45, relwidth=0.31, relheight=0.07, anchor="w")
        
        self.fullChoice = tk.IntVar()
        self.placefullResult = tk.StringVar()
        
        self.fullOption = tk.Radiobutton(
                        self.frameBack, 
                        text="5", 
                        variable=self.fullChoice, 
                        value=5, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold"),
                        )
        self.fullOption.place(relheight=0.09, relwidth=0.1, relx=0.66, rely=0.52, anchor=tk.CENTER)

        self.fullOption2 = tk.Radiobutton(
                        self.frameBack, 
                        text="6", 
                        variable=self.fullChoice, 
                        value=6, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold"),
                        )
        self.fullOption2.place(relheight=0.09, relwidth=0.1, relx=0.82, rely=0.52, anchor=tk.CENTER)

        self.fullOption3 = tk.Radiobutton(
                        self.frameBack, 
                        text="8", 
                        variable=self.fullChoice, 
                        value=8, 
                        bd=0, 
                        highlightthickness=0, 
                        bg="#4F4F4F", 
                        activebackground="#4F4F4F", 
                        font=("verdana",14,"bold"),
                        )
        self.fullOption3.place(relheight=0.09, relwidth=0.1, relx=0.95, rely=0.52, anchor=tk.CENTER)

        self.fullTextWeek = tk.Label(
                        self.frameBack, 
                        text="Vendas 7 dias", 
                        bg="#4F4F4F", 
                        font=("verdana", 10, "bold")
                        )
        self.fullTextWeek.place(relx=0.65, rely=0.59, relwidth=0.31, relheight=0.07, anchor="w")

        self.fullTextResult = tk.Label(
                        self.frameBack, 
                        text="Qtd. a enviar", 
                        bg="#4F4F4F", 
                        font=("verdana", 10, "bold")
                        )
        self.fullTextResult.place(relx=0.65, rely=0.75, relwidth=0.31, relheight=0.07, anchor="w")

        ## LABEL DO CALCULO DO FULL
        self.entryFullWeek = tk.Entry(
                        self.frameBack, 
                        bd=0, 
                        font=("verdana", 14, "bold")
                        )
        self.entryFullWeek.place(relheight= 0.089 ,relwidth=0.15, relx=0.87, rely=0.69, anchor=tk.CENTER)



        self.calcBt = tk.Button(self.frameBack, text="Full", bg="#DCDCDC", bd=0, command=self.fullCalc)
        self.calcBt.place(relx=0.62, rely=0.72, relheight=0.09, relwidth=0.12)

    def fullCalc(self):
        
        getFullChoice = self.fullChoice.get()
        weekEntry = self.entryFullWeek.get()

        
        self.placefullResult.set(self.calc.mathFull(getFullChoice, weekEntry))

        self.fullResult = tk.Label(self.frameBack, textvariable= self.placefullResult, font=("verdana", 14, "bold"))
        
        self.fullResult.place(relheight= 0.089 ,relwidth=0.15, relx=0.87, rely=0.85, anchor=tk.CENTER)


    ## DEFININDO O BOTÃO DE COPIAR
    def copyText(self):
        self.copyBt = tk.Button(self.frameBack, text="Copiar", bg="#DCDCDC", bd=0, command= self.copyButton, font=("verdana", 11, "italic", 'bold'))
        self.copyBt.place(relx=0.059, rely=0.69, relheight=0.12, relwidth=0.14)

        self.copyMsg = tk.Label(self.frameBack, text="", bg="#4F4F4F")
        self.copyMsg.place(relx=0.27, rely=0.82, relheight=0.05, relwidth=0.25)

        self.copyBt.bind("<Button-1>", lambda arg: self.copyMsg.config(text="texto copiado"))
        self.copyBt.bind("<ButtonRelease-1>", lambda arg: self.root.after(1000, lambda: self.copyMsg.config(text="")))
        


    ## FUNÇÃO DE USO DO BOTÃO COPIAR
    def copyButton(self):
        copy = self.returnResult
        self.root.clipboard_clear()
        self.root.clipboard_append(copy)


    ## DEFININDO BOTÃO DE LIMPEZA
    def delButton(self):
        
        self.del_bt = tk.Button(
                        self.frameBack, 
                        text="Clear", 
                        bd=1, 
                        bg="#4F4F4F",
                        command= self.clear
                        )
        self.del_bt.place(relheight=0.09, relwidth=0.09,relx=0.5, rely=0.94, anchor=tk.CENTER)


    ## FUNÇÃO DO BOTÃO LIMPAR
    def clear(self):
        self.entryCalc.delete(0, tk.END)
        self.valueOffer.set('')
        self.result.set('')
        self.placefullResult.set('')
        self.entryFullWeek.delete(0, tk.END)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Apliccation()
    root.mainloop()

    
