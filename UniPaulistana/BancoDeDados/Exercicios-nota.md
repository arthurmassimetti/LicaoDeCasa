### 1. Criação da base de dados e tabelas:

```bash

-- Criação da base de dados Comercio
CREATE DATABASE Comercio;

-- Usar a base de dados Comercio
USE Comercio;

-- Criação da tabela Fatura
CREATE TABLE Fatura (
    numFatura INT,
    codCliente INT
);

-- Criação da tabela Produto
CREATE TABLE Produto (
    codProduto INT,
    descricao VARCHAR(50)
);

```
### 2. Alterações nas tabelas:



```bash

-- Alterar o nome da tabela Fatura para Pedidos
ALTER TABLE Fatura RENAME TO Pedidos;

-- Incluir o campo dataPed na tabela Pedidos
ALTER TABLE Pedidos ADD COLUMN dataPed DATE;

-- Incluir o campo precoCompra na tabela Produto
ALTER TABLE Produto ADD COLUMN precoCompra DECIMAL(10, 2);

-- Alterar o tipo de dado do campo descrição para varchar(25) na tabela Produto
ALTER TABLE Produto MODIFY descricao VARCHAR(25);

```

### 3. Criação da base de dados "Carro" e tabelas:

```bash

-- Criação da base de dados Carro
CREATE DATABASE Carro;

-- Usar a base de dados Carro
USE Carro;

-- Criação da tabela Cliente
CREATE TABLE Cliente (
    CPF INT,
    nome VARCHAR(50),
    numConta INT,
    telefone VARCHAR(10),
    cidade VARCHAR(50)
);

-- Criação da tabela Carro
CREATE TABLE Carro (
    CHASSI VARCHAR(10),
    modelo VARCHAR(50),
    cor VARCHAR(20),
    ano INT,
    valor DECIMAL(10, 2)
);

```

### 4. Inserção dos dados:

```bash

-- Inserção dos dados na tabela Cliente
INSERT INTO Cliente (CPF, nome, numConta, telefone, cidade)
VALUES 
    (111111, 'Ana', 2317, '019', 'Campinas'),
    (222222, 'Fábio', 1711, '011', 'Jundiaí'),
    (121111, 'Maria', 7121, '011', 'São Paulo'),
    (321222, 'Flávio', 2211, '019', 'Campinas'),
    (123111, 'Fernando', 1123, '021', 'Rio de Janeiro'),
    (217222, 'Marta', 3211, '031', 'Belo Horizonte');

-- Inserção dos dados na tabela Carro
INSERT INTO Carro (CHASSI, modelo, cor, ano, valor)
VALUES 
    ('A21', 'Uno', 'Prata', 2003, 0),
    ('2AC', 'Gol', 'Preto', 2004, 0),
    ('33A', 'Corsa', 'Branco', 2005, 0),
    ('12C', 'Uno', 'Verde', 2001, 0),
    ('1C2', 'Astra', 'Prata', 2005, 0),
    ('22A', 'Gol', 'Prata', 2005, 0);

```

### 5. Operações SQL pedidas:

```bash

-- Incluir uma linha na tabela Cliente com um campo em branco
INSERT INTO Cliente (CPF, nome, numConta, telefone, cidade)
VALUES (null, 'Pedro', 1212, '022', 'Brasília');

-- Inserir um registro na tabela Carro (na ordem: valor, cor, ano, CHASSI, modelo)
INSERT INTO Carro (valor, cor, ano, CHASSI, modelo)
VALUES (15000, 'Azul', 2010, '99X', 'Palio');

-- Alterar o campo telefone para '019' em toda a tabela Cliente
UPDATE Cliente
SET telefone = '019';

-- Alterar o nome de um registro da tabela Cliente para 'André'
UPDATE Cliente
SET nome = 'André'
WHERE CPF = 111111;

-- Alterar a cidade para 'Brasília' onde numConta é maior que 2000
UPDATE Cliente
SET cidade = 'Brasília'
WHERE numConta > 2000;

-- Modificar todos os valores dos carros para 20.000
UPDATE Carro
SET valor = 20000;

-- Alterar todos os modelos Uno e Corsa para a cor Azul
UPDATE Carro
SET cor = 'Azul'
WHERE modelo IN ('Uno', 'Corsa');

-- Excluir os clientes da cidade de Campinas
DELETE FROM Cliente
WHERE cidade = 'Campinas';

-- Excluir os veículos dos anos 2003 e 2004
DELETE FROM Carro
WHERE ano IN (2003, 2004);

-- Excluir o veículo com CHASSI '22A'
DELETE FROM Carro
WHERE CHASSI = '22A';

```
