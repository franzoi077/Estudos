#include <stdio.h>
#include <math.h>

float raio, area, volume;
int main() {
    printf("Digite o raio da esfera: ");
    scanf("%f", &raio);

    area = 4 * M_PI * pow(raio, 2);
    volume = (4.0 / 3.0) * M_PI * pow(raio, 3);

    printf("Area da esfera: %.2f\n", area);
    printf("Volume da esfera: %.2f\n", volume);

    return 0;
}