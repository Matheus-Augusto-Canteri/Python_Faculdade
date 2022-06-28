nome = "Matheus Canteri"
print(nome)

#obtendo e imprimindo carectere por caractere
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])
print(nome[6], "\n")

#um pedaco
print(nome[4:], "\n")
print(nome[8:10], "\n")
print(nome[:8], "\n") # atras do 8
print(nome[-4:], "\n")
print(nome[:-4], "\n")
print(nome[:], "\n")

nome = "       Canteri          "

#Strip remove todos os espaços em brando do inicio e do fim da string, TEM QUE ARMAZENAR CARALHO
novoNome = nome.strip() 
print(novoNome) 

#Lstrip remove todos os espaços em branco à ESQUERDA da string, TEM QUE ARMAZENAR CARALHO
novoNome = nome.lstrip()
print(novoNome)

#Rstrip remove todos os espaços em branco à DIREITA da string, TEM QUE ARMAZENAR CARALHO
novoNome = nome.rstrip()
print(novoNome)

texto1 = "12345"

#isdecimal retorna true se uma string representa um valor decimal
retorno = texto1.isdecimal() #print(texto.isdecimal()) é valido
print(retorno)

flag = 0# 0 indica que não há numero, 1 cc
texto1 = "1e5t26y74u83o20kk21"
for letra in texto1:
    if letra.isdecimal():
        flag = 1

if flag == 1:
    print("Senha contém pelo menos um número")
else:
    print("Senha não contém pelo menos um número")


#isupper informa se a string é maiuscula ou não
texto1 = "MAIUSCULA"
texto2 = "minuscula"

retorno = texto1.isupper()
print(retorno)

retorno = texto2.isupper()
print(retorno)

#a funcao find reotnra -1 caso o texto procurado nao esteja na string e retorna a psoicao em que a string procurada se encontra caso esteja
texto = "Estrutura de dados"
encontrado = texto.find("Dados")
print(encontrado)

encontrado = texto.find("Banco")
print(encontrado)

# a funcao replace procura uma substring em uma string e, se a enctrona, suubstitui por um outro texto especificado
texto = "Estrutura de dados"

novoTexto = texto.replace("t", "C")
print(novoTexto)

# a funcao split quebra uma string em padecos menores com base em outra string, vira uma lista com os elementos, ou seja, posicao[0] é lasanha,
# posicao[2] = de, posicao[3] = berinjela etc
texto = "Lasanha de berinjela deveria ser ilegal"
textoDivido = texto.split(" ")

for item in textoDivido:
    print(item)

# vira uma lista com os elementos, ou seja, posicao[0] é lasanha,
# posicao[2] = de, posicao[3] = berinjela etc
disciplina = "Estrutura de dados"
lista = disciplina.split(" ")
print(lista)


texto3 = "/um texto qualquer"
texto4 = "um texto qualquer"

retorno = texto3.startswith("/")
print(retorno)
# a funcao startswith retorna true se uma string comeca com um texto especificado

retorno = texto4.startswith("/")
print(retorno)
#a funcao starswith retorna false se uma string não começa com um texto especificado

