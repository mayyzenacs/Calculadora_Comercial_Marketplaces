import math
import psycopg2

connection = psycopg2.connect(
    database='calculator',
    user='postgres',
    password='123',
    host='localhost',
    port='5432'
)
cursor = connection.cursor()

## DEFININDO CLASSE DE CÁLCULO
class Calculator():

    def __init__(self):
        self.float_value = 0
        self.percent = 0
        self.value = 0
        self.rest = 0
    
    ## FUNÇÃO QUE REALIZA O CALCULO PRINCIPAL
    def calc(self, option, value):

        if value is None or value == '':
            return ''
        
        try: 
            self.float_value = float(value)
            self.value = self.float_value

            if option == 0: 
                discount = 1 - 0.10

            elif option == 1:  
                discount = 1 - 0.20

            elif option == 2:
                discount = 1 - 0.35
            

            var = self.float_value / discount
            self.rest = math.ceil(var * 100) / 100
                
            return self.rest

        except ValueError:
            return "error"

        finally:
            self.checker()
            self.save_db()

    ## FUNÇÃO QUE CHECA SE O CALCULO ESTÁ CORRETO
    def checker(self):
        check_value = (self.rest - self.float_value) - self.rest
        return abs(check_value)
    
    ## FUNÇÃO QUE CALCULO O VALOR PARA OFERTA MELI
    def offer(self):
        return self.float_value - (self.float_value * 0.03) 
    

    def save_db(self):
        cursor.execute(
            "INSERT INTO prices (choice, valor, final_value) VALUES (%s, %s, %s)",
            (self.percent, self.value, self.rest)
        )
        connection.commit()
        print("operação salva com sucesso no banco de dados")
        connection.close()



    



