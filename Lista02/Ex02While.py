"""Vai começar lendo sempre o parenteses interno"""
"""Saber quantos valores tem dentro da lista usando o print(lista.__len__())"""
lista = []
for i in range(0, 7):
    lista.append(int(input("Informe o valor: \n")))

# Retorna a quantidade de elementos contidos na lista
tamanhoLista = lista.__len__()

# Procurando valores pares
i = 0
print("Valores pares:\n")
while i < tamanhoLista:
    if lista[i] % 2 == 0:
        print(lista[i], " na posição ", i)
        print("\n")
        i += 1

# Procurando valores impares
i = 0
print("Valores pares:\n")
while i < tamanhoLista:
    if lista[i] % 2 != 0:
        print(lista[i], " na posição ", i)
        print("\n")
        i += 1