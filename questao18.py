# Entrada de dados
n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))
# Declaranção de variaveis
g = 0       # G é o maior valor
m = 0       # se m é a variavel que vai dizer se foi encontrado o mmc
 
# Verificando o maior valor
if n1 > n2:
    g = n1

else:
    g = n2

  
# Repitindo enquanto o valor não for encontrado
while m != 1:

    # Verificando se o valor é multiplo de ambos.
    if g % n1 == 0 and g % n2 == 0:
        m = 1
        print("O mmc de", n1, "e", n2," é: ", g)
        
    g += 1