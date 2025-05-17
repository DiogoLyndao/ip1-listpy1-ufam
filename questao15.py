# Declaração de varaveis
h = 0
n = 1
# Calculando h
for i in range(1,51):
	print(n, "/",i)
	h = h + (n / i)
	n = n + 2
print("O resultado é: ", h)
	