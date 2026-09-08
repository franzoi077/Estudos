#include <stdio.h>
int s, dias, h, m, seg;

int main() {
    printf("Digite o valor em segundos: \n");
    scanf("%d", &s);

    dias = s / 86400;
    h = (s % 86400) / 3600;
    m = (s % 3600) / 60;
    seg = s % 60;

    printf("O valor em dias, horas, minutos e segundos é: %d dias, %d horas, %d minutos e %d segundos\n", dias, h, m, seg);

    return 0;
}