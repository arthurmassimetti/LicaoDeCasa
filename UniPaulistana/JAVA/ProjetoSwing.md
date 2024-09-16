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
