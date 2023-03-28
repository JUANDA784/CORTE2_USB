
def busq(dicc):
    n = ''
    while n != 'salir':
        n = input('Ingrese un key de busqueda: ')

        if n == 'salir':
            break
        if n not in dicc:#Para ver si no esta ese numero. 'In' para saber si esta.
            print('Error, fuera de rango')
        else:
            print(dicc[n])