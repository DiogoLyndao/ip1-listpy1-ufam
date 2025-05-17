# Este for verifica todos os valores de 3 digítos
for i in range(100, 999):
	# A variável n transforma o valor inteiro de i em uma string
	n = str(i)
	
    # Cada variável irá receber uma parte da string (Representando cada casa decimal)
	num1 = int(n[0])
	num2 = int(n[1])
	num3 = int(n[2])
	# A condição verificará se o número se adéqua a propriedade de Amstrong
	if(num1**3 + num2 **3 + num3**3 == i):
		print(i, end=", ")
