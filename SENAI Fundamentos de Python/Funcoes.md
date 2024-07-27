```Python
largura = 5
comprimento = 8
area_jardim = largura * comprimento
print(f"A área do jardim é {area_jardim} m²")

celsius = 25
fahrenheit = (9/5) * celsius + 32
print(f"A temperatura em Fahrenheit é {fahrenheit} °F")

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é {media}")
```

```Python
def calcular_preco_total(preco_unitario, quantidade, categoria_cliente):
    preco_total = preco_unitario * quantidade
    if categoria_cliente == "vip":
        desconto = 0.10
    elif categoria_cliente == "premium":
        desconto = 0.20
    else:
        desconto = 0.0
    valor_desconto = preco_total * desconto
    preco_final = preco_total - valor_desconto
    return preco_final

# Exemplo de uso
preco_unitario = 50
quantidade = 3
categoria_cliente = "premium"

preco_final = calcular_preco_total(preco_unitario, quantidade, categoria_cliente)
print(f"O preço final da compra é: R${preco_final:.2f}")

```
