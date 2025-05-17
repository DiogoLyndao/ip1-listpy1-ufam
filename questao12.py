# Entrada de dados 
idd = int(input("Digite sua idade: "))

# Condições
if idd <= 18:
	print("Plano Júnior")
elif idd <= 40:
	print("Plano Adulto!")
elif idd <= 60:
	print("Plano Senior!")
elif idd > 60:
	print("Plano Master com coparticipação")
else: 
	print("Idade inválida")