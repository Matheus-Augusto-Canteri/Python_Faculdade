arq = open('teste1.txt', 'r')
texto = arq.readlines()
tam = texto.__len__()
print(tam)

valorTotal = 0
vagas = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4] # 4 = Vazio, a primeira hora vai ser vazio
valorPorVaga = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = nulo, ou seja, não arrecadou nada

