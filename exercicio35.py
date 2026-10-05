
idade = int(input("Idade: "))
estudante = input("É estudante? (sim/não): ")
if idade < 12 or estudante == "sim" or idade >= 60:
    valor = 30 * 0.50
else:
    valor = 30
print("Valor do ingresso: R$", valor)

