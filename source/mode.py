def price(valor, porcentagem=25.001):
    preço_por = float(valor)
    porcentagem = float(porcentagem)
    preço_de = porcentagem * preço_por / 100
    return preço_por + preço_de

def is_float(numero):
    try:
        float(numero)
        return True
    except:
        return False