# enrtrada de dados
time = int(input("Digite o tempo de ligação: "))
print("\n======= Escolha o tipo de ligação ========")
print("1 - Local")
print("2 - Nacional")
print("3 - Internacional")
type = int(input("Digite o tipo da ligação: "))

adtime = 0

if type == 1:
	print("=========== Local =============")
	# Condições do tempo de ligação
	if time <= 3:
		 print("O valor a ser pago é de: R$0.50")
    else:   
		adtime = time - 3
		print("O valor a ser pago é de: R$",(adtime * 0.10)+0.50)

if type == 2:
	print("========= Nacional ===========")
	# Condições do tempo de ligação
	if time <= 3:
		print("O valor a ser pago é de: R$1.00")
	else: 
		adtime = time - 3
		print("O valor a ser pago é de: R$",(adtime * 0.25)+1.00)

if type == 3:
	print("======== Internacional =========")
	# Condições do tempo de ligação
	if time <= 3:
		print("O valor a ser pago é de: R$2.00")
	else:
		adtime = time - 3
		print("O valor a ser pago é de: R$", (adtime * 0.60)+2.00)
	