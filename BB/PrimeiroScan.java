import java.util.Scanner;

public class PrimeiroScan {
    public static void main(String[] args) {
        try (Scanner leitor = new Scanner(System.in)) { // é o scanner para ler a entrada do usuário
            System.out.println("Digite seu nome:"); 
            String nome = leitor.nextLine(); // le a linha de entrada do usuário e armazena na variável nome
            
            System.out.println("Digite sua idade:");
            int idade = leitor.nextInt(); // le a próxima entrada do usuário como um inteiro e armazena na variável idade
            System.out.println("Olá, " + nome + "! Você tem " + idade + " anos."); // imprime uma mensagem de saudação usando o nome e a idade do usuário   
        }
    }
}
