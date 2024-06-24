from pprint import pprint

def verificar_biblioteca(amigo):
    return amigo in hast_amigos


def criar_amigo(amigo):
    global hast_amigos
    hast_amigos[amigo] = [0, 0, 0]



#funcao para o tempo passar com padrão de t=1 pois quando envia ou recebe msg esse é o tempo que passa
def tempo_passar(t=1):
    global hast_amigos
    if len(hast_amigos) > 0:
        for k, v in hast_amigos.items():
            if v[0] != v[1]:
                v[2] += t
    
tempo = False
n = int(input())
hast_amigos = {}
for i in range(n):
    informacao = str(input()).split()
    x = int(informacao[1])
    tipo = informacao[0]
    if tipo in 'R':
        if not verificar_biblioteca(x):
            criar_amigo(x)
        hast_amigos[x][0] += 1
        if not tempo:
            tempo_passar()
        tempo = False
    elif tipo in 'E':
        if verificar_biblioteca(x) and hast_amigos[x][0] > hast_amigos[x][1]:
            hast_amigos[x][1] += 1
            if not tempo:
                tempo_passar()
            tempo = False
    elif informacao[0] in 'T':
        t = x
        tempo_passar(t=t)
        tempo = True

for k, v in hast_amigos.items():
    if v[0] != v[1]:
        v[2] = -1
    print(f'{k} {v[2]}')
pprint(hast_amigos)