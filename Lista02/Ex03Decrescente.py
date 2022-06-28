def analisarCrescente(lista):
    tamanho =  lista._len_() - 1
    flag = 0
    while tamanho > 0:
        if lista [tamanho] <= lista[tamanho-1]:
            flag = 1
        tamanho -= 1

    if flag == 0:
        print("Lista crescente")
    else:
        analisarDecrescente(lista)

def analisarDecrescente(lista):
    tamanho =  lista._len_() - 1
    flag = 0
    while tamanho > 0:
        if lista [tamanho] >= lista[tamanho-1]:
            flag = 1
        tamanho -= 1
    if flag == 0:
        print("Lista decrescente")
    else:
        print("Lista não é crescente e nem decrescente")

lista = [4, 3, 5, 1]

analisarCrescente(lista)