frase = "Esse é um exercício de estrutura de dados"

listaPalavras = frase.split(" ")

frase = frase.replace(".", " ")

print(frase)
print(listaPalavras)
print(listaPalavras.__len__()) #Mostra quantos elementos tem na lista

