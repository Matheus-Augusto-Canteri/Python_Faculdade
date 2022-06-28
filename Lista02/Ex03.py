
def analisarCrescente(lista):
    tamanho = lista.__len__() - 1
    flag = 0 # 0 se lista é crescente, 1 caso contrario
    while tamanho > 0:
        if lista[tamanho] <= lista[tamanho - 1]:
            flag  = 1
        tamanho -= 1
    if flag == 0:
        print("A lista é crescente!")
    else:
        print("A lista NÃO é crescente!")
lista = [10, 20, 30, 40, 50]
analisarCrescente(lista)
