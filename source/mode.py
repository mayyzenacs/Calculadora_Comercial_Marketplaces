

def calc(option, value):
    if value is None or value == '':
        return ''
            
    try: 
        valor_final = float(value)
        if option == 0: 
            percent = 15.001
            
            percent = float(percent)
            var1 = valor_final / 0.90
            checker(0.10, var1)
            return f'{var1:.2f}'
        elif option == 1:  
            percent_20 = 25.001
            percent_20 = float(percent_20)
            de_por = percent_20 * valor_final / 100
            var2 = de_por + valor_final
            
            different = round(var2 - valor_final, 2)
            if different > 0.01:
                var2 -= 0.01
            checker(0.20, var2)
            return f'{var2:.2f}'
        elif option == 2:
            percent_35= 53.848
            percent_35 = float(percent_35)
            de_por = percent_35 * valor_final / 100
            var3 = de_por + valor_final
            print(f"{var3:.2f}")
            checker(0.35, var3)
            return f'{var3:.2f}'
    except ValueError:
        return "error"

def checker(percent, var_value):
    check_value = (var_value * percent) - var_value
    return print(check_value)