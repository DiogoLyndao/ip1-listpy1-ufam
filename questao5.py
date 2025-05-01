# entrada de dado do valor em reais
reais = float(input("Digite o valor em reais: R$"))

# Calculo de taxa IOF

iof = reais * (6.38/100)

dolar = (reais * 0.18) + iof
euro = (reais * 0.16) + iof
iene = (reais * 25.21) + iof

print("O valor convertido em dólar é de: ", dolar)
print("O valor convertido em Euros é de: ", euro)
print("O valor convertido em iene japônes é de: ", iene)