from decimal import Decimal, ROUND_HALF_UP

## DEFININDO CLASSE DE CÁLCULO
class Calculator():

    def __init__(self):
        self.final_value = 0
        self.percent = 0
        self.value = 0
        self.var = 0

    def initial(self, descount_percent):
        self.descount = Decimal(str(descount_percent)) / Decimal('100')
    
    ## FUNÇÃO QUE REALIZA O CALCULO PRINCIPAL
    def calc(self, option, value):

        if value is None or value == '':
            return ''
        
        try: 
            self.final_value = float(value)

            if option == 0: 
                self.percent = 15.001
                percent = float(self.percent)
                self.var = percent * self.final_value / 100
                return f'{self.final_value + self.var:.2f}'

            elif option == 1:  
                self.percent = 25.001
                percent = float(self.percent)
                self.var = percent * self.final_value / 100
                return f'{self.final_value + self.var:.2f}'

            elif option == 2:
                self.initial(35)
                self.var = self.final_value / (Decimal(1) - self.descount)

                return f'{round(self.var, 2)}'

        except ValueError:
            return "error"

        finally:
            self.checker()

    ## FUNÇÃO QUE CHECA SE O CALCULO ESTÁ CORRETO
    def checker(self):
        check_value = (self.var - self.final_value) - self.var
        return abs(check_value)
    
    ## FUNÇÃO QUE CALCULO O VALOR PARA OFERTA MELI
    def offer(self):
        return self.final_value - (self.final_value * 0.03) 
    


    



