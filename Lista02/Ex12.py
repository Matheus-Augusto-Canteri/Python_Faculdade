arq = open('MarlonDeus.txt', 'r')
texto = arq.readlines()
aux = 0

for linha in texto:
    while aux <= 9:
        if not linha.startswith(str(aux)):
            print(linha)