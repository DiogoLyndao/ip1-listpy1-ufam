# Entrada de dados
size = int(input("Digite o tamanho do arquivo em MB: "))
print("========== Plano de internet ===========")
print("1 - Plano básico (1MBps)")
print("2 - Plano Intermediário (5MBps)")
print("3 - Plano Avançado (10MBps)")
v = int(input("Digite a velocidade da conexão de acordo com o plano: "))
time = 0

# Verificando o plano
if v == 1:
	time = (size * 8) / 1
	print("O tempo será: ", time, " segundos")
	if time <= 60:
		print("Velocidade excelente")
	elif time <= 3600:
		print("Velocidade boa!")
	else:
		print("Lentidão!")
elif v >= 2:
	time = (size * 8) / 5
	print("o tempo será: ", time, " segundos")
	if time <= 60:
		print("Velocidade excelente")
	elif time <= 3600:
		print("Velocidade boa!")
	else:
		print("Lentidão!")
elif v >= 3:
	time = (size * 8) / 10
	print("o tempo será: ", time, " segundos")
	if time <= 60:
		print("Velocidade excelente")
	elif time <= 3600:
		print("Velocidade boa!")
	else:
		print("Lentidão!")