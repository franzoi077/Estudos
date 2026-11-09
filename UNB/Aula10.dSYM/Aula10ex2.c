#include <stdio.h>
#include <string.h>

int main () {
    char palavra1[50];
    char palavra2[50];

    printf("Digite a primeira palavra que pode ter ate 49 caracteres: ");
    fgets(palavra1, 50, stdin);

    printf("Digite a segunda palabra que pode ter ate 50 caracteres: ");
    fgets(palavra2, 50, stdin);

    if(strcmp(palavra1, palavra2) == 0){
        printf("as palavras são iguais\n");
    }
    else{
        printf("as palavras são diferentes\n");
    }

    return 0;
}