# Entradas de dados da primeira data
d1 = int(input("Insira o dia da primeira data: "))
m1 = int(input("Insira o mês da primeira data: "))
a1 = int(input("Insira o ano da primeira data: "))

# Entradas de dados da segunda data
d2 = int(input("Insira o dia da segunda data: "))
m2 = int(input("Insira o mês da segunda data: "))
a2 = int(input("Insira o ano da segunda dara: "))

# Calculo 
dif = (((a2 - a1)*365) + ((m2 - m1)* 30) +(d2 - d1))

print("===== As datas =====")
print(d1,"/", m1, "/", a1)
print(d2,"/", m2, "/", a2)
print("A diferença em dias é de: ", dif, " dias")