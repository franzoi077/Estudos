#include <stdio.h>

int quadrado (int numero){
    int resultado = numero * numero;
    return resultado;
}

int main() { 
    int num = 4;
    int resultado = quadrado(num);
    
    printf("%d\n", resultado);
    return 0;

}
