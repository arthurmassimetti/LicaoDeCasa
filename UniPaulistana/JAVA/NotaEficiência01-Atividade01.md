```java
public class Heroi {
    private String nome;
    private String poder;
    private double altura;
    private int idade;

    // Construtor
    public Heroi(String nome, String poder, double altura, int idade) {
        setNome(nome);
        setPoder(poder);
        setAltura(altura);
        setIdade(idade);
    }

    // Getters e Setters com validações
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if(nome != null && !nome.isEmpty()) {
            this.nome = nome;
        } else {
            throw new IllegalArgumentException("Nome não pode ser vazio.");
        }
    }

    public String getPoder() {
        return poder;
    }

    public void setPoder(String poder) {
        if(poder != null && !poder.isEmpty()) {
            this.poder = poder;
        } else {
            throw new IllegalArgumentException("Poder não pode ser vazio.");
        }
    }

    public double getAltura() {
        return altura;
    }

    public void setAltura(double altura) {
        if(altura > 0) {
            this.altura = altura;
        } else {
            throw new IllegalArgumentException("Altura deve ser positiva.");
        }
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        if(idade >= 0) {
            this.idade = idade;
        } else {
            throw new IllegalArgumentException("Idade não pode ser negativa.");
        }
    }

    public void exibirInformacoes() {
        System.out.println("Nome: " + getNome());
        System.out.println("Poder: " + getPoder());
        System.out.println("Altura: " + getAltura());
        System.out.println("Idade: " + getIdade());
        System.out.println("---------------------------");
    }
}

```

```Java
public class TestaHeroi {
    public static void main(String[] args) {
        Heroi heroi1 = new Heroi("Superman", "Força", 1.90, 30);
        Heroi heroi2 = new Heroi("Batman", "Inteligência", 1.85, 35);
        Heroi heroi3 = new Heroi("Mulher-Maravilha", "Agilidade", 1.80, 28);

        heroi1.exibirInformacoes();
        heroi2.exibirInformacoes();
        heroi3.exibirInformacoes();
    }
}

```

```Java
public class Veiculo {
    private String marca;
    private String modelo;
    private int anoFabricacao;
    private String combustivel;
    private double velocidadeAtual;

    // Construtor
    public Veiculo(String marca, String modelo, int anoFabricacao, String combustivel) {
        this.marca = marca;
        this.modelo = modelo;
        this.anoFabricacao = anoFabricacao;
        this.combustivel = combustivel;
        this.velocidadeAtual = 0;
    }

    public void ligar() {
        System.out.println("O veículo foi ligado.");
    }

    public void acelerar(double velocidade) {
        if (velocidade > 0) {
            this.velocidadeAtual += velocidade;
            System.out.println("O veículo acelerou para " + this.velocidadeAtual + " km/h.");
        }
    }

    public void frear(double velocidade) {
        if (velocidade > 0 && this.velocidadeAtual - velocidade >= 0) {
            this.velocidadeAtual -= velocidade;
            System.out.println("O veículo desacelerou para " + this.velocidadeAtual + " km/h.");
        } else {
            System.out.println("Não é possível frear para uma velocidade negativa.");
        }
    }

    public void exibirInformacoes() {
        System.out.println("Marca: " + this.marca);
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Ano de Fabricação: " + this.anoFabricacao);
        System.out.println("Combustível: " + this.combustivel);
        System.out.println("Velocidade Atual: " + this.velocidadeAtual + " km/h");
        System.out.println("---------------------------");
    }
}

```

```Java
public class TesteVeiculo {
    public static void main(String[] args) {
        Veiculo veiculo1 = new Veiculo("Toyota", "Corolla", 2020, "Gasolina");
        Veiculo veiculo2 = new Veiculo("Honda", "Civic", 2021, "Etanol");

        veiculo1.ligar();
        veiculo1.acelerar(50.0);
        veiculo1.frear(20.0);
        veiculo1.exibirInformacoes();

        veiculo2.ligar();
        veiculo2.acelerar(60.0);
        veiculo2.frear(30.0);
        veiculo2.exibirInformacoes();
    }
}

```
