def definirPalindroma(palavra):
    tamanho = palavra.__len__() - 1
    i =  tamanho // 2
    palindroma = True
    aux = 0 

    while i > 0:
        if palavra[aux] != palavra[tamanho]:
            palindroma = False
        aux += 1
        tamanho -= 1
        i -= 1

    return palindroma

palavraInicial = "Osso"
palavraInicial = palavraInicial.lower()

print(definirPalindroma(palavraInicial)) 
