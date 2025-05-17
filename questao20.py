
soma = 1  # Essa váriavel irá receber todo o calculo (O 1 representa o primeiro valor da série)
ope = 'a' # Ope vai receber a operação
den = 3 # variavel do denominador

# for para contar as repetições
for i in range(19):
	# Verificar se é número par e ímpar 
	if i % 2 == 0:
		ope ='-'
	else:
		ope = '+'
	
    # Fazendo a alternância
	if ope == '-':
		soma = soma - (1/den)
		den += 2
	elif ope == '+':
		soma = soma + (1/den) 
		den += 2

# Imprimindo o resultado	
print("n é igual: ",4*soma)