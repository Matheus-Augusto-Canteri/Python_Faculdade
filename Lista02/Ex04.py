
listaNomes = ["João", "Maria", "José"]
listaNotas = [7.9, 5.6, 9.8]

tamanhoLista = listaNotas.__len__() - 1

while tamanhoLista >= 0:
    if listaNotas[tamanhoLista] >= 7:
        print(listaNomes[tamanhoLista], " está aprovado com nota ", listaNotas[tamanhoLista])
        tamanhoLista -= 1