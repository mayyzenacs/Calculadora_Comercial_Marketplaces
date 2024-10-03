

def calc(option, value):
    try: 
        valor_final = float(value)
        if option == 1: 
            percent = 15.001
            
            percent = float(percent)
            de_por = percent * valor_final / 100
            var1 = de_por + valor_final
            print(f"{var1:.2f}")
            return f'{var1:.2f}'
        elif option == 0:  
            percent_20 = 25.001
            percent_20 = float(percent_20)
            de_por = percent_20 * valor_final / 100
            var2 = de_por + valor_final
            return f'{var2:.2f}'
        elif option == 2:
            percent_35= 53.848
            percent_35 = float(percent_35)
            de_por = percent_35 * valor_final / 100
            var3 = de_por + valor_final
            print(f"{var3:.2f}")
            return f'{var3:.2f}'
    except ValueError:
        return "error"
        

# codigo antigo abaixo

"""
#o preço que queremos + 25,000%

def price(valor, porcentagem=25.001):
    valor_final = float(valor)
    porcentagem = float(porcentagem)
    de_por = porcentagem * valor_final / 100
    return de_por + valor_final

def checador(valorx, entrada):
    if valorx != entrada:
        return print(f"=> {valorx + 0.01:.2f}")
    else:
        pass

entrada = input("Valor ").replace(",",".")
resultado = price(entrada)
checador(resultado, entrada)
print(f"=> {resultado:.2f}")
"""
        