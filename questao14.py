# Entrada de dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# estrutura de repetição 
for i in range(n1, n2 + 1):
	if i % 3 == 0 and i % 5 == 0:
		print("Os números: ", i)