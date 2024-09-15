def price(valor, porcentagem=25.001):
    valor_final = float(valor)
    porcentagem = float(porcentagem)
    de_por = porcentagem * valor_final / 100
    return de_por + valor_final



entrada = input("Valor ").replace(",",".")
resultado = price(entrada)
print(f"=> {resultado:.2f}")