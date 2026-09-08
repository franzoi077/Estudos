// Área do Círculo
#include <stdio.h>
#include <math.h>
#define PI 3.14159
int main() {
    float raio, area;
    printf("Digite o raio do seu circulo: ");
    scanf("%f", &raio);

    area = PI * pow(raio, 2);
    
    printf("A area do circulo é: %.2f\n", area);

    return 0;
}