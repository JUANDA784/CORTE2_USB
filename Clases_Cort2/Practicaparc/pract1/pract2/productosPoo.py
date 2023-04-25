class Archivo():
    def __init__(self):

        self.__leer = None
        self.__producto = None
        self.__precio = None
        self.__productos = []
        self.__producto_list = []
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

        valores = [] 

        for linea in data:
            valores.append(linea.strip('\n').split(','))

        self.__productos = valores

    def setProducto(self):
        self.__producto = input('Ingrese el producto que desea calcular o dale (exit): ')

        if self.__producto != 'exit':
            for producto in self.__productos:
                if self.__producto == producto[1]:
                    self.__producto_list = producto
                    return

    def setPrecio(self):
        self.__precio = int(input('Ingrese el precio del producto: '))

    #--------------------------- metodos ---------------------------------------
    def __valorNeto(self):
        self.__valor_neto = round(self.__precio / (1 + float(self.__producto_list[2])), 2)
        return self.__valor_neto
        
    def getNeto(self):
        return self.__valorNeto()


    def __ivaProduct(self):
        iva = round((self.__valor_neto * float(self.__producto_list[2])),2)
        return iva

    def getivaDelProducto(self):
        return self.__ivaProduct()

def main():
    iva = Archivo()
    iva.setLeer()
    iva.getLeer()
    iva.setProducto()
    iva.setPrecio()
    iva.getNeto()

    print(f'IVA = {iva.getivaDelProducto()}\n'+ \
          f'El valor neto o precio sin IVA del producto es = {iva.getNeto()}')


if __name__=='__main__': 
    main()