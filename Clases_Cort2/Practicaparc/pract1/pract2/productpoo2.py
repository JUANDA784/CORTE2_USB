class Producto():
    def __init__(self, code, name, iva) -> None:
        self.__code = code
        self.__name = name
        self.__iva = iva

    def get_name(self):
        return self.__name

    def get_iva(self):
        return self.__iva

class Archivo():
    def __init__(self):

        self.__leer = None
        self.__product = None
        self.__precio = None
        self.__productos = []
        self.__valor_neto = 0

    #--------------------------- getters -----------------------------

    def getLeer(self):
        return self.__leer
    def getProducto(self):
        return self.__producto
    def getPrecio(self):
        return self.__precio
    
    #---------------------------- setters -----------------------------    
    
    def setLeer(self):
        self.__leer = open('Alimentos.txt','r')# leer = self.__leer 
        data = self.__leer.readlines()
        data.pop(0)
        self.__leer.seek(0)

        for linea in data:
            product_list = linea.strip('\n').split(',')

            product = Producto( product_list[0], product_list[1], product_list[2] )

            self.__productos.append(product)

    def setProducto(self):
        name = input('Ingrese el producto que desea calcular o dale (exit): ')

        if name != 'exit':
            for producto in self.__productos:

                if name == producto.get_name():
                    self.__product = producto
                    return

    def setPrecio(self):
        self.__precio = int(input('Ingrese el precio del producto: '))

    #--------------------------- metodos ---------------------------------------
    def leerArchivo(self):
        list_product = []
       
        return list_product
    
    def __valorNeto(self):
        self.__valor_neto = round(self.__precio / ( 1 + float(self.__product.get_iva() ) ), 2)
        return self.__valor_neto
        
    def getNeto(self):
        return self.__valorNeto()


    def __ivaProduct(self):
        iva = round((self.__valor_neto * float(self.__product.get_iva())),2)
        return iva

    def getivaDelProducto(self):
        return self.__ivaProduct()

def main():
    iva = Archivo()
    iva.setLeer()
    iva.getLeer()
    iva.setProducto()
    iva.setPrecio()
    iva.leerArchivo()
    iva.getNeto()

    print(f'IVA = {iva.getivaDelProducto()}\n'+ \
          f'El valor neto o precio sin IVA del producto es = {iva.getNeto()}')


if __name__=='__main__': 
    main()