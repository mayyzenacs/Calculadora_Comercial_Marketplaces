import math
import psycopg2

conection = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='123',
    host='localhost',
    port='5432',
    options='-c client_encoding=UTF8'
)
cursor = conection.cursor()

## DEFININDO CLASSE DE CÁLCULO
class Calculator():

    def __init__(self):
        self.final_value = 0
        self.percent = 0
        self.value = 0
        self.rest = 0
    
    ## FUNÇÃO QUE REALIZA O CALCULO PRINCIPAL
    def calc(self, option, value):

        if value is None or value == '':
            return ''
        
        try: 
            self.final_value = float(value)

            if option == 0: 
                discount = 1 - 0.10
                var = self.final_value / discount
                rest = math.ceil(var * 100) / 100
                
                return rest

            elif option == 1:  
                discount = 1 - 0.20
                var = self.final_value / discount
                rest = math.ceil(var * 100) / 100
                
                return rest

            elif option == 2:
                discount = 1 - 0.35
                var = self.final_value / discount
                rest = math.ceil(var * 100) / 100
                
                return rest

        except ValueError:
            return "error"

        finally:
            self.checker()

    ## FUNÇÃO QUE CHECA SE O CALCULO ESTÁ CORRETO
    def checker(self):
        check_value = (self.rest - self.final_value) - self.rest
        return abs(check_value)
    
    ## FUNÇÃO QUE CALCULO O VALOR PARA OFERTA MELI
    def offer(self):
        return self.final_value - (self.final_value * 0.03) 
    

    def save_db(self):
        cursor.execute(
            "INSERT INTO operations (percent, value, rest) VALUES (%s, %s, %s)",
            (self.percent, self.value, self.rest)
        )
        conection.commit()
        print("operação salva com sucesso no banco de dados")


    



