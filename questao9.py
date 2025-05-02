# entrada de dados
l1 = int(input("Insira o valor do lado 1: "))
l2 = int(input("Insira o valor do lado 2: "))
l3 = int(input("Insira o valor do lado 3: "))
# Variavel da hipotenusa e catetos
hip = 0
c1 = 0
c2 = 0
# Verificando se realmente é um triângulo
if l1 + l2 > l3 and l1 + l3 > l2 and l2 +l3 > l1:
	# Verificação de lados para saber o tipo
	if l1 == l2 and l1 == l3 and l2 == l3:
		print("O triângulo é equilátero!")
	elif l1 == l2 or l1 == l3 or l2 == l3:
		print("O triângulo isósceles!")
	else:
		print("O triângulo é escaleno!")

	# Encontrando a hipotenusa
	if l1 > l2 and l1 > l3:
		hip = l1
		c1 = l2
		c2 = l3
	elif l2 > l1 and l2 > l3:
		hip = l2
		c1 = l1
		c2 = l3
	else:
		hip = l3
		c1 = l1
		c2 = l2
	
	# Teorema de pitagoras
	hip = hip **2
	ter = (c1 ** 2) + (c2 ** 2)
	
	# Achando o ângulo
	if  hip == ter:
		print("O triângulo é Retângulo")
	elif hip < ter:
		print("O triângulo é Acutângulo")
	else:
		print("O triângulo é Obtusângulo")


else:
	print("Estes valores não formam um triângulo")