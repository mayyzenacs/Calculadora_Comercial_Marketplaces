
## IMPORTANDO BIBLIOTECAS IMPORTANTES
import tkinter as tk
from mode import Calculator
from encoded_image import encoded_logo

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
    

    ## DEFININDO FUNDO PRINCIPAL
    def screen(self):
        self.root.title("Calculadora de Preço Comercial Auto by Mayra Pereira")
        self.root.configure(background= "#363636")
        self.root.geometry("480x450")
        self.root.resizable(False, False)


    ## DEFININDO O LOGO NO TOPO
    def logo(self):
        self.bg_image = tk.PhotoImage(data=encoded_logo)
        self.bg_image_label = tk.Label(self.root, image=self.bg_image, bd=0, bg="#000000")
        self.bg_image_label.place(relheight=0.20, relwidth=1, anchor=tk.CENTER, relx=0.5, rely=0.1)


    ## FRAME PRINCIPAL
    def frame(self):
        self.frame_back = tk.Frame(self.root, relief="solid", bg="#4F4F4F")
        self.frame_back.place(relx=0.5, rely=0.59, relheight= 0.78,relwidth=0.95, anchor=tk.CENTER)

        self.str = tk.Label(
                        self.frame_back, 
                        text="Calculadora automática de preços comerciais para Marketplaces", 
                        bg="#4F4F4F", 
                        font=("verdana", 9, "bold")
                        )
        self.str.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.035, anchor=tk.CENTER)
       

    ## DEFININDO RADIO BUTTONS DE OPÇÃO
    def checkbutton(self): 
        self.choice = tk.Label(self.frame_back, text="Selecione qual porcentagem utilizar", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.choice.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.10, anchor=tk.CENTER)

        self.var = tk.IntVar()
        self.check = tk.Radiobutton(
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
        self.check2 = tk.Radiobutton(
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
        self.check3 = tk.Radiobutton(
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
        self.check.place(relheight= 0.12, relwidth=0.22, relx=0.2, rely=0.19, anchor=tk.CENTER)
        self.check2.place(relheight= 0.12, relwidth=0.22, relx=0.5, rely=0.19, anchor=tk.CENTER)
        self.check3.place(relheight= 0.12, relwidth=0.22, relx=0.7, rely=0.19, anchor='w')


    ## DEFININDO A ENTRADA QUE RECEBE O VALOR
    def entry(self):
        self.result_text = tk.Label(self.frame_back, text="Preço final", bg="#4F4F4F", font=("Verdana", 11, "bold"))
        self.result_text.place(relheight=0.09, relwidth=1, relx=0.5, rely=0.28, anchor=tk.CENTER)

        self.entrycalc = tk.Entry(
                        self.frame_back, 
                        bd=0, 
                        font=("verdana", 15, "bold")
                        )
        self.entrycalc.icursor(0)
        self.entrycalc.place(relheight= 0.1 ,relwidth=0.22, relx=0.5, rely=0.38, anchor=tk.CENTER)
        

    # CHAMA O VALOR DO RATION BUTTON
    def take(self):
        option = self.var.get()
        valor = self.entrycalc.get().replace(",",".")   
        self.return_result = self.calc.calc(option, valor)

        self.offer_label()


        ## POSICIONA O VALOR FINAL NO FRAME
        self.result = tk.StringVar()
        self.result.set(self.return_result)
        self.label_return = tk.Label(self.frame_back, textvariable = self.result, font=("verdana", 15, "bold"))
        self.label_return.place(relx=0.25, rely=0.56, relheight=0.25, relwidth=0.30)        
        

    ## INSERINDO BOTÃO DE CALCULO 
    def buttons(self):
        self.action_bt = tk.Button(self.frame_back, text="Calcular", bg="#DCDCDC", bd=0, command=self.take)
        self.action_bt.place(relx=0.069, rely=0.51, relheight=0.15, relwidth=0.15)


    ## LABEL QUE RETORNA O RESULTADO
    def label(self): 
        var = tk.StringVar()
        label = tk.Label(
                        self.frame_back, 
                        textvariable=var,
                        relief=tk.RAISED, 
                        bg="#4F4F4F",
                        font=("verdana", 15, "bold"),
                        bd = 0
                    )
        var.set("PREÇO DE")
        label.place(relx=0.55, rely=0.45, relheight= 0.1 ,relwidth=0.31, anchor='ne')

        ## DEFINE O TEXTO DE OFERTA
        self.value_checker = tk.Label(self.frame_back, text="-3%", bg="#4F4F4F", font=("Verdana", 12, "bold"))
        self.value_checker.place(relx=0.62, rely=0.58, relwidth=0.34, relheight=0.06, anchor="w")


    ## DEFININDO LABEL DE OFERTA
    def offer_label(self):
        self.offer_value = tk.StringVar()
        self.offer_value.set(f"{self.calc.offer():.2f}")
        self.offer_price = tk.Label(self.frame_back, textvariable=self.offer_value, font=("Verdana", 12, "bold"))
        self.offer_price.place(relx=0.62, rely=0.67, relwidth=0.31, relheight=0.07, anchor="w")


    ## DEFININDO O BOTÃO DE COPIAR
    def copy_text(self):
        self.copy_bt = tk.Button(self.frame_back, text="Copiar", bg="#DCDCDC", bd=0, command= self.copy_button)
        self.copy_bt.place(relx=0.069, rely=0.69, relheight=0.15, relwidth=0.15)

        self.copy_msg = tk.Label(self.frame_back, text="", bg="#4F4F4F")
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
        self.del_bt = tk.Button(
                        self.frame_back, 
                        text="Clear", 
                        bd=1, 
                        bg="#4F4F4F",
                        command= self.clear
                        )
        self.del_bt.place(relheight=0.09, relwidth=0.09,relx=0.5, rely=0.94, anchor=tk.CENTER)


    ## FUNÇÃO DO BOTÃO LIMPAR
    def clear(self):
        self.entrycalc.delete(0, tk.END)
        self.offer_value.set("")
        self.result.set("")
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Apliccation()
    root.mainloop()

    
