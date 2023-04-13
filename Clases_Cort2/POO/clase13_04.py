
class Deportista:
        def __init__(self,nombre:str,documento:int,edad:int):
            self.__nombre = nombre
            self.__documento = documento
            self.__edad = edad
        # ------------- Getters ------------------     

        def getNombre(self):
            return self.__nombre
        def getDocumento(self):
            return self.__documento
        def getEdad(self):
            return self.__edad

        # ------------- Setters ------------------
        def setNombre(self, nombre:str):
            self.__nombre = nombre
        def setDocumento(self,documento:int):
            self.__documento = documento
        def setEdad(self,edad:int):
            self.__edad = edad

        #-------------- Sobrecarga ----------------
        def medalla(self):
            return 'Has ganado una medalla'

class DeportistaFutbol(Deportista):
    def __init__(self, nombre: str,documento: int,edad: int, goles: int, \
                 nombreEquipo: str):
        super().__init__(nombre,documento,edad)
        self.__goles = goles
        self.__nombreEquipo = nombreEquipo

    def getGoles(self):
        return self.__goles
    def getNombreEquipo(self):
        return self.__nombreEquipo
    
    def setGoles(self, goles:str):
        self.__goles = goles
    def setNombreEquipo(self,nombreEquipo:int):
        self.__nombreEquipo = nombreEquipo

    def medalla(self):
            return 'Has ganado la Europa League'

def main():
    Futbolista = DeportistaFutbol('Falcao',2483543634,36,35,'Selección Colombia')
    Futbolista2 = Deportista('Juan',103484383,18)
    

    print(f'Deportistas: {Futbolista.getNombre()}\n'+\
    f'Documento: {Futbolista.getDocumento()}\n'+\
    f'Edad: {Futbolista.getEdad()}\n'+\
    f'Cantidad de goles: {Futbolista.getGoles()}\n'+\
    f'Deportistas: {Futbolista.getNombreEquipo()}\n'+\
    f'medalla:{Futbolista.medalla()}\n')

    print(f'Deportistas: {Futbolista2.getNombre()}\n'+\
    f'Documento: {Futbolista2.getDocumento()}\n'+\
    f'Edad: {Futbolista2.getEdad()}\n'+\
    f'medalla:{Futbolista2.medalla()}')

if __name__=='__main__':
    main()        