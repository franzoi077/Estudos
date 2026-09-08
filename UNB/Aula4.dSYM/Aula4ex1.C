#include <stdio.h>
int a, b, c, d, mediap;
int main() {
    
    printf("Digite o valor da primeira nota: \n");
    scanf("%d", &a);
    
    printf("Digite o valor da segunda nota: \n");
    scanf("%d", &b);
    
    printf("Digite o valor da terceira nota: \n");
    scanf("%d", &c);
    
    printf("Digite o valor da quarta nota: \n");
    scanf("%d", &d);
    
    mediap = (2*a + 3*b + 3*c + 2*d)/10;
    printf("A média ponderada é: %d\n", mediap);

    return 0;
}