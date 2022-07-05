arq = open('meuArquivoPython.txt', 'r', encoding="UTF-8")
texto = arq.readlines()
for linha in texto:
    print(linha, end = '')
arq.close()