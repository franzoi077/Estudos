#desafio 77:
palavras = ('ola', 'hello', 'arthur', 'pedro',)
for d in palavras:
    a = d.count('a')
    e = d.count('e')
    i = d.count('i')
    o = d.count('o')
    u = d.count('u')
    print(f'a palavra {d} tem {a + e + i + o + u} vogais')