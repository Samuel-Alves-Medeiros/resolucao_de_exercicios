from cofre_real import tamanho

sinais_da_floresta:list[str] = [
    ["M12", "Y08", "C16", "|"],
    ["B15","BOO", "L25", "|"],
    ["T20", "P19", "K15", "|"],
    ["G18", "R22", "S10", "W14"],

]


rotas = {
    0: [],
    2: [],
    3: []
}

nums = "0123456789"
for i in range(tamanho(sinais_da_floresta)):
    if "BOO" in sinais_da_floresta[i]:
        continue
    for j in sinais_da_floresta[i]:
        num_local = ""
        for k in j:
            if k in nums:
                num_local+= k
        rotas[i].append(num_local)


rota1 = rotas[0]
rota3 = rotas[2]
rota4 = rotas[3]

contador1:int = 0
acumulador1:int = 0

for i in range(tamanho(rota1)-1):
    acumulador1 += int(rota1[i])
    contador1+=1

acumulador3 = 0
contador3 = 0

for i in range(tamanho(rota3)-1):
    acumulador3 += int(rota3[i])
    contador3 += 1

media_rota3 = acumulador3/ contador3

acumulador4 = 0
contador4 = 0

for i in range(tamanho(rota4)):
    acumulador4 += int(rota4[i])
    contador4 += 1

media_rota4 = acumulador4/contador4
media_rota1  = acumulador1/contador1

def melhor_trilha_sinais():
    if media_rota1 > media_rota3 and media_rota1 > media_rota4:
        return "trilha1", media_rota1
    elif media_rota3 > media_rota1 and media_rota3 > media_rota4:
        return "trilha 3", media_rota3
    return "trilha 4", media_rota4

print(melhor_trilha_sinais())