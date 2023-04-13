def busqueda_dicc(paises_dicc):
    while True:
        num = input("Ingrese el número del país (1-243): ")
        if num == "exit":
            break

        num_int = int(num)
        if 1 <= num_int <= 243:
            pais = paises_dicc[num_int]
            print(f"Información del país {num}: {pais}")
            for info in paises_dicc[pais]:
                print(info)
        else:
            print("Número inválido. Ingrese un número entre 1 y 243 o escriba 'exit' para salir.")