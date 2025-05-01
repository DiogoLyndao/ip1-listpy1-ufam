# entrada de dados 
wage = float(input("Digite seu salário bruto: R$"))
imp = float(input("Digite o valor do empréstimo: R$"))

# Calculo 
impmax = (30/100) * wage 
print(f"O valor de empréstimo máximo é de R${impmax:.2f}")
if imp > impmax:
	print("Seu impréstimo não poderá ser feito!")
else:
	print(f"Seu empréstimo pode de R${imp:.2f} ser realizado com sucesso!")