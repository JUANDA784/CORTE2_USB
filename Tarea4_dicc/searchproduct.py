def busqueda_dicc(dicc, valores):
    product = ''
    while product != 'salir':
        product = input('\nIngrese el producto que desea calcular: ')
        precio = int(input('Ingrese el precio del producto: '))
        
        if product == 'salir':
            break 
        elif product in dicc:
            valores = dicc[product] 
            print(f'{valores[0]} - {valores[1]} - {valores[2]}')
            valor_neto = round(precio / (1 + float(valores[2])),2)
            iva = round((valor_neto * float(valores[2])),2) 
            print(f'IVA = {iva}')
            print(f'El valor neto o precio sin IVA del producto es = {valor_neto} $ pesos colombianos')
        else:
            print('No se encuentra el producto')