```python
numero = int(input("Digite um número: "))

print(f"Tabuada do {numero}:")
for i in range(11):
  print(f"{numero} x {i} = {numero * i}")
```

```python
dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
total_vendas = 0

for dia in dias_da_semana:
  vendas_do_dia = float(input(f"Digite o valor total das vendas de {dia}: "))
  total_vendas += vendas_do_dia

print(f"O total de vendas da semana foi de: R${total_vendas:.2f}")
```

```python
vendedores = ["Alice","Bob","Carlos","Diana","Eduardo","Fernanda","Gustavo","Heloísa","Igor","Juliana"]
vendas = [1500.50,2300.75,1800.00,2000.25,2100.60,1750.30,2500.90,1900.40,2200.10,1600.80]

for i in range(len(vendedores)):
  if vendas[i] > 1900:
    print(f"O vendedor {vendedores[i]} atingiu a meta, vendendo R${vendas[i]:.2f}")
```

```python
vendedores_vendas = [
    ["Alice", 1500.50],
    ["Bob", 2300.75],
    ["Carlos", 1800.00],
    ["Diana", 2000.25],
    ["Eduardo", 2100.60],
    ["Fernanda", 1750.30],
    ["Gustavo", 2500.90],
    ["Heloísa", 1900.40],
    ["Igor", 2200.10],
    ["Juliana", 1600.80]
]

for vendedor in vendedores_vendas:
  nome = vendedor[0]
  vendas = vendedor[1]
  if vendas > 1900:
    print(f"O vendedor {nome} atingiu a meta, vendendo R${vendas:.2f}")
```
