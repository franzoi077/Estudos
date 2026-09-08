//Conversor de temperatura fahrenheit para celsius e vice-versa
#include <stdio.h>
int main() {
    float celsius, fahrenheit;
    int opcao;

    printf("Escolha a conversão:\n");
    printf("1. Celsius para Fahrenheit\n");
    printf("2. Fahrenheit para Celsius\n");
    printf("Digite a opção (1 ou 2): ");
    scanf("%d", &opcao);

    if (opcao == 1) {
        printf("Digite a temperatura em Celsius: ");
        scanf("%f", &celsius);
        fahrenheit = (celsius * 9 / 5) + 32;
        printf("%.2f Celsius é igual a %.2f Fahrenheit\n", celsius, fahrenheit);
    } 
    
    else if (opcao == 2) {
        printf("Digite a temperatura em Fahrenheit: ");
        scanf("%f", &fahrenheit);
        celsius = (fahrenheit - 32) * 5 / 9;
        printf("%.2f Fahrenheit é igual a %.2f Celsius\n", fahrenheit, celsius);
    } 
    
    else {
        printf("Opção inválida!\n");
    }

    return 0;
}