#desafio 22: Ler o nome completo de uma pessoa e mostrar: O nome com todas as letras maiúsculas, O nome com todas as letras minúsculas, Quantas letras ao todo (sem considerar os espaços), Quantas letras tem o primeiro nome
nome = str(input('digite seu nome completo: ')).strip()
print('seu nome em maiúsculo é {}'.format(nome.upper()))
print('seu nome em minúsculo é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))

#desafio 23:ler um número e mostrar o número da unidade, dezena, centena e milhar
num = str(input('digite um número de 0 a 9999; '))
print('analisando o número {}'.format(num))
print('unidade: {}'.format(num[3]))
print('dezena: {}'.format(num[2]))
print('centena: {}'.format(num[1]))
print('milhar: {}'.format(num[0]))

#desafio 24: ler o nome de uma cidade e mostrar se ela começa ou não com o nome "SANTO"
cidade = str(input('digite o nome de uma cidade: ')).strip()
print('a cidade começa com santo? {}'.format(cidade.upper().find('SANTO') == 0))
#o uso do find('SANTO') == 0 é para verificar se a substring "SANTO" está presente no início da string cidade. O método find() retorna a posição da primeira ocorrência da substring, e se ela estiver no início da string, a posição será 0. Portanto, se find('SANTO') retornar 0, significa que a cidade começa com "SANTO".

#desafio 25: ler o nome de uma pessoa e mostrar se ela tem "SILVA" no nome
nome = str(input('digite o nome de uma pessoa: ')).strip()
print('a pessoa tem silva no nome? {}'.format(nome.upper().find('SILVA') != -1))
#o uso do find('SILVA') != -1 é para verificar se a substring "SILVA" está presente em qualquer parte da string nome. O método find() retorna a posição da primeira ocorrência da substring, e se ela não estiver presente, ele retorna -1. Portanto, se find('SILVA') retornar um valor diferente de -1, significa que a pessoa tem "SILVA" no nome.

#deasafio 26: ler uma frase e mostrar quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez
frase = str(input('digite uma frase: ')).strip()
print('a letra "A" aparece {} vezes na frase'.format(frase.upper().count('A')))
print('a letra "A" aparece pela primeira vez na posição {}'.format(frase.upper().find('A') + 1))
print('a letra "A" aparece pela última vez na posição {}'.format(frase.upper().rfind('A') + 1))
#o uso do find('A') + 1 é para mostrar a posição da letra "A" na frase, considerando que a contagem de posições começa em 1. O método find() retorna a posição da primeira ocorrência da substring, e se ela não estiver presente, ele retorna -1. Portanto, se find('A') retornar um valor diferente de -1, significa que a letra "A" está presente na frase.
#o uso do rfind('A') + 1 é para mostrar a posição da última ocorrência da letra "A" na frase, considerando que a contagem de posições começa em 1. O método rfind() retorna a posição da última ocorrência da substring, e se ela não estiver presente, ele retorna -1. Portanto, se rfind('A') retornar um valor diferente de -1, significa que a letra "A" está presente na frase.

#desafio 27: ler o nome completo de uma pessoa e mostrar o primeiro e o último nome separadamente
nome = str(input('digite seu nome completo: ')).strip()
print('seu primeiro nome é {}'.format(nome.split()[0]))
print('seu último nome é {}'.format(nome.split()[-1]))
#o uso do split() é para dividir a string nome em uma lista de palavras, usando o espaço como separador. O índice [0] é usado para acessar o primeiro elemento da lista, que é o primeiro nome da pessoa. O índice [-1] é usado para acessar o último elemento da lista, que é o último nome da pessoa. Portanto, nome.split()[0] retorna o primeiro nome e nome.split()[-1] retorna o último nome.