# Entrada de dados
n = int(input("Digite um valor: "))
p = 0
# Dividindo o losango
div = n // 2

# Parte de cima
if n % 2 != 0:
	# Esse é o for que vai contar em que linha tá
    for i in range(div+1):
        p = 2 * i+1
    # imprimir espaços
        for j in range(div - i):
            print(" ", end="")
    # Imprimir os *
        for a in range(p):
            print("*", end="")
        print("")

    # Parte de baixo
    for i in range(div-1, -1, -1):
        p = 2 * i+1
    # conta os espaços
        for j in range(div -i):
            print(" ", end="")
    #  conta os *
        for a in range(p):
            print("*", end="")
        print("")