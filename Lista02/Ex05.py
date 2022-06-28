# Retorna posição do valor se o encontra, -1 cc
def buscarValor(valores, chave):
    tamanhoLista = valores.__len__() - 1
    while tamanhoLista >= 0:
        if valores[tamanhoLista] == chave:
            return tamanhoLista
        tamanhoLista -= 1
    return -1
        
    # for item in valores:
    #     # if item == chave:
        #     return True
        # else:
        #     return False


valores = [10, 89, 87, 1888, 19]
chave = int(input("Informe o valor a ser encontrado:\n"))
retorno = buscarValor(valores, chave)
if retorno != -1:
    print("Valor encontrado na posição: " ,retorno)
else:
    print("O valor não foi encontrado!")
