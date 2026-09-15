#include <stdio.h>

float calcular_area_triangulo(float base, float altura);
void exibir_area(float area);

float calcular_area_triangulo(float base, float altura) { //funcao que calcula a area
    return base * altura / 2;

}

void exibir_area(float area) {
    printf("A area do triangulo é: %.2f\n", area);
}

int main() {
    float base, altura; 
    
    printf("Digite o valor da base: \n");
    scanf("%f", &base);

    printf("Digite o valor da altura; \n");
    scanf("%f", &altura);

    float area = calcular_area_triangulo(base, altura);

    exibir_area(area);
    
    return 0;
}
