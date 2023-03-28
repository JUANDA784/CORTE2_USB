#def main():
#    f = open('matrizAsignacion.txt','rt')
#    matriz = f.read()
#    print(matriz)
#
#if __name__=='__main__':
#    main()
#
#def main():
#    f = open('matrizAsignacion.txt','rt')
#    matriz = f.readlines()
#    f.seek(0)
#
#    for i in range(len(matriz)):
#        print(f.readline().rstrip('\n').split(','))
#
#if __name__=='__main__':
#    main()

#def main():
#    f = open('matrizAsignacion.txt','rt')
#    matriz = f.readlines()
#    f.seek(0)
#
#    suma = 0
#    for i in range(len(matriz)):
#        valor = f.readline().rstrip('\n').split(',')#Split lo vuelve una lista. Y rstrip quite o omite
#        print(valor)
#        suma += int(valor[0])
#        print(suma)
#    print(suma)
#    f.close
#
#
#if __name__=='__main__':
#    main()
#
#def main():
#    dicc = {}
#    f = open('matrizAsignacion.txt','rt')
#    matriz = f.readlines()
#    f.seek(0)
#
#    suma = 0
#    for i in range(len(matriz)):
#        valor = f.readline().rstrip('\n').split(',')#Split lo vuelve una lista. Y rstrip quite o omite
#        for j in range(len(valor)):
#            pos = str(f'{i}{j}')
#            dicc[pos] = valor[j]
#
#    print(dicc)
#    print(f'la posicion 4,3 es: {dicc["43"]}')
#
#if __name__=='__main__':
#    main()

import busqueda
def main():
    dicc = {}
    f = open('matrizAsignacion.txt','rt')
    matriz = f.readlines()
    f.seek(0)

    suma = 0
    for i in range(len(matriz)):
        valor = f.readline().rstrip('\n').split(',')#Split lo vuelve una lista. Y rstrip quite o omite
        for j in range(len(valor)):
            pos = str(f'{i}{j}')
            dicc[pos] = valor[j]

    print(dicc)
    f.close()
    busqueda.busq(dicc)

if __name__=='__main__':
    main()