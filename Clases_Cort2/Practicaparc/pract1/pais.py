#def lectura():
#    n = open('organizations-100.csv','rt')
#    data = []
#    linea = n.readline()
#    while linea != '':
#        data.append(linea.rstrip('\n').split(','))
#        linea = n.readline()
#    n.close()
#    return data
# ó 
def leer():
    f = open('organization_data.csv')
    matriz = f.readlines()
    matriz.pop(0)
    f.seek(0)

    valores = []

    for linea in matriz:
        valores.append(linea.strip('\n').split(','))

    f.close()

    return valores

def organization_paises(valores):
    paises = []

    for i in valores:
        pais = i[4]
        
        if pais not in paises:
            paises.append(pais)
    
    paises.sort()

    return paises

def searchpais(paises, valores):
    compañias = []
    empleados = []

   
    indice = input('Indice del país de busqueda o (salir): ')
    
    for lista in valores:
        if lista[4] == paises[int(indice)-1]:
            compañias.append(lista)
            empleados.append(int(lista[8]))
    
    return compañias, empleados

def imprimir(compañias, empleados):
    print(f'\nPaís: {compañias[0][4]}\n')

    mayor = empleados.index(max(empleados))
    menor = empleados.index(min(empleados))

    print('#Empresa con mayor número de empleados:\n ')
    rotulo = ['- Empresa: ','- Website: ','- Descripción: ','- fundación: ', '- Industria: ','- #Empleados: ']

    line1 = compañias[mayor]
    line1.pop(4)
    line1.pop(1)
    line1.pop(0)

    for i in range (len(rotulo)):
        print(f'{rotulo[i]} {line1[i]}')

    line2 = compañias[menor]
    line2.pop(4)
    line2.pop(1)
    line2.pop(0)

    print('\n#Empresa con menor número de empleados: ')
    for i in range (len(rotulo)):
        print(f'{rotulo[i]} {line2[i]}')

    print(f'Promedio de empleados: {round(sum(empleados)/len(empleados),2)}')
    print(f'Cantidad de empleos: {len(empleados)}')

def main():
    valores = leer()
    paises =  organization_paises(valores)
    compañias_matriz,empleados_matriz = searchpais(paises, valores)
    imprimir(compañias_matriz,empleados_matriz)

if __name__=='__main__':
    main()

