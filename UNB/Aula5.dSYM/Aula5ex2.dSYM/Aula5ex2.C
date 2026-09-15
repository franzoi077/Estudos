#include <stdio.h>

#define cotacao 5.15

float transformar_dolar(float reais);

float transformar_dolar(float reais) { //tranforma reais para dolar de acordo com uma cotacao fixa
    return reais / cotacao;
}


int main() { 
    float reais, valor_em_dolar;
    printf("Digite a quatidade que voce quer converter: \n");
    scanf("%f", &reais);

    valor_em_dolar = transformar_dolar(reais);

    printf("o valor em dolares é: %.2f\n", valor_em_dolar);

    return 0;
}
