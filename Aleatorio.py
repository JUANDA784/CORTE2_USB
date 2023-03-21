import random as r

def Aleatorio():
    num = r.randint(100, 120)
    while num in [110, 115, 119]:
        num = r.randint(100, 120)
    return num

pares = []
impares = []

for i in range(10):
    if i % 2 == 0:
        num = Aleatorio()
        while num % 2 != 0:
            num = Aleatorio()
        pares.append(num)
    else:
        num = Aleatorio()
        while num % 2 == 0:
            num = Aleatorio()
        impares.append(num)

for i in range(5):
    print(pares[i])
    print(impares[i])


import math

print('1.Seno \n2.Coseno \n3.Tangente \n4.Exponecial \n5.Logaritmo natural')

num = float(input('Ingrese un nùmero en radianes: '))

while True:

    opc = int(input('Seleccione el nùmero (1 a 5) de la funcion que desee, y si quiere salir ponga 0: '))

    pi = 3.1415
    if opc == 0:
        break
    else:
        if opc == 1:
            print(f'El seno de {num} es = {(round((math.sin(num))*180 / pi))}°') 
        elif opc == 2:
            print(f'El coseno de {num} es = {(round((math.cos(num))*180 / pi))}°') 
        elif opc == 3:
            print(f'La tangente de {num} es = {(round((math.tan(num))*180 / pi))}°') 
        elif opc == 4:
            print(f'La exponencial de {num} es = {(round((math.exp(num))*180 / pi))}°') 
        elif opc == 5:
            print(f'El logaritmo natural de {num} es = {(round((math.log(num))*180 / pi))}°') 
