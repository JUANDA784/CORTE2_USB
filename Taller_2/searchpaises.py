def busqueda_dicc(paises_dicc):
    while True:
        num = input("Ingrese el número del país (1-243): ")
        if num == "exit":
            break
        elif not num.isnumeric() or int(num) < 1 or int(num) > 243:
            print("Número inválido. Ingrese un número entre 1 y 243 o escriba 'exit' para salir.")
        else:
            pais = list(paises_dicc.keys())[int(num)-1]
            print(f"Información del país {num}: {pais}")
            for info in paises_dicc[pais]:
                print(info)