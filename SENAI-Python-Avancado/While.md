```Python
vendas = []
venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')

while venda != '':
  vendas.append(venda)
  venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')


print(f'Registro Finalizado. As vendas cadastradas foram: {vendas}')
```

```Python
vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

i = 0
while i < len(vendas):
  if vendas[i] > meta:
    print(f"O vendedor {vendedores[i]} bateu a meta. Vendas: {vendas[i]}")
  i += 1
```
