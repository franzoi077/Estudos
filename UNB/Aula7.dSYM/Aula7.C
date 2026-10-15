#include <stdio.h>

int main (){
    int numero, soma = 0;
    printf("Digite numeros inteiro (0 para encerrar):\n");
    scanf("%d", &numero);
    while (numero != 0){
        soma += numero;
        scanf("%d", &numero);
    }
    printf("A soma dos numeros é: %d\n", soma);
    return 0;   
}