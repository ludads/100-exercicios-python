peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / (altura * altura)
print("IMC:", imc)
if imc < 18.5:
    print("ABAIXO DA FAIXA")
elif imc < 25:
    print("FAIXA NORMAL")
elif imc < 30:
    print("ACIMA DA FAIXA")
else:
    print("FAIXA ELEVADA")
