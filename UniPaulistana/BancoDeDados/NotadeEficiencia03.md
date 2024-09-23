
# Sistema de Gerenciamento de Biblioteca

## Descrição do Projeto
Este projeto consiste no desenvolvimento de um sistema de gerenciamento de biblioteca utilizando um banco de dados relacional. O objetivo é armazenar informações sobre livros e usuários, facilitando o controle do acervo e o registro de novos membros.

## Estrutura do Banco de Dados

### 1. Criação do Banco de Dados

Para iniciar, vamos criar o banco de dados chamado `Biblioteca` e definir o contexto de uso:

```bash
CREATE DATABASE Biblioteca;
USE Biblioteca;
```

### 2. Tabelas

#### Tabela `Livros`
A tabela `Livros` será utilizada para armazenar as informações sobre os livros disponíveis na biblioteca. A estrutura da tabela é definida como segue:

```sql
CREATE TABLE Livros (
    id INT(3) PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(50) NOT NULL,
    ano_publicacao INT(4) NOT NULL,
    genero VARCHAR(30) NOT NULL
);
```

##### Descrição das Colunas:
- **id**: Identificador único do livro.
- **titulo**: Título do livro.
- **autor**: Nome do autor do livro.
- **ano_publicacao**: Ano de publicação do livro.
- **genero**: Gênero literário do livro.

#### Tabela `Usuarios`
A tabela `Usuarios` armazena as informações dos usuários cadastrados na biblioteca. A estrutura da tabela é:

```sql
CREATE TABLE Usuarios (
    id INT(3) PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    endereco VARCHAR(100),
    data_registro DATE NOT NULL
);
```

##### Descrição das Colunas:
- **id**: Identificador único do usuário.
- **nome**: Nome completo do usuário.
- **email**: Endereço de e-mail do usuário.
- **telefone**: Número de telefone para contato.
- **endereco**: Endereço residencial do usuário.
- **data_registro**: Data de registro do usuário na biblioteca.

### 3. Alterações na Estrutura das Tabelas

#### Remover a Coluna `disponivel` da Tabela `Livros`
Caso a coluna `disponivel` tenha sido previamente criada na tabela `Livros`, ela pode ser removida com o comando:

```sql
ALTER TABLE Livros DROP COLUMN disponivel;
```

### 4. Consultas

#### Consulta para Exibir Todos os Livros
Para listar todos os registros presentes na tabela `Livros`, utilize o seguinte comando:

```sql
SELECT * FROM Livros;
```

#### Consulta para Exibir Todos os Usuários
Para visualizar todos os usuários cadastrados na biblioteca, utilize o comando abaixo:

```sql
SELECT * FROM Usuarios;
```

## Instruções para Execução

1. **Criar o Banco de Dados e as Tabelas:**
   - Execute os comandos SQL fornecidos acima para criar o banco de dados `Biblioteca` e as tabelas `Livros` e `Usuarios`.

2. **Inserir Dados nas Tabelas:**
   - Após a criação das tabelas, você pode inserir registros utilizando comandos `INSERT` conforme necessário.

3. **Realizar Consultas:**
   - Utilize as consultas fornecidas para visualizar os dados cadastrados nas tabelas.

## Considerações Finais
Este projeto proporciona um ponto de partida para a gestão de bibliotecas utilizando um banco de dados relacional. A estrutura criada permite armazenar informações de forma organizada, com a possibilidade de futuras expansões, como o controle de empréstimos de livros e a inclusão de novas funcionalidades.


