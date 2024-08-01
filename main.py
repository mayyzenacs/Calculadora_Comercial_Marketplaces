#o preço que queremos + 25,000%

def price(valor, porcentagem=25.001):
    preço_por = float(valor)
    porcentagem = float(porcentagem)
    preço_de = porcentagem * preço_por / 100
    return preço_por + preço_de

def checador(valor_de, valor_entrada):
    if valor_de != valor_entrada:
        return print(f"{valor_de + 0.01:.2f}")
    else:
        pass

entrada = input("Valor ").replace(",",".")
resultado = price(entrada)
checador(resultado, entrada)
print(f"{resultado:.2f}")