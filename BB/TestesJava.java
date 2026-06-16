import java.util.*;
import java.util.stream.Collectors;

public class TestesJava {
    public static void main(String[] args) { // método principal, ponto de entrada do programa
        List<Integer> lista = List.of(1, 2, 3, 4, 5); // cria uma lista imutável com os números de 1 a 5
        
        Set<Integer> resultado = lista.stream() // faz com que passe a ser um fluxo de dados
            .filter(n -> n % 2 == 0) // filtra os números pares
            .collect(Collectors.toSet()); // coleta os resultados em um Set

        System.out.println(resultado); // imprime o resultado, que será um conjunto de números pares
    }
}
