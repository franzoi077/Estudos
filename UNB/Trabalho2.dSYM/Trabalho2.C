#include <stdio.h>
#include <math.h>
// Funcao para ler um valor positivo com direito a uma segunda tentativa
float ler_valor_positivo(char *rotulo) {
float valor;
printf("%s"
, rotulo);
scanf("%f"
, &valor);
// Verifica se o primeiro valor digitado nao e positivo
if (valor <= 0) {
printf("Valor invalido.\n");
printf("%s"
, rotulo);
scanf("%f"
, &valor); // Segunda tentativa usando apenas if-else
if (valor <= 0) {
printf("Valor invalido.\n");
}
}
return valor;
}
// Funcao que calcula o montante em juros simples
float juros_simples(float capital, float taxa, int meses) {
float i = taxa / 100.0f; // Conversao de porcentagem para fator decimal
return capital * (1.0f + i * meses);
}
// Funcao que calcula o montante em juros compostos
float juros_compostos(float capital, float taxa, int meses) {
float i = taxa / 100.0f; // Conversao de porcentagem para fator decimal
return capital * pow(1.0f + i, meses);
}
// Funcao que exibe o relatorio final formatado
void exibir_relatorio(float capital, float taxa, int meses, float ms, float mc) {
float diferenca = fabs(mc - ms); // Diferenca absoluta entre os montantes
printf("\n--- Relatorio de Investimento ---\n");
printf("Capital inicial: R$ %.2f\n"
, capital);
printf("Taxa mensal: %.2f%%\n"
, taxa);
printf("Prazo: %d meses\n"
, meses);
printf("Montante (Juros Simples): R$ %.2f\n"
, ms);
printf("Montante (Juros Compostos): R$ %.2f\n"
, mc);
printf("Diferenca entre os regimes: R$ %.2f\n"
, diferenca);
}
int main(void) {
float capital, taxa, ms, mc;
int meses;
// 1. Leitura e validacao das entradas
capital = ler_valor_positivo("Digite o capital inicial (R$): ");
if (capital <= 0) return 0;
taxa = ler_valor_positivo("Digite a taxa de juros mensal (%%): ");
if (taxa <= 0) return 0;
// Leitura do prazo convertendo o retorno float para int
meses = (int)ler_valor_positivo("Digite o prazo (meses): ");
if (meses <= 0) return 0;
// 2. Calculo dos dois regimes
ms = juros_simples(capital, taxa, meses);
mc = juros_compostos(capital, taxa, meses);
// 3. Exibicao dos resultados
exibir_relatorio(capital, taxa, meses, ms, mc);
return 0;
}