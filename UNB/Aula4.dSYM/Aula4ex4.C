#include <stdio.h>
float m, c, i;
int t;
int main() {
    printf("Digite o valor do capital: \n");
    scanf("%f", &c);
    
    printf("Digite o valor da taxa de juros: \n");
    scanf("%f", &i);
    
    printf("Digite o valor do tempo: \n");
    scanf("%d", &t);
    
    m = c * (1 + i * t);
    printf("O montante é: %.2f\n", m);

    return 0;
}