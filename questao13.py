# Entrada de dados
n = int(input("Digite um número: "))
# Variaveis para testar o primo
p = 1

# Testando primo
for i in range(2, n + 1):
	p = 1

	# Testando se é divisivel por outros números
	for j in range(2, i):
		if i % j == 0:
			p = 0
	
	# Condicional para imprimir o primo
	if p == 1:
		print(i)