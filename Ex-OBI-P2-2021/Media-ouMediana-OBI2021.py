a, b = map(int, input().split())
if a > b:
    dif = a - b
    menor = b
else:
    dif = b - a
    menor = a
c = menor - dif
print(c)