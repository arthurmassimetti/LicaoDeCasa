### Parte 1 - Workbench
Criar a base de dados no MySQL Workbench:
```SQL
CREATE DATABASE Cinema;
USE Cinema;
```

Criar a tabela Filmes:
```SQL
CREATE TABLE Filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    duracao INT,
    genero VARCHAR(100)
);
```

### Parte 2 - JDBC
Criar o projeto na IDE: Se você estiver usando IntelliJ ou Eclipse, crie um novo projeto Java e adicione o arquivo JAR do JDBC na sua pasta lib.

Adicionar o JAR do JDBC: Faça o download do JAR aqui, adicione no classpath do projeto.

String de conexão JDBC: Use a seguinte string para conectar ao banco de dados MySQL:

```java
String url = "jdbc:mysql://localhost:3306/Cinema";
String user = "seu_usuario"; // Coloque seu usuário MySQL
String password = "sua_senha"; // Coloque sua senha MySQL
Connection conn = DriverManager.getConnection(url, user, password);
```

### Operações CRUD:

Método create:

```java
public void create(Connection conn, String nome, int duracao, String genero) throws SQLException {
    String sql = "INSERT INTO Filmes (nome, duracao, genero) VALUES (?, ?, ?)";
    PreparedStatement stmt = conn.prepareStatement(sql);
    stmt.setString(1, nome);
    stmt.setInt(2, duracao);
    stmt.setString(3, genero);
    stmt.executeUpdate();
}

```

Método read:

```java
public void read(Connection conn) throws SQLException {
    String sql = "SELECT * FROM Filmes";
    Statement stmt = conn.createStatement();
    ResultSet rs = stmt.executeQuery(sql);
    while (rs.next()) {
        System.out.println(rs.getInt("id") + " - " + rs.getString("nome") + ", " + rs.getInt("duracao") + " min, " + rs.getString("genero"));
    }
}

```

Método update:

```java
public void update(Connection conn, int id, String novoNome) throws SQLException {
    String sql = "UPDATE Filmes SET nome = ? WHERE id = ?";
    PreparedStatement stmt = conn.prepareStatement(sql);
    stmt.setString(1, novoNome);
    stmt.setInt(2, id);
    stmt.executeUpdate();
}

```

Método delete:

```java
public void delete(Connection conn, int id) throws SQLException {
    String sql = "DELETE FROM Filmes WHERE id = ?";
    PreparedStatement stmt = conn.prepareStatement(sql);
    stmt.setInt(1, id);
    stmt.executeUpdate();
}

```

### Inserir filmes e testar CRUD:
Inserir 10 filmes: No método main, você pode fazer algo como:

```java
public static void main(String[] args) {
    try {
        Connection conn = DriverManager.getConnection(url, user, password);
       
        CinemaDAO cinema = new CinemaDAO();

        cinema.create(conn, "Filme 1", 120, "Ação");

        cinema.update(conn, 1, "Novo Filme 1");
        cinema.update(conn, 2, "Novo Filme 2");

        cinema.delete(conn, 10);

        cinema.read(conn);

    } catch (SQLException e) {
        e.printStackTrace();
    }
}

```


### Teste no Workbench:
Execute o seguinte comando no Workbench para verificar os dados:

```sql
SELECT * FROM Filmes;

```
