class Ciudadano():
    def __init__(self): 
        self.__nombre = None        
        self.__cédula = None
        self.__edad = None

    # ------------- Getters ------------------ 
    def getNombre(self):
        return self.__nombre
    def getCédula(self):
        return self.__cédula
    def getEdad(self):
        return self.__edad
    
    # ------------- Setters ------------------ 
    def setNombre(self):
        self.__nombre = input('Nombre del ciudadano: ')
    def setCédula(self):
        self.__cédula = int(input('Cédula del ciudadano: '))
        digit = 0
        cedula = self.__cédula
        while cedula > 0:
            digit += 1
            cedula = cedula // 10
        
        if not 8 <= digit < 11:     
            print('ERROR. El número de digitos de la cédula tiene que ser entre 8 y 10')
            self.__cédula = None
        else:
            self.__cédula = self.__cédula

    def setEdad(self):
        self.__edad = int(input('La edad del ciudadano: '))
        if self.__edad < 0:
            print('La edad tiene que ser mayor que 0')
            self.__edad = None

    # ------------- Metodo mostrar ---------------

    def __Mostrar(self):

        return f'Nombre: {self.__nombre} - Edad: {self.__edad} - CC: {self.__cédula}'
        
    def getInfo(self):
        return self.__Mostrar()
    
    # --------------- Metodo esMayorDeEdad ---------------

    def __esMayorDeEdad(self):
        edad = self.__edad
        if edad != None:
            if edad < 18:
                return str('El ciudadano es MENOR de edad')
            else:
                return str('El ciudadano es MAYOR de edad')
        else:
            return str('NO puedo decir si es mayor o menor porque la edad que pusiste es incorrecta')
    
    def getEdadMayor(self):
        return self.__esMayorDeEdad()

# ---------------- Función main ------------------

def main():

    persona1 = Ciudadano()
    persona1.setNombre()
    persona1.setCédula()
    persona1.setEdad()

    print(f'{persona1.getInfo()}\n')
    print(persona1.getEdadMayor())
    

if __name__=='__main__':
    main() 