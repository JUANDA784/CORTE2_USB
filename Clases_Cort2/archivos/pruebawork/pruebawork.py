import busquedawork

def main():
    dicc = {}
    f = open('matriz.txt','rt')
    matriz = f.readlines()
    f.seek(0)
    for i in range(len(matriz)):
        valor=f.readline().rstrip('\n').split(',')
        for j in range(len(valor)):
            pos = str(f'{i}{j}')
            dicc[pos] = valor[j]

    print(dicc) 
    f.close()

    busquedawork.busqueda_dicc(dicc)
     
    

if __name__=="__main__":
    main()