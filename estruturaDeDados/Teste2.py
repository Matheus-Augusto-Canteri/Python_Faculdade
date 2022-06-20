def definirPar(valor):
    if valor % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
    def definirPositivo(valor):
        if valor > 0:
            return "Positivo"
        else:
            return "Negativo"

resultado = definirPar(int(input("Informe o valor: ")))
print(resultado)
resultad = definirPositivo(int(input("Informe o valor novamente: ")))
print(resultado)