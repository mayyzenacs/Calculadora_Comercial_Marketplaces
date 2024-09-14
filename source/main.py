from mode import is_float, price

def do_calc20(self, line):
    while True: 
        entrada = input("Valor ").replace(",",".")

        if is_float(entrada):    
            resultado = price(entrada)
            print(f"=> {resultado:.2f}")
            break
        else:
            print("Digite somente números")
    print("Calculo de 20'%' realizado com sucesso")


