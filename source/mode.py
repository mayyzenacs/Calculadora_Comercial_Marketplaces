
class Calculator():
    def __init__(self):
        self.valor_final = 0
        self.percent = 0
        self.value = 0
        
    def calc(self, option, value):
        if value is None or value == '':
            return ''
                
        try: 
            self.valor_final = float(value)
            if option == 0: 
                self.percent = 15.001
                
                self.percent = float(self.percent)
                var1 = self.valor_final / 0.90
                self.checker()
                self.offer(var1)

                return f'{var1:.2f}'
            elif option == 1:  
                self.percent = 25.001
                self.percent = float(self.percent)
                de_por = self.percent * self.valor_final / 100
                var2 = de_por + self.valor_final
                
                different = round(var2 - self.valor_final, 2)
                if different > 0.01:
                    var2 -= 0.01

                self.offer(var2)
                return f'{var2:.2f}'
            elif option == 2:
                self.percent = 53.848
                self.percent = float(self.percent)
                #de_por = self.percent * self.valor_final / 100
                #var3 = de_por + self.valor_final
                var3 = self.valor_final / 0.55
                print(f"{var3:.2f}")
                self.checker()
                self.offer(var3)

                return f'{var3:.2f}'
        except ValueError:
            return "error"

    def checker(self):
        check_value = (self.value * self.percent) - self.valor_final
        return check_value
    
    def offer(self, price):
        return (price * 0.3) - price


Calculator()