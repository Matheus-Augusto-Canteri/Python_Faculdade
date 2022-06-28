""" Lista resultante """

def multiplicarLista(lista):
    i = 0
    for item in lista:
        lista[i] = lista[i] * i
        i += 1
    return lista

j = 0
listaInicial = []
while j < 10:
    """valor = int(input("Informe o valor: ")) Forma meme"""
    listaInicial.append(int(input("Informe o valor: "))) 
    j += 1

listaFinal = multiplicarLista(listaInicial)
print(listaFinal)