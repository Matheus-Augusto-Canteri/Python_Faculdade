#Escrevendo em um arquivo
arq = open('meuArquivoPython.txt', 'w', encoding = "UTF-8")
texto = """
Lista de compras:
-------------------
1 pacote de feijão
1 Kg de batata
2 litros de suco\n3 litross de chá gelado
"""

arq.write(texto) # Armazena
arq.close() # Fecha o arquivo que abriu

#\n = new line
#\t = tabulação (tab)