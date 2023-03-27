#def imprimir(x):
#    if x>0:
#        imprimir(x-1)
#        print(x)
#    else:
#        print(f'finalizo {x}')
#
#imprimir(5)

#Recursivo impar.

def impar(x):
    if x <= 0:
        return 0
    else:
        num = (2*x-1) + impar(x-1)#La suma de los impares
        return num

if __name__=='__main__':
     valor = impar(3)
     print(valor)