#include <stdio.h>

void frahreinheit_para_celcius(void){
    float f;
    printf("temperatura em fahrenheit: \n");
    scanf("%f", &f);

    float c = (f -32) * 5/9;

    printf("A temperatura em celcios: %.2f\n", c);

}

void celcius_para_fahrenheit(void){
    float c;
    printf("temperatura em celcius: \n");
    scanf("%f", &c);

    float f = (c * (9.0/5)) * 32; //usa o 9.0 para maior precisão na hora da divisão 

    printf("A temperatura em fahrengeit: %.2f\n", c);

}

void km_para_milhas(void){
    float km;
    printf("distancia em km; \n");
    scanf("%f", &km);

    float mil = km * 0.621371;

    printf("A distancia em milhas é: %.2f\n", mil);
}

void milhas_para_km(void){
    float mil;
    printf("distancia em milhas: \n");
    scanf("%f", &mil);

    float km = mil / 0.621371;

    printf("a distancia em km é: %.2f", km);
}

int main(){
    int opcao;
    printf("===CONVERSOR===\n");
    printf("1 - celcius para fahrenheit\n");
    printf("2 - fahrenheit para celcius\n");
    printf("3 - km para milhas\n");
    printf("4 - milhas para km\n");
    printf("0 - sair\n");
    scanf("%d", &opcao);

    do { 
    
        switch (opcao){
    
            case 1:
            frahreinheit_para_celcius();
            break;
    
        case 2:
            celcius_para_fahrenheit();
            break;
    
        case 3:
            km_para_milhas();
            break;
    
        case 4:
            milhas_para_km();
            break;
    
        case 0:
            break;
    
        default:
            printf("opcao invalida");
            break;
    }
}   while (opcao != 0);

    return 0;
}