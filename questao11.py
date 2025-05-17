# Entrada de dados
num = int(input("Digite o número: "))

print("====== Faixa de Números ======")
# Condicionais
if num % 3 == 0 and num % 5 == 0:
	print("Este número é da Faixa 1")
if num % 2 == 0 and num % 10 == 0:
	print("Este número é da Faixa 2")
if num >= 100 and num <= 1000:
	print("Este número é da Faixa 3")