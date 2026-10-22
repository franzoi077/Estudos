#include <stdio.h>

int main () {
    float notas[50];
    int num_alunos, i;
    float soma = 0, media, menor, maior;

    printf("quantos alunos tem a turma(maximo 50): "); // descobrindo a quantidade de alunos
    scanf("%d", &num_alunos);

    if (num_alunos <= 0 || num_alunos > 50){ //validando a quantidade de alunos
        printf("Numero invalido de alunos\n");
        return 1;
    }
    
    for(i = 0; i < num_alunos; i++){ //registrando a nota
        printf("Digite a nota do aluno %d: ", i + 1);
        scanf("%f", &notas[i]);

        if (notas[i] < 0 || notas[i] > 10){ //validar a nota 
            printf("nota invalida, tem que ser de 0 a 10\n");
            continue;
        }
        soma += notas[i];
    }

    media = soma / num_alunos; //descobrindo a media

    maior = menor = notas[0];

    for (i = 0; i < num_alunos; i++){ // descobrindo a maior e a menor nota
        if(maior < notas[i]) maior = notas[i];
        if(menor > notas[i]) menor = notas[i];
    }

    int aprovados = 0, reprovados = 0;

    for (i = 0; i < num_alunos; i++){ //descobrindo a quantidade de alunos aprovados ou reprovados
        if(notas[i] >= 5.0){
            aprovados ++;
        }
        else{
            reprovados++;
        }
    }
    
    // exebindo resultados
    printf("\nResultados da turma:\n");
    printf("Media da turma: %.2f\n", media);
    printf("Maior nota: %.2f\n", maior);
    printf("Menor nota: %.2f\n", menor);
    printf("Aprovados: %d (%.1f%%)\n", aprovados, (float)aprovados / num_alunos * 100); //exebindo aqui com a porcentagem de aprovados ou reprovados na linha de baixo 
    printf("Reprovados: %d (%.1f%%)\n", reprovados, (float)reprovados / num_alunos * 100);
    
    return 0;
}