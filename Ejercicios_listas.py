#Consultar su horario de clases con listas.

materias = ['calculo', 'fisica', 'circuitos', 'programacion', 'dibujo']
dia = ['martes', 'viernes', 'miércoles', 'jueves', 'lunes']
hora = ['7:00 a.m', '3:00 p.m', '11:00 p.m', '1:00 p.m', '9:00 a.m' ]
salon = ['406 DB', '407 DB', '306 DB', '304 GO', '302 DS']
profesor = ['Jairo', 'Andrea', 'Roberto', 'David', 'Gabriel']

print(materias)

num = input('Ingrese el nombre de la materia: ')

indice = materias.index(num)

print(f'Día: {dia[indice]}')
print(f'Hora: {hora[indice]}')
print(f'Salon: {salon[indice]}')
print(f'Profesor@: {profesor[indice]}')

#Programa que saque el numero mayor de una lista aleatoria y los primos de esa misma lista.

import  random as r

aleatorios = []

for i in range(10):
    aleat = r.randint (1,50)
    aleatorios.append(aleat)

print(aleatorios)

def mayor():
    aleatorios.sort()
    print(f'El numero mayor de esta lista es: {aleatorios[9]}')

mayor()

primos = []

def  prim ():
    for i in aleatorios:
        cont = 2
        primo = True

        if i == 1:
            primo = False

        while primo and cont < i :
            if i % cont == 0 :
                primo = False
            else:
                cont += 1

        if primo:
            primos.append(i)
    
    print(f'Los numeros primos de esta lista son: {primos}')

prim()