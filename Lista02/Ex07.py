login = "Login456"
senha = "Login123"

erro = False

if login.__len__() <= 7 or login.__len__() >= 10:
    print("Login possui 7 caracteres ou menos ou 10 caracteres ou mais")
    erro = True

if senha.__len__() <= 7 or senha.__len__() >= 10:
    print("Senha possui 7 caracteres ou menos ou 10 caracteres ou mais")
    erro = True

if senha.find(login) >= 0:
    print("Senha não pode conter o login")
    erro = True

if login.islower():
    print("O login deve conter pelo menos uma letra maiuscula")
    erro = True

if not erro:
    print("Não tem erro")