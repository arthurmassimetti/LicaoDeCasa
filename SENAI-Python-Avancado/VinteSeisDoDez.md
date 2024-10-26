```python
# 1 - Você possui uma lista de nomes de pessoas VIP. Peça ao usuário para inserir um nome e verifique se esse nome está presente na lista VIP. Informe ao usuário se ele é um membro VIP ou não.
lista_vip = ["Alice", "Bruno", "Carla", "Daniel", "Eva"]

meuNome = input("Digite seu nome: ")

if meuNome in lista_vip:
    print("Você é um membro VIP")
else:
    print("Você não é um membro VIP")

```
```python
# 2 - Em uma sala, foram registradas as alturas de 5 pessoas. Crie um programa que armazene essas alturas em uma lista e calcule a média das alturas. Apresente o resultado ao usuário.
alturas = [1.70, 1.65, 1.80, 1.75, 1.60]

media = sum(alturas) / len(alturas)

print(f"A média das alturas é: {media}")

```
```python
# 3 - Você possui uma lista com os valores das vendas de cada mês do ano (totalizando 12 meses). Desenvolva um programa que informe qual mês teve a maior venda e qual mês teve a menor venda. Utilize a lista de vendas para encontrar essas informações.
vendas = [1200, 1500, 800, 2000, 1700, 2200, 1600, 1900, 1300, 2500, 2100, 1400]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

menorNumero = min(vendas)
maiorNumero = max(vendas)

mesMaiorVenda = meses[vendas.index(maiorNumero)]
mesMenorVenda = meses[vendas.index(menorNumero)]

print(f"o mês com menor numero de vendas foi: {mesMenorVenda}, já o maior foi: {mesMaiorVenda}")

```
```python
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
vendas = [1200, 1500, 800, 2000, 1700, 2200, 1600, 1900, 1300, 2500, 2100, 1400]

maior_venda = max(vendas)
menor_venda = min(vendas)
valorMaior = vendas.index(maior_venda)
valorMenos = vendas.index(menor_venda)
mes_maior_venda = meses[vendas.index(maior_venda)]
mes_menor_venda = meses[vendas.index(menor_venda)]

print(f"o maior mes de vendas foi: {mes_maior_venda} com o valor de: {maior_venda}")
print(f"o menor mes de vendas foi: {mes_menor_venda} com o valor de: {menor_venda}")

```
```python
# 5 - Você tem uma lista com 10 valores de vendas. Crie um programa que determine e exiba os 3 maiores valores de vendas dessa lista, formando assim um "top 3". Apresente esses valores ao usuário de forma clara.
vendas = [1500, 3000, 2500, 1000, 4000, 2000, 3500, 4500, 500, 6000]

top3 = sorted(vendas, reverse=True)[:3]

print("Os 3 maiores valores de vendas são:")
for valor in top3:
    print(valor)
```


```
