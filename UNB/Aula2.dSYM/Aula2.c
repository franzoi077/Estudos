#include <stdio.h>

int main() {
    double  peso, altura, imc;

    //entrada de dados
    printf("Digite seu peso: ");
    scanf("%lf", &peso);

    printf("Digite sua altura: ");
    scanf("%lf", &altura);

    //calcuraldora
    imc = peso / (altura * altura);
    
    //saida
    printf("Seu IMC: %.2f\n", imc);

    return 0;
}
