
imovel = float(input("Valor do imóvel: "))
salario = float(input("Salário: "))
anos = int(input("Prazo em anos: "))
meses = anos * 12
prestacao = imovel / meses
limite = salario * 0.30
print("Prestação:", prestacao)
print("Limite:", limite)
if prestacao <= limite:
    print("APROVADO")
else:
    print("NEGADO")
