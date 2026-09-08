#include <stdio.h>
float c, f;
int main() {
    printf("Digite o valor em graus celsius: \n");
    scanf("%f", &c);

    f = 1.8 * c + 32;
    printf("O valor em graus fahrenheit é: %.2f\n", f);

    return 0;
}