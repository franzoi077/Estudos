#include <stdio.h>
#include <math.h>

// Estrutura para representar um ponto no plano cartesiano
typedef struct {
    double x;
    double y;
} Ponto;

// Função para calcular a distância entre dois pontos
double calcularDistancia(Ponto p1, Ponto p2) {
    double difX = p2.x - p1.x;
    double difY = p2.y - p1.y;
    
    return sqrt(pow(difX, 2) + pow(difY, 2));
}

int main() {
    Ponto p1, p2;

    printf("=== Calculadora de Distância Cartesiana ===\n\n");

    // Coordenadas do primeiro ponto
    printf("Digite as coordenadas do Ponto 1 (x y): ");
    if (scanf("%lf %lf", &p1.x, &p1.y) != 2) {
        printf("Entrada inválida.\n");
        return 1;
    }

    // Coordenadas do segundo ponto
    printf("Digite as coordenadas do Ponto 2 (x y): ");
    if (scanf("%lf %lf", &p2.x, &p2.y) != 2) {
        printf("Entrada inválida.\n");
        return 1;
    }

    // Cálculo da distância
    double distancia = calcularDistancia(p1, p2);

    // Exibição do resultado
    printf("\nA distância entre P1(%.2lf, %.2lf) e P2(%.2lf, %.2lf) é: %.4lf\n", 
           p1.x, p1.y, p2.x, p2.y, distancia);

    return 0;
}