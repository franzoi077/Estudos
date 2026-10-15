#include <stdio.h>
int main () {
    int numero;
    int soma = 0, par = 0;
    printf("Digite o valor de n: ");
    scanf("%d", &numero);
    for (int i = 0; i <= numero; i++){
        soma += i;
        if (i % 2 == 0){
            par ++;
        }
    }
    printf("a soma é: %d\n", soma);
    printf("%d são pares\n", par);

    return 0;
}