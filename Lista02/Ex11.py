arq = open('Operações.txt', 'r')
texto = arq.readlines()

for linha in texto:
    linha = linha.split(" ")

    if linha[0] == "1":
        result = int(linha[1]) + int(linha[2])
        print(result)
    elif linha[0] == "2":
        result = int(linha[1]) / int(linha[2])
        print(result)
    elif linha[0] == "3":
        result = int(linha[1]) ** int(linha[2])
        print(result)
    elif linha[0] == "4":
        result = int(linha[1]) - int(linha[2])
        print(result)    
