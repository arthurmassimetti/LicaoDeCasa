quantidade_pessoas = int(input("Digite a quantidade de pessoas no quarto (1-4): "))

quarto = []

for i in range(quantidade_pessoas):
    nome = input(f"Digite o nome do hóspede {i+1}: ")
    cpf = input(f"Digite o CPF do hóspede {i+1}: ")
    quarto.append([nome, f'cpf:{cpf}'])

print("Registro de hóspedes:")
for hospede in quarto:
    print(hospede)

#------------------------------------------------------------------------------------------
meta = 10000

vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

print("Vendedores que bateram a meta:")
for vendedor in vendas:
    nome = vendedor[0]
    valor_venda = vendedor[1]
    if valor_venda >= meta:
        print(f"{nome} - Valor vendido: {valor_venda}")
#-----------------------------------------------------------------------------------------
# Listas de produtos e vendas
produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633, 725316, 644622, 994303]

# Análise de crescimento
print("Produtos que tiveram crescimento nas vendas de 2020 em relação a 2019:")
for i, produto in enumerate(produtos):
    venda2019 = vendas2019[i]
    venda2020 = vendas2020[i]
    if venda2020 > venda2019:
        crescimento = (venda2020 / venda2019 - 1) * 100
        print(f"{produto}: Venda 2019 = {venda2019}, Venda 2020 = {venda2020}, Crescimento = {crescimento:.2f}%")

