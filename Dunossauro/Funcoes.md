#   o  que são funções e para que servem?
# função é um bloco de código reutilizável que realiza uma tarefa específica. Ela pode receber entradas (chamadas de parâmetros) e retornar uma saída (chamada de valor de retorno). As funções são usadas para organizar o código, evitar repetição e melhorar a legibilidade. Elas permitem que você escreva um código mais modular e fácil de manter, facilitando a resolução de problemas complexos dividindo-os em partes menores e mais gerenciáveis.

# um subprograma é uma abstração de um processo, encapsulada, reutilizável, que geralmente tem um nome e pode ser parametizável
abstração de processo (uma lista de passos para realizar uma tarefa específica)
encapsulada (com sua lógica isolada do restante do código)
reutilizável (pode ser chamada diversas vezes em diferentes partes do programa)
geralmente pode receber um nome
parametrizável (pode aceitar entradas para personalizar seu comportamento)

Exemplo de função simples em Python:
def saudacao(nome):
    return f"Olá, {nome}!"
Usando a função
print(saudacao("Dunossauro"))

- as chamadas de subprogramas são feitas a partir do seu nome, seguido de () 
- são retulizáveis, pois podem ser chamdas diversas vezes em diferentes partes do programa
* o termo tecnico é callable -> siguinifica chamavém em ingles, ou seja, algo que pode ser chamado como uma função

- exitem duas categorias de subprogramas: funções e procedimentos
. procedimentos[procedures] -> Não retornam um valor, apenas executam uma ação 
. funções[Functions] -> Retornam um valor após a execução