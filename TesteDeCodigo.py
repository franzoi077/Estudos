c = 'S'
l = []
while c == 'S':
    n = int(input('digite um valor: '))
    l.append(n)
    media = sum(l) / len(l)
    maior = max(l)
    menor = min(l)
    c = str(input('voce deseja continuar? [S/N]: ').upper())
print(f'a media é {media:.2f}, o maior é {maior} e o menor é {menor}')
