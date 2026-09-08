//media de notas
#include <stdio.h>
#include <math.h>

#define PESO1 1
#define PESO2 2
#define PESO3 3
int main() {
    float nota1, nota2, nota3, media;
    printf("digite quanto voce tirou na p1: ");
    scanf("%f", &nota1);

    printf("digite quanto voce tirou na p2: ");
    scanf("%f", &nota2);

    printf("Digite quanto voce tirou na p3: ");
    scanf("%f", &nota3);

    media = (nota1 * PESO1) + (nota2 * PESO2) + (nota3 + PESO3);

    printf("Sua media é: %.2f\n", media);

    return 0;
}