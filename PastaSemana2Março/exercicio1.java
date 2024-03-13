import java.util.Scanner;


public class JavaApplication1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem-vindo à calculadora de área de retângulo!");
        System.out.print("Por favor, insira a base do retângulo: ");
        double base = scanner.nextDouble();

        System.out.print("Agora, por favor, insira a altura do retângulo: ");
        double altura = scanner.nextDouble();

        double area = calcularArea(base, altura);

        System.out.println("A área do retângulo com base " + base + " e altura " + altura + " é: " + area);
        
        scanner.close();
    }

    public static double calcularArea(double base, double altura) {
        return base * altura;
    }
}
