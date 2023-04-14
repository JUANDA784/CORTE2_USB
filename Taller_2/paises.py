import searchpaises

def main():
    f = open('organization_data.csv','r')
    matriz = f.readlines()
    matriz.pop(0)

    def country(line):
        columna = line.split(',')
        return columna[4]
    matriz.sort(key=country)

    paises_dicc = {}
    num_pais = 1
    for linea in matriz:
        columna = linea.strip().split(',')
        pais = columna[4]
        if pais not in paises_dicc:
            paises_dicc[pais] = []
        paises_dicc[pais].append(columna)
        num_pais += 1

    searchpaises.busqueda_dicc(paises_dicc)

if __name__=="__main__":
    main()