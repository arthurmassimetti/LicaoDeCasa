# Projeto Swing: Gerenciador de Tarefas e Calculadora de IMC

Este repositório contém dois exemplos de interfaces gráficas em Java utilizando **AWT** e **Swing**. A ideia é ilustrar a criação de um **Gerenciador de Tarefas** e de uma **Calculadora de IMC** com a interface gráfica desenvolvida em Java.

## Exemplo 1: Gerenciador de Tarefas

Neste exemplo, criamos uma interface gráfica que simula o registro de pedidos em um mercadinho. A interface permite adicionar produtos, suas quantidades e preços, e visualizá-los em uma tabela.

### Componentes Utilizados

- **JFrame**: A janela principal do aplicativo.
- **JLabel**: Etiquetas de texto para identificar os campos.
- **JTextField**: Campos de texto para inserir dados como nome do produto, quantidade e preço.
- **JButton**: Botão para adicionar o pedido à lista.
- **JTable**: Tabela para exibir os produtos adicionados.

### Funcionalidades

1. **Adicionar Pedido**: O botão "Adicionar Pedido" permite adicionar o nome do produto, a quantidade e o preço à tabela de pedidos.
2. **Remover Pedido**: Um botão opcional pode ser adicionado para remover itens da lista.
3. **Finalizar Pedido**: Outra funcionalidade opcional seria a de "Finalizar Pedido", que poderia exibir uma mensagem com o total dos pedidos.

### Exemplo de Código

```java
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GerenciadorTarefas extends JFrame {

    private JTextField campoProduto;
    private JTextField campoQuantidade;
    private JTextField campoPreco;
    private JTable tabelaPedidos;
    private DefaultTableModel modeloTabela;

    public GerenciadorTarefas() {
        setTitle("Gerenciador de Tarefas");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);

        JLabel labelProduto = new JLabel("Produto:");
        labelProduto.setBounds(20, 20, 80, 25);
        add(labelProduto);

        campoProduto = new JTextField();
        campoProduto.setBounds(100, 20, 150, 25);
        add(campoProduto);

        JLabel labelQuantidade = new JLabel("Quantidade:");
        labelQuantidade.setBounds(20, 60, 80, 25);
        add(labelQuantidade);

        campoQuantidade = new JTextField();
        campoQuantidade.setBounds(100, 60, 150, 25);
        add(campoQuantidade);

        JLabel labelPreco = new JLabel("Preço:");
        labelPreco.setBounds(20, 100, 80, 25);
        add(labelPreco);

        campoPreco = new JTextField();
        campoPreco.setBounds(100, 100, 150, 25);
        add(campoPreco);

        JButton botaoAdicionar = new JButton("Adicionar Pedido");
        botaoAdicionar.setBounds(100, 140, 150, 25);
        add(botaoAdicionar);

        modeloTabela = new DefaultTableModel(new Object[]{"Produto", "Quantidade", "Preço"}, 0);
        tabelaPedidos = new JTable(modeloTabela);
        JScrollPane scrollPane = new JScrollPane(tabelaPedidos);
        scrollPane.setBounds(20, 180, 350, 100);
        add(scrollPane);

        botaoAdicionar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String produto = campoProduto.getText();
                String quantidade = campoQuantidade.getText();
                String preco = campoPreco.getText();
                modeloTabela.addRow(new Object[]{produto, quantidade, preco});
            }
        });
    }

    public static void main(String[] args) {
        GerenciadorTarefas app = new GerenciadorTarefas();
        app.setVisible(true);
    }
}


```


## Exemplo 2: Calculadora de IMC

Neste exemplo, criaremos uma interface gráfica para calcular o **Índice de Massa Corporal (IMC)** de uma pessoa. O cálculo é feito a partir do peso e da altura fornecidos, com base na fórmula:

\[
\text{IMC} = \frac{\text{peso}}{(\text{altura})^2}
\]

### Componentes Utilizados

- **JFrame**: A janela principal do aplicativo.
- **JLabel**: Etiquetas de texto para identificar os campos.
- **JTextField**: Campos de texto para inserir o peso e a altura.
- **JButton**: Botão para realizar o cálculo do IMC.
- **JLabel**: Exibe o resultado do cálculo.

### Funcionalidades

1. **Cálculo do IMC**: Ao clicar no botão "Calcular IMC", o aplicativo calcula o IMC com base nos valores de peso e altura fornecidos e exibe o resultado.
2. **Classificação do IMC**: Exibe a classificação do IMC com base no valor calculado, como "Peso normal", "Abaixo do peso", "Sobrepeso", ou "Obesidade".

### Exemplo de Código

```java
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraIMC extends JFrame {

    private JTextField campoPeso;
    private JTextField campoAltura;
    private JButton botaoCalcular;
    private JLabel resultado;

    public CalculadoraIMC() {
        setTitle("Calculadora de IMC");
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);

        JLabel labelPeso = new JLabel("Peso (kg):");
        labelPeso.setBounds(20, 20, 80, 25);
        add(labelPeso);

        campoPeso = new JTextField();
        campoPeso.setBounds(100, 20, 150, 25);
        add(campoPeso);

        JLabel labelAltura = new JLabel("Altura (m):");
        labelAltura.setBounds(20, 60, 80, 25);
        add(labelAltura);

        campoAltura = new JTextField();
        campoAltura.setBounds(100, 60, 150, 25);
        add(campoAltura);

        botaoCalcular = new JButton("Calcular IMC");
        botaoCalcular.setBounds(100, 100, 150, 25);
        add(botaoCalcular);

        resultado = new JLabel("");
        resultado.setBounds(20, 140, 250, 25);
        add(resultado);

        botaoCalcular.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                calcularIMC();
            }
        });
    }

    private void calcularIMC() {
        try {
            double peso = Double.parseDouble(campoPeso.getText());
            double altura = Double.parseDouble(campoAltura.getText());
            double imc = peso / (altura * altura);

            String mensagem;
            if (imc < 18.5) {
                mensagem = "Abaixo do peso";
            } else if (imc < 24.9) {
                mensagem = "Peso normal";
            } else if (imc < 29.9) {
                mensagem = "Sobrepeso";
            } else {
                mensagem = "Obesidade";
            }

            resultado.setText("IMC: " + String.format("%.2f", imc) + " - " + mensagem);

        } catch (NumberFormatException ex) {
            resultado.setText("Entrada inválida.");
        }
    }

    public static void main(String[] args) {
        CalculadoraIMC app = new CalculadoraIMC();
        app.setVisible(true);
    }
}

```
