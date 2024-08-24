from mode import is_float, price
import cmd

class MyCLI(cmd.Cmd):
    prompt = ">> "
    intro = "Bem vindo ao programa de cálculo automático de preço, digite help para ver os comandos"

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

    def do_quit(self, line):
        "Saindo da interface"   
        return True
    
if __name__ == "__main__":
    MyCLI().cmdloop()
