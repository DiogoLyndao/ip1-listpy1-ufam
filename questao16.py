# Variaveis 
n1 = 1
n2 = 0
# Mostrar o primeiro número
print(n1)
# Mostrando as outras sequências 
for i in range(1, 8):
	n2 = n2 + n1 
	print(n2)
	n1 = n1 + n2
	print(n1)