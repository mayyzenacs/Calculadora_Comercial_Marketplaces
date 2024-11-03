
class Calculator():
    def __init__(self):
        self.valor_final = 0
        self.percent = 0
        self.value = 0
        self.var = 0
        
    def calc(self, option, value):
        if value is None or value == '':
            return ''
                
        try: 
            self.valor_final = float(value)
            if option == 0: 
                self.percent = 15.001
                
                self.percent = float(self.percent)
                self.var = self.valor_final / 0.90
                self.checker()

                return f'{self.var:.2f}'
            elif option == 1:  
                self.percent = 25.001
                self.percent = float(self.percent)
                de_por = self.percent * self.valor_final / 100
                self.var = de_por + self.valor_final
                
                different = round(self.var - self.valor_final, 2)
                if different > 0.01:
                    self.var -= 0.01

                return f'{self.var:.2f}'
            elif option == 2:
                self.percent = 53.848
                self.percent = float(self.percent)
                self.var = self.valor_final / 0.55
                self.checker()

                return f'{self.var:.2f}'
        except ValueError:
            return "error"

    def checker(self):
        check_value = (self.value * self.percent) - self.valor_final
        return check_value
    
    def offer(self):
        return self.var * 0.97


Calculator()