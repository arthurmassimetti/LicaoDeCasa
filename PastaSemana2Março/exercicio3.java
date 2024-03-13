import java.util.Scanner;

public class VerificadorTemperatura {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Por favor, insira a temperatura:");
        double temperatura = scanner.nextDouble();

        if (temperatura >= 20 && temperatura <= 30) {
            System.out.println("A temperatura está dentro da faixa desejada (>=20 e <=30).");
        } else {
            System.out.println("A temperatura está fora da faixa desejada.");
        }
        
        scanner.close();
    }
}
