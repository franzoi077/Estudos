#include <stdio.h>

double calcular_imc(double peso, double altura);

double calcular_imc(double peso, double altura) {
    return peso / (altura * altura);
}

int main() {
    double peso, altura, imc;
    
    printf("Digite seu peso: \n");
    scanf("%lf", &peso);

    printf("Digite sua altura: \n");
    scanf("%lf", &altura);

    imc = calcular_imc(peso, altura);

    printf("Seu IMC é: %.2lf\n", imc);

    return 0;
}
