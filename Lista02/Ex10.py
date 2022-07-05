arq = open('OnePiece.txt', 'r')
texto = arq.readlines()
print(texto.__len__())

i = int(input("Informe qual linha você deseja ler: "))

print(texto[i - 1])