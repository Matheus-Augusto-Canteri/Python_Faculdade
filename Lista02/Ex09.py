import random
num = 0
aux = 0
comp = False
while not comp:
    aleatorio = str(random.randint(100,1000000))
    if aleatorio.find("12345") != -1:
        num = aleatorio
        comp = True
    aux += 1

print(num, "-", aux)