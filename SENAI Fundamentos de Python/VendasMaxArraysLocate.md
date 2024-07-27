```Python
# Meses e vendas
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_ano = vendas_1sem + vendas_2sem

melhor_venda = max(vendas_ano)
pior_venda = min(vendas_ano)

melhor_mes_index = vendas_ano.index(melhor_venda)
pior_mes_index = vendas_ano.index(pior_venda)

melhor_mes = meses[melhor_mes_index]
pior_mes = meses[pior_mes_index]

faturamento_total = sum(vendas_ano)

percentual_melhor_mes = (melhor_venda / faturamento_total) * 100

vendas_top3 = sorted(vendas_ano, reverse=True)[:3]

print("-" *50)
print(f"Valor de vendas do melhor mês do ano: {melhor_venda}")
print("-" *50)
print(f"Valor de vendas do pior mês do ano: {pior_venda}")
print("-" *50)
print(f"O melhor mês do ano foi {melhor_mes} com {melhor_venda} vendas")
print("-" *50)
print(f"O pior mês do ano foi {pior_mes} com {pior_venda} vendas")
print("-" *50)
print(f"Faturamento total do ano: {faturamento_total}")
print("-" *50)
print(f"O melhor mês representou {percentual_melhor_mes:.2f}% do faturamento total")
print("-" *50)
print(f"Top 3 valores de vendas do ano: {vendas_top3}")
print("-" *50)
```
