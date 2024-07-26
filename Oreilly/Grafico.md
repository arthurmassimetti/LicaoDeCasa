```python
import matplotlib.pyplot as plt

# Inicialização das listas para armazenar as informações
Unidades = []
Vendas = []

# Solicita ao usuário a quantidade de empresas a verificar
quantidadeEmpresa = int(input("Quantas empresas deseja verificar? "))

# Loop para coletar os dados de cada empresa
for i in range(quantidadeEmpresa):
    unidade = input(f"Digite o nome da unidade {i+1}: ")
    venda = float(input(f"Digite a venda da unidade {i+1}: "))
    Unidades.append(unidade)
    Vendas.append(venda)

# Configuração dos dados para o gráfico de barras
bar_labels = Unidades
bar_values = Vendas

# Criação do gráfico de barras
plt.bar(bar_labels, bar_values, color='skyblue')
plt.xlabel('Unidades')
plt.ylabel('Vendas')
plt.title('Vendas por Unidade')

# Exibição do gráfico
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo X para melhor visualização
plt.tight_layout()  # Ajusta o layout para evitar sobreposição
plt.show()
```
![image](https://github.com/user-attachments/assets/ec32d61e-9749-4c2f-9c8b-c026072b6feb)
