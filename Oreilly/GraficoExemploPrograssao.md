```Python
import matplotlib.pyplot as plt

years = []
pib = []

quantidadeEmpresa = int(input("Quantas empresas deseja verificar? "))

for i in range(quantidadeEmpresa):
    Ano = int(input("Ano do Faturamento: "))
    Faturamento = int(input(f"Qual o faturamento do ano {Ano}? "))
    years.append(Ano)
    pib.append(Faturamento)

plt.plot(years, pib, color='green', marker='o', linestyle='solid')
plt.xlabel('Ano')
plt.ylabel('Faturamento')
plt.title('Faturamento por Ano')
plt.show()
```

![image](https://github.com/user-attachments/assets/c9c8235d-68d9-4bfc-81bb-8ffe29b3b29d)
