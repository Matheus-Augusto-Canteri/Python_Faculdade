# Isso é um comentário 

'''
Comentário de múltiplas linhas

variavel = 10 # Variável dinâmica, pode ser int aqui e na linha de baixo string 
variavel = "Texto"
resultado = variavel * 18
print(resultado)

# Int = valores inteiros
# Float = valores decimais
# Str = valores de texto

valor = 10
texto = "estrutura de dados"
float = 10.89
print("Olá")

from unittest import result


nome = "Matheus"
idade = 19

print("Olá " + nome + ", sua idade é: " + str(idade) + " anos")
 
nome = input("Informe seu nome: ")
print(nome)

idade = int(input("Informe sua idade: ")) # Todo valor lido pelo usuário é String
valor = idade + 10
print(valor)

idade = int(input("Informe sua idade: ")) # Todo valor lido pelo usuário é String
if idade < 18: # Utiliza esse tipo de identação
    print("Você não possui maioridade penal! ")
else:
    print("Você possui maioridade penal! ")
    # Outros comandos
    # Mais comandos ainda

conceito = float(input("Informe sua nota: "))
if conceito >= 8:
    print("Aprovado! ")
elif conceito >= 6 and  conceito <= 7.9:
    print("Em recuperação! ")
else:
    print("Reprovado! ")


i = 0
while i < 10:
    print(str(i) + "\t")
    i += 1 # i += 1 é igual a i++;


for i in range (0, 10, 1): # Range = faixa, de tanto até tanto e de quanto ele vai se auto incrementar
    print(str(i)+" ")

    def somarValores(v1, v2, v3):
        resultado = v1 + v2 + v3
        return resultado

print("Olá mundo!")
result = somarValores(3,4,6)
print(result)'''

#criando uma lista vazia
minhaLista[]
#criando uma lista com elementos
minhaOutraLista = [1,7,38,99]

#acessando um elemento da lista
print(minhaOutraLista[3]) #99
resultado = minhaOutraLista[0] + minhaOutraLista[2]
print(resultado) #39

#inserindo novos valores
novoValor = input("Insira um novo valor: ")
minhaOutraLista.append(int(novoValor))
minhaOutraLista.append(40)
#exibindo todo o conteúdo da lista
print(minhaOutraLista)

#removendo um elemento especifico
minhaOutraLista.remove(7)
print(minhaOutraLista)
#removendo um elemento em um índice específico
minhaOutraLista.__delitem__(2)
print(minhaOutraLista)

#Percorrendo uma lista - 1 Forma
minhaLista = ["João", "José", "Maria", "Ana"]
for item in minhaLista:
    print(item)

#Percorendo uma lista - 2 forma
minhaLista = ["João", "José", "Maria", "Ana"]
i = 0
while(i < 4):
    print(minhaLista[i])
    i += 1