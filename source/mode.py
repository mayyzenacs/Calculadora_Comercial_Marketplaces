
## DEFININDO CLASSE DE CÁLCULO
class Calculator():
    def __init__(self):
        self.valor_final = 0
        self.percent = 0
        self.value = 0
        self.var = 0
    
    ## FUNÇÃO QUE REALIZA O CALCULO PRINCIPAL
    def calc(self, option, value):
        if value is None or value == '':
            return ''
                
        try: 
            self.valor_final = float(value)

            if option == 0: 
                self.percent = 10
                
                self.var = self.valor_final / 0.9

                return f'{self.var:.2f}'

            elif option == 1:  
                self.percent = 20
                
                self.var = self.valor_final / 0.8
                

                return f'{self.var:.2f}'

            elif option == 2:
                self.percent = 35
                self.percent = float(self.percent)
                self.var = self.valor_final / 0.65

                return f'{self.var:.2f}'

        except ValueError:
            return "error"

        finally:
            self.checker()

    def checker(self):
        check_value = self.var * (1 - self.percent / 100)
        return check_value
    
    def offer(self):
        return self.valor_final - (self.valor_final * 0.03) 
    


    



