# entrada de dados
anos = int(input("Digite a quantidade de anos que você bebeu: "))
lat = int(input("Digite a quantidade de latinha bebida por dia: "))
preco = float(input("Digite o preço de cada latinha: R$"))

# Calculando
latano = (lat*365) * anos
total = latano * preco

# Mostrando resultados
print(f"A quantidade de dinheiro gasta em latinhas foi de: R${total:.2f}")