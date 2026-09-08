#include <stdio.h>
int a = 1234;
int primeiro, segundo, terceiro, quarto;
int main() {
    primeiro = a % 10;
    printf("o ultimo digito é %d\n", primeiro);
    
    segundo = (a / 10) % 10;
    printf("o penultimo digito é %d\n", segundo);
    
    terceiro = (a / 100) % 10;
    printf("o antepenultimo digito é %d\n", terceiro);
    
    quarto = (a / 1000) % 10;
    printf("o primeiro digito é %d\n", quarto);

    return 0;
}