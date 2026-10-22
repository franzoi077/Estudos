#include <stdio.h>

int main(void) {

    // Declaracao das variaveis do tipo inteiro

    int numero;

    int d1, d2, d3, d4, d5;

    int soma;

    // Entrada de dados

    printf("Digite um número de cinco dígitos: ");

    scanf("%d", &numero);

    // 1. Validacao do intervalo (deve estar entre 10000 e 99999)

    if (numero < 10000 || numero > 99999) {


        return 0; // Encerra o programa imediatamente

    }

    // 2. Decomposicao dos cinco algarismos usando apenas / e %

    d1 = numero / 10000;          // Extrai a dezena de milhar (1o digito)

    d2 = (numero / 1000) % 10;    // Extrai a unidade de milhar (2o digito)

    d3 = (numero / 100) % 10;     // Extrai a centena (3o digito)

    d4 = (numero / 10) % 10;      // Extrai a dezena (4o digito)

    d5 = numero % 10;             // Extrai a unidade (5o digito)

    // Exibicao dos algarismos separados por espaco

    printf("Algarismos: %d %d %d %d %d\n", d1, d2, d3, d4, d5);

    // 3. Calculo e exibicao da soma dos algarismos

    soma = d1 + d2 + d3 + d4 + d5;

    printf("Soma dos algarismos: %d\n", soma);

    // 4. Verificacao de palindromo (compara extremidades simetricas)

    if (d1 == d5 && d2 == d4) {

        printf("O número E um palíndromo.\n");

    } else {

        printf("O número NAO e um palíndromo.\n");

    }

    // 5. Verificacao da paridade da soma

    if (soma % 2 == 0) {

        printf("A soma dos algarismos e PAR.\n");

    } else {

        printf("A soma dos algarismos e IMPAR.\n");

    }

    return 0;

}
