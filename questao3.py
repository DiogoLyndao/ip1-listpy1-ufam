# importando biblioteca
import math 
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

# Calculo
a = ((num1 * 2) * (num2/2))
b = ((num1 * 3)+ num3)
c = num3 ** 3
d = math.fabs(num1 - num2)
e = ((num2 ** 2) + (math.log(num3 * num1)))

# Mostrando os resultados
print("O produto do dobro do primeiro com a metade do segundo é: ", a)
print("A soma do triplo do primeiro com o terceiro é: ", b)
print("O terceiro elevado ao cubo é: ", c)
print("O valor absoluto da subtração entre o primeiro e o segundo: ", d)
print("O quadrado do segundo somado com o logaritmo nastural do terceiro multiplicado pelo primeiro é: ", e) 