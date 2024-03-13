import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem-vindo à Calculadora!");
        System.out.print("Por favor, insira o primeiro número: ");
        double numero1 = scanner.nextDouble();

        System.out.print("Agora, insira o segundo número: ");
        double numero2 = scanner.nextDouble();

        System.out.println("Escolha uma operação:");
        System.out.println("1. Adição (+)");
        System.out.println("2. Subtração (-)");
        System.out.println("3. Multiplicação (*)");
        System.out.println("4. Divisão (/)");

        int escolha = scanner.nextInt();

        double resultado = 0;

        switch (escolha) {
            case 1:
                resultado = numero1 + numero2;
                break;
            case 2:
                resultado = numero1 - numero2;
                break;
            case 3:
                resultado = numero1 * numero2;
                break;
            case 4:
                if (numero2 != 0) {
                    resultado = numero1 / numero2;
                } else {
                    System.out.println("Erro: Divisão por zero não é permitida.");
                    return;
                }
                break;
            default:
                System.out.println("Opção inválida. Por favor, selecione uma opção válida de 1 a 4.");
                return;
        }

        System.out.println("O resultado da operação é: " + resultado);

        scanner.close();
    }
}
