#include <stdio.h>
int main() {
    int n, i = 0;
    int multiplo = 0, soma = 0;
    
    do { //validador de numero com do-while
        printf("Digite um numero: ");
        scanf("%d", &n);

    }while (n < 1 && n >10);
    
    while ((i < 10))//gerador da tabuada
    {
        i++;
        multiplo = n * i;
        soma += multiplo;

        printf("%d X %d = %d\n", n, i, multiplo);    
    }
    printf("soma = %d\n", soma );
    return 0;
    
}