salas_fantasmas:dict[int] = {
    "norte" : [20, -5, 35, 10],
    "sul" : [15,40,10,25],
    "leste": [50,10,15],
    "oeste": [30,-5,60,5]
}

salas_limpas = {}

for k,v in salas_fantasmas.items():
    soma_salas:int = 0
    for i in v:
        if -5 in v:
            break
        if i >= 15:
            soma_salas+=i
    if soma_salas != 0:
        salas_limpas[k] = soma_salas

maior_valor = {"ala": "", "moedas": 0}

for k,v in salas_limpas.items():
    if v > maior_valor["moedas"]:
        maior_valor["moedas"] = v
        maior_valor["ala"] = k

print(maior_valor)