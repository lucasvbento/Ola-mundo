alfabeto = 'abcdefghijklmnopqrstuvwxyz'
vogais = 'aeiou'


def consoante(letra):
    pos = alfabeto.index(letra)
    menor_distancia = float('inf')
    letra_menor = ''
    for v in vogais:
        distancia = abs(pos - alfabeto.index(v))
        if distancia < menor_distancia:
            letra_menor = v
            menor_distancia = distancia
        elif distancia == menor_distancia and alfabeto.index(v) < alfabeto.index(letra_menor):
            letra_menor = v
            menor_distancia = distancia
        if (pos + 1) < len(alfabeto):
            if alfabeto[pos + 1] in vogais:
                cons = alfabeto[pos + 2]
            else:
                cons = alfabeto[pos + 1]
        else:
            cons = 'z'
    codigo = letra + letra_menor + cons
    return codigo

    
p = str(input()).lower()
palavra = [p[i] for i in range(len(p))]
for i in range(len(p)):
    vogal = False
    for v in vogais:
        if p[i] == v:
            vogal = True
    if not vogal:
        palavra[i] = consoante(p[i])
print(''.join(palavra))
         