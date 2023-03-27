#Creacion de listas bidimensionales.
import random as rand

def matrices(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = rand.randint(1,10)
            matriz[i].append(num) #append agrega al final.
    return matriz

def escalar(matriz,n):
    for i in matriz:
        for j in range(len(i)):
            i[j] *= n  
    print(matriz)

def app():
    i =int(input('Ingrese el numero de filas: '))
    j = int(input('Ingrese el numero de columnas: '))
    matriz = matrices(i,j)
    print(matriz)
    n = int(input('Ingrese un numero para escalar la matriz: '))
    escalar(matriz,n)


if __name__ == '__main__':
    app()


