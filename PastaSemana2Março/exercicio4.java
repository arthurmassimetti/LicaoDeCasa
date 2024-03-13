import java.util.InputMismatchException;
import java.util.Scanner;

public class VerificadorNumero {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Por favor, insira um número inteiro:");
        int numero;

        try {
            numero = scanner.nextInt();
        } catch (InputMismatchException e) {
            System.out.println("Erro: O valor inserido não é um número inteiro.");
            return;
        }

        if (numero > 0) {
            System.out.println("O número é positivo.");
        } else if (numero < 0) {
            System.out.println("O número é negativo.");
        } else {
            System.out.println("O número é zero.");
        }

        if (numero % 2 == 0) {
            System.out.println("O número não é impar.");
        } else {
            System.out.println("O número é ímpar.");
        }
        
        scanner.close();
    }
}
