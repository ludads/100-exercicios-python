alario = float(input("Salário atual: "))
if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5
aumento = salario * percentual / 100
novo_salario = salario + aumento
print("Percentual:", percentual, "%")
print("Aumento:", aumento)
print("Novo salário:", novo_salario)
