

def calc(option, value):
    try: 
        valor_final = float(value)
        if option == 0: 
            percent = 15.001
            
            percent = float(percent)
            de_por = percent * valor_final / 100
            var1 = de_por + valor_final
            print(f"{var1:.2f}")
            return f'{var1:.2f}'
        elif option == 1:  
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

