#quantos numeros são falados
n = int(input())
numeros = []
#adicionando os números na lista e retirando quando for dito zero
for i in range(n):
    s = int(input())
    if s == 0:
        numeros.pop()
    else:
        numeros.append(s)
#somando valores da lista
soma = 0
for i in numeros:
    soma += i
print(soma)