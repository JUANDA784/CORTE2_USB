import search

def main():

    paises_dicc = {}
    f = open('organization_data.csv','r')
    matriz = f.readlines()
    matriz.pop(0)
    
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            if matriz[i].split(',')[4] > matriz[j].split(',')[4]:
                matriz[i], matriz[j] = matriz[j], matriz[i]

    num_pais = 1
    for linea in matriz:
        columna = linea.strip().split(',')
        pais = columna[4]
        if pais not in paises_dicc:
            paises_dicc[pais] = []
        paises_dicc[pais].append(columna)
        num_pais += 1

    for line in matriz[1:]:
           campos = line.strip().split(',')
           num = campos[0]
           pais = campos[1]
           paises_dicc[num] = campos[1:]

    print(matriz) 
    print(paises_dicc)


    search.busqueda_dicc(paises_dicc)

if __name__=="__main__":
    main()