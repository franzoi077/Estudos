#fatiando um string
frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:21:2])
#o uso do [9:13] é para pegar os caracteres da posição 9 até a posição 12, ou seja, o caractere da posição 13 não é incluído. O primeiro caractere da string tem a posição 0, então o caractere da posição 9 é o décimo caractere da string.
print(frase[:5])

#Analizando uma string
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformando uma string
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

#dividindo uma string
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
print(frase.split()[0])

#juntando uma string
print('-'.join(frase))