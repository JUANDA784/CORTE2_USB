#Punto 1: Ordenamiento de una matriz aleatoria.
import random as r
   
matriz = []
for i in range(5):
    fila = []
    for j in range(10):
        columna = r.randint(0,50)
        fila.append(columna)

    matriz.append(fila)

print(matriz)

maximo = matriz[0][0]
minimo = matriz[0][0]
posmax = (0, 0)
posmin = (0, 0)

for fila in range(len(matriz)):
    for columna in range(len(matriz[0])):
        if matriz[fila][columna] > maximo:
            maximo = matriz[fila][columna]
            posmax = (fila, columna)
        if matriz[fila][columna] < minimo:
            minimo = matriz[fila][columna]
            posmin = (fila, columna)

print(f"El valor máximo es {maximo} en la posición {posmax}")
print(f"El valor mínimo es {minimo} en la posición {posmin}")

lista = []
for fila in matriz:
    lista.extend(fila)

lista.sort(reverse=True)

orden = []
i = 0
for fila in matriz:
    fila2 = []
    for j in range(len(fila)):
        fila2.append(lista[i])
        i += 1
    orden.append(fila2)

print("Matriz ordenada:")
for fila in orden:
    print(fila)


##Punto 2: Funcion recursiva de una funcion.
def k(n, p):
    if n <= 0:
        return 0
    else:
        func = k(n-1, p) + n * p
        return func  

if __name__=='__main__':
     result = k(5, 3)
     print(f'El resultado del factorial que escogiste es: {result}')

#Punto 3: Funcion recursiva de fibonacci.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo = fibonacci(n-1) + fibonacci(n-2)
        return fibo
if __name__=='__main__':
     resultado = fibonacci(10)
     print(f'El número de fibonacci que es escogiste es: {resultado}')
