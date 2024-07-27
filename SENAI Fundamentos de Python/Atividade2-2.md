```Python
# Definição dos estoques mínimos por categoria
estoque_minimo = {
    "alimentos": 50,
    "bebidas": 75,
    "limpeza": 30
}

# Função para verificar estoque e emitir alerta se necessário
def verifica_estoque(nome, categoria, quantidade):
    if categoria in estoque_minimo:
        if quantidade < estoque_minimo[categoria]:
            print(f"Solicitar {nome} à equipe de compras, temos apenas {quantidade} unidades em estoque.")
    else:
        print("Categoria inválida. As categorias válidas são: alimentos, bebidas, limpeza.")

# Solicitação de inputs ao usuário
nome_produto = input("Digite o nome do produto: ")
categoria_produto = input("Digite a categoria do produto (alimentos, bebidas, limpeza): ")
quantidade_produto = input("Digite a quantidade atual em estoque: ")

# Verificação se os inputs foram preenchidos corretamente
if nome_produto and categoria_produto and quantidade_produto:
    try:
        quantidade_produto = int(quantidade_produto)
        verifica_estoque(nome_produto, categoria_produto, quantidade_produto)
    except ValueError:
        print("Por favor, insira um número válido para a quantidade.")
else:
    print("Por favor, preencha todas as informações corretamente.")
```
