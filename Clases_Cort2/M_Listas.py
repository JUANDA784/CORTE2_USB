#la lista cuenta desde de 0.

#milista = []
#milista.append(7)
#milista.append(4)
#milista.append('hola')
#print(milista)

#EL while 1: es eterno

#milista = [3,5,7]
#
#opc = input('Ingrese un numero: ')
#idx = int(input('Ingrese un indice: '))
#milista.insert(idx,opc)
#print(milista)
#
milista = [3,5,7,5]
opc = ''
while opc != 'salir':
    opc = input('¿Que metdos desea utilizar?: ')
    if opc == 'borrar':
        dato = int(input('¿Cual dato quierer borrar?: '))
        milista.remove(dato)
    elif opc == 'buscar':
        dato = int(input('¿Cual dato quierer buscar?: '))
        pos = milista.index(dato) 
        print(f'El indice es {pos} ')
    elif opc == 'agregar':
        dato = int(input('¿Cual dato quierer agregar?: '))
        milista.append(dato)
        print(milista)
    elif opc == 'limpiar':
        milista.clear()
        print(milista)
    elif opc == 'insertar':
        dato = int(input('¿Cual dato quierer insertar?: '))
        idx = int(input('Ingrese un indice: '))
        milista.insert(idx,dato)
    elif opc == 'tamaño':
        print(len(milista))
    elif opc == 'sacar':
        idx = int(input('Ingrese un indice del numero a sacar: '))
        milista.pop(idx)
        print(milista)
    elif opc == 'comporar':
        print(f'El valor maximo es: {max(milista)} \nEl valor minimo es: {min(milista)}')
    elif opc == 'suma':
        print(f'La suma de la lista es: {sum(milista)}')
    elif opc == 'contar':
        dato = int(input('¿Cual dato quierer contar?: '))
        a = milista.count(dato)
        print(a)
    elif opc == 'comprobar':
        dato = int(input('¿Cual dato quierer comprobar?: '))
        b = dato in milista
        print(b)
    elif opc == 'extender':
        otralista = [1,2,3,4]
        milista.extend(otralista)
        print(milista)
    elif opc == 'ascender':
        milista.sort()
        print(milista)
    elif opc == 'decender':
        milista.reverse()
        print(milista)




#El 'remove' borra el primero que encuentra si hay dos numeros iguales.