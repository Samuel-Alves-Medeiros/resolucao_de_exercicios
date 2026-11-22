runas_mural:list[str] = [
    "osso", "koopa", "radar", "castelo", "salas"
]
pergaminhos_cifrados:list[str] = [
    "wstetsw", "fsawiv", "vizmziv", "quevms", "qmvmq", "tiegl"
]

def tamanho(text:str) ->int:
    contador:int = 0
    for i in text:
        contador+=1
    return contador

def reverse(text) ->str:
    text_invertido:str = ""
    contador_negativo:int = -1
    for i in range(tamanho(text)):
        text_invertido+= text[contador_negativo]
        contador_negativo-=1 
    return text_invertido

def eh_palindromo(r_m:list[str]) -> int:
    contador_palind:int = 0
    for i in range(tamanho(r_m)):
        if r_m[i] == reverse(r_m[i]):
            contador_palind+=1
    return contador_palind

def decifrar(cifra:str, key:int) -> str:
    alfabeto:str = "abcdefghijklmnopqrstuvwxyz"
    txt_decrypted:str = ""
    deslocamento = key +1

    for i in range(tamanho(cifra)):
        for j in range(tamanho(alfabeto)):
            if cifra[i] == alfabeto[j]:
                txt_decrypted += alfabeto[(j - deslocamento) % 26] 

    return txt_decrypted


lista_palindromos:list[str] = []
for i in pergaminhos_cifrados:
    txt_decrypted:str = decifrar(i, eh_palindromo(runas_mural))
    if txt_decrypted == reverse(decifrar(i, eh_palindromo(runas_mural))):
        lista_palindromos.append(txt_decrypted)

if __name__ == "__main__":

    print("-".join(lista_palindromos))
    