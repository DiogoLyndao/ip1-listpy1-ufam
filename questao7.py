wage = float(input("Digite seu salário anual: R$"))
ir = 0

if wage <= 28000.00:
	print("Você está isento de pagar imposto de renda.")
elif wage <= 40000.00:
	ir = (15/100)*wage
	print(f"Você deve pagar o imposto de renda de R${ir:.2f} ")
else:
	ir = (27/100)*wage
	print(f"Você deve pagar o imposto de renda de R${ir:.2f}")