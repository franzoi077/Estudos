#include <stdio.h>
#include <string.h>

int main (){
    char palavra[50];
    printf("Digite uma palavra com no maximo 49 caracteres: ");
    scanf("%49s", palavra);

    int tamanho = strlen(palavra);

    printf("voce digitou a palabre \"%s\", que tem %d caracteres", palavra, tamanho);

    return 0;
}