# Data pré-definida
# 17/05/2025

# Entrada de dados
d = int(input("Digite o dia do seu nascimento: "))
m = int(input("Digite o mês do seu nascimento: "))
a = int(input("Digite o seu ano de nascimento: "))


anos = 2025 - a
meses = anos * 12
dias = anos * 365
minutos = 1440*dias
seg = dias * 86400

print("Você tem: ", anos, " anos de idade.")
print("Você tem: ", meses, " meses de vida")
print("Você tem: ", dias, "dias de vida")
print("Você tem: ", minutos, "minutos de vida")
print("Você tem: ", seg, " segundos de vida")