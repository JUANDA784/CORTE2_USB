#2:32
class Archivo():
    def __init__(self):

        self.__leer = None
        self.__producto = None
        self.__precio = None

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

    def setProducto(self, valores):
        self.__producto = input('Ingrese el producto que desea calcular o dale (exit): ')

        if self.__producto != 'exit':

            list_product = []

            for i in valores:
                if len(i) < 2:
                    continue
                if self.__producto == i[1]:
                    list_product.append(i)

        print(list_product)

    def setPrecio(self):
        self.__precio = int(input('Ingrese el precio del producto: '))

#--------------------------- metodos ---------------------------------------
    def leerArchivo(self):
        list_product = []
       
        return list_product
    
    def __valorNeto(self, list_product):
        valor_neto = 0
        if len(list_product) >= 3:
            valor_neto = round(self.__precio / (1 + float(list_product[2])), 2)
        else:
            print("La lista de productos no tiene suficientes elementos")
        return valor_neto
        
    def getNeto(self, list_product):
        return self.__valorNeto(list_product)


    def __ivaProduct(self, valor_neto, list_product):
        if len(list_product) >= 3:
            iva = round((valor_neto * float(list_product[2])),2)
            return iva
        else:
            print("La lista de productos no tiene suficientes elementos")
    
    def getivaDelProducto(self, valor_neto, list_product):
        return self.__ivaProduct(valor_neto, list_product)

def main():
    iva = Archivo()
    iva.setLeer()
    valores = iva.getLeer()
    iva.setProducto(valores)
    iva.setPrecio()
    list_product = iva.leerArchivo()
    valor_neto = iva.getNeto(list_product)

    print(f'IVA = {valor_neto}\n'+ \
          f'El valor neto o precio sin IVA del producto es = {iva.getivaDelProducto(valor_neto, list_product)}')


if __name__=='__main__': 
    main()