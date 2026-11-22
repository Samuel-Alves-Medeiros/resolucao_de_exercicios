from ex001 import tamanho
mapa_blocos:list[list[int]] = [
    [15,5,20,-1,50],
    [30,10,8],
    [5,-1,40,25],
    [20,15,10]
]

soma_moedas:int = 0

for i in range(tamanho(mapa_blocos)):
    for j in mapa_blocos[i]:
        if j == -1:
            break

        if j >= 10:
            soma_moedas += j

print(soma_moedas)