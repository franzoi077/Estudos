#include <stdio.h>

int main() {
    int numeros[10];
    int ja_contado[10] = {0}; // 0 = nao analisado, 1 = ja analisado
    int i, j;
    int encontrou_duplicados = 0;

    // 1. Leitura dos 10 valores
    for (i = 0; i < 10; i++) {
        printf("Digite o valor %d/10: ", i + 1);
        scanf("%d", &numeros[i]);
    }

    // 2. Contagem de frequencias
    for (i = 0; i < 10; i++) {
        // Se este numero ja foi analisado em uma repeticao anterior, pula
        if (ja_contado[i]) {
            continue;
        }

        int contagem = 1;

        // Compara com as posicoes seguintes
        for (j = i + 1; j < 10; j++) {
            if (numeros[i] == numeros[j]) {
                contagem++;
                ja_contado[j] = 1; // Marca o indice duplicado para nao processar depois
            }
        }

        // Se apareceu mais de uma vez, exibe
        if (contagem > 1) {
            printf("O numero %d apareceu %d vezes.\n", numeros[i], contagem);
            encontrou_duplicados = 1;
        }
    }

    if (!encontrou_duplicados) {
        printf("Nenhum valor duplicado foi encontrado.\n");
    }

    return 0;
