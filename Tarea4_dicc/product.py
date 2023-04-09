import searchproduct

def main():
    dicc = {}
    f = open('Alimentos.txt','rt')
    matriz = f.readlines()
    f.seek(0)
    for linea in matriz:
        valores = linea.rstrip('\n').split(',')
        if len(valores) < 3:
            continue
        clave = valores[1]
        dicc[clave] = valores

    for clave in dicc:
        print(f'{clave}', end= ' - ')

    f.close()

    searchproduct.busqueda_dicc(dicc, valores)

if __name__=="__main__":
    main()