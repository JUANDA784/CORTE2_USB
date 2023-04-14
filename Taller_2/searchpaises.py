def busqueda_dicc(paises_dicc):
    while True:
        num = input("Ingrese el número del país (1-243): ")
        if num == "salir":
            break
        elif int(num) < 1 or int(num) > 243:
            print("Número inválido. Ingrese un número entre 1 y 243 o escriba 'salir' para salir.")
        else:
            pais = list(paises_dicc.keys())[int(num)-1]

            max_list = 0
            max_empresa = []

            min_list = 999999999
            min_empresa = []

            total_empleados = 0

            print(f"\nPaís: {pais}\n")
            for empresa in paises_dicc[pais]:
                total_empleados += int(empresa[8])

                if int(empresa[8]) > max_list:
                    max_list = int(empresa[8])
                    max_empresa = empresa

                if int(empresa[8]) < min_list:
                    min_list = int(empresa[8])
                    min_empresa = empresa

            print(f'Empresa con mayor # de empleados: ')
            print(f'- Empresa: {max_empresa[2]}')
            print(f'- Website: {max_empresa[3]}')
            print(f'- Descripcion: {max_empresa[5]}')
            print(f'- Fundacion: {max_empresa[6]}')
            print(f'- Industria: {max_empresa[7]}')
            print(f'- #Empleados: {max_empresa[8]}\n')

            print(f'Empresa con menor # de empleados: ')
            print(f'- Empresa: {min_empresa[2]}')
            print(f'- Website: {min_empresa[3]}')
            print(f'- Descripcion: {min_empresa[5]}')
            print(f'- Fundacion: {min_empresa[6]}')
            print(f'- Industria: {min_empresa[7]}')
            print(f'- #Empleados: {min_empresa[8]}\n')

            print(f'Promedio empleos: {round(total_empleados / len(paises_dicc[pais]),2)}')
            print(f'Cantidad de empresas: {len(paises_dicc[pais])}')