from cofre_real import tamanho

sinais_da_floresta:list[str] = [
    "M12", "Y08", "C16", "|",
    "B15","BOO", "L25", "|",
    "T20", "P19", "K15", "|",
    "G18", "R22", "S10", "W14",
]

def split(txt:str, key:str) ->list[str]:
    matriz:list[list[str]] = []
    splited_text:list[str] = []
    for char in txt:
        if char == key:
            matriz.append(splited_text)
            splited_text = []
        else:
            splited_text.append(char)
    matriz.append(splited_text)

    return matriz

matriz_sinais:list[list[str]] = split(sinais_da_floresta, "|")

rotas_seguras:list[list[int]] = []
digitos:str = "0123456789"

for i in range(tamanho(matriz_sinais)):
    lista_digitos:list[int] = []
    str_num:str = ""
    if "BOO" not in matriz_sinais[i]:
        for j in matriz_sinais[i]:
            for c in j:
                if c in digitos:
                    str_num += c
            lista_digitos.append(int(str_num))
            str_num = ""
        rotas_seguras.append(lista_digitos)

def num_rotas_seguras():
    rotas_seguras:list[int] = []
    for i in range(tamanho(matriz_sinais)):
        if "BOO" not in matriz_sinais[i]:
            rotas_seguras.append(i)
    return rotas_seguras

num_rotas = num_rotas_seguras()

def melhor_trilha(sinais:list[list[int]]):
    media_rotas= {}

    for i in range(tamanho(sinais)):
        soma_sinais:int = 0
        for j in sinais[i]:
            soma_sinais +=j
        media_rotas[num_rotas[i]] = soma_sinais/tamanho(sinais[i])
        soma_sinais = 0

    return media_rotas


melhor_rota:dict = {}
maior:int = 0 

for k,v in melhor_trilha(rotas_seguras).items():
    if v > maior:
        melhor_rota = {}
        maior = v
        melhor_rota[k] = v

for k,v in melhor_rota.items():
    print(f"A rota {k} é a melhor! Sua média é de {v}")