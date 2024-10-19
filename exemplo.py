# exercicio 1
# email = input("Insira seu email")
# senha = input("Insira sua senha")

# emailEsperado = "admin@senai.com.br"
# senhaEsperada = "senai2040"

# if email == emailEsperado and senha == senhaEsperada:
#     print("Login realizado com sucesso")
# else:
#     print("Falha ao realizar login, credenciais erradas")

#------------------------------------------------------------------

#exercicio 2
# print("Bem-vindo ao conversor de temperatura")
# print("EScolha a conversão:")
# print("1: Calcule para Fahrenheit")
# print("2: fahrenheit para Celsius")

# escolha = input("Digite 1 ou 2:")

# if escolha == 1:
#     celsius = int(input("Digite a temperatura em Celsius"))
#     fahrenheit = (celsius * 9/5) + 32
#     resultado_fahrenheit = "{:.2f}".format(fahrenheit)
#     print(f"a temperatura em fahrenheits é: {fahrenheit}")
# else:
#     fahrenheit = int(input("Digite a temperatura em fahrenheits: "))
#     celsius = (fahrenheit - 32) * 5/9
#     resultado_celsius = "{:.2f}".format(celsius)
#     print(f"a temperatura em Celsius é: {resultado_celsius}C")

#-------------------------------------------------------------------

#exercicio3
# imc abaixo de 18.5 - "Abaixo do peso"
# imc entre 18.5 e 25 - "Peso normal"
# imc entre 25 e 30 - "Sobrepeso"
# imc acima de 30 - "Obesidade"
# IMC (imc = peso/(altura ** 2))

nome = input("Para começarmos, qual seu nome?")
peso = input("insira o seu peso")
altura = input("insira sua altura")

calculoIMC = peso/(altura ** 2)

if calculoIMC < 18.5:
    print(f"{nome} está abaixo do peso")
elif calculoIMC > 18.5 and calculoIMC < 25:
    print(f"{nome} está no peso normal")
elif calculoIMC > 25 and calculoIMC < 30:
    print(f"{nome} está com sobrepeso")
else:
    print(f"{nome} está gordo pra caralho")

#-------------------------------------------------------------------

#exercicio4
nome = input("insira o nome do funcionario")
meta = 1000
vendasFuncionarios = 3000

if vendasFuncionarios < meta:
    print("Você não alcançou a meta deste mês, se esforçe e melhore")
elif vendasFuncionarios == meta:
    metaVendida = vendasFuncionarios * 0.05
    print(f"{nome} a meta, ganha 5% em cima do seu valor, portanto recebe: {metaVendida}")
elif vendasFuncionarios > meta:
    metaVendida = vendasFuncionarios * 0.10
    print(f"parabens {nome}, você vendeu mais do que o esperado este mês, portanto recebe 10% em cima, ganhando: {metaVendida}")

# --------------------------------------------------------------------

# 3- Corrija todos os erros do código abaixo:

satisfacao_cliente = int(input("Digite a nota para Satisfação do Cliente (1 a 5): "))
trabalho_em_equipe = int(input("Digite a nota para Trabalho em Equipe (1 a 5): "))

soma_total = satisfacao_cliente + trabalho_em_equipe

if soma_total >= 8:
    print("Classificação Final: Excelente")
elif soma_total >= 6:
    print("Classificação Final: Bom")
elif soma_total >= 6:
    print("Classificação Final: Regular")
elif soma_total >= 2:
    print("Classificação Final: Insuficiente")
else:
    print("Classificação Final: Demitir funcionário!")
