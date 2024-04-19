#o preço que queremos + 25,000%

def price(valor, porcentagem=25.001):
    valor2 = valor / 100
    return porcentagem * valor2 + valor

def checador(valorx,valor):
    if valorx != valor:
        return print(valorx + 0.01)
    else:
        pass

entrada = float(input("Valor "))
resultado = price(entrada)
checador(resultado, entrada)
print(resultado)