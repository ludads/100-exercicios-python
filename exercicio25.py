
preco = float(input("Preço: "))
opcao = int(input("Opção: "))
if opcao == 1:
    valor = preco * 0.90
elif opcao == 2:
    valor = preco * 0.95
elif opcao == 3:
    valor = preco
elif opcao == 4:
    valor = preco * 1.08
else:
    print("OPÇÃO INVÁLIDA")
    valor = None
if valor is not None:
    print("Valor final:", valor)
