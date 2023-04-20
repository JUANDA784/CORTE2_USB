class Ciudadano:
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
    def saludo(self):
        return 'Hola soy un ciudadano'


class Arquitecto(Ciudadano):
    def __init__(self, nombre: str,documento: int,edad: int, tipodeconstrucion: str, \
                 experiencia: int):
        super().__init__(nombre,documento,edad)
        self.__tipodeconstrucion = tipodeconstrucion
        self.__experiencia = experiencia 

    def getTipodeconstrucion(self):
        return self.__tipodeconstrucion
    def getExperiencia(self):
        return self.__experiencia
    
    def setTipodeconstrucion(self, tipodeconstrucion:str):
        self.__tipodeconstrucion = tipodeconstrucion
    def setExperiencia(self,experiencia:int):
        self.__experiencia = experiencia


class MedicoCirujano(Ciudadano):
    def __init__(self, nombre: str,documento: int,edad: int, universidad: str, \
                 especializacion: str):
        super().__init__(nombre,documento,edad)
        self.__universidad = universidad
        self.__especializacion = especializacion

    def getUniversidad(self):
        return self.__universidad
    def getEspecializacion(self):
        return self.__especializacion
    
    def setUniversidad(self, universidad:str):
        self.__universidad = universidad
    def setEspecializacion(self,especializacion:int):
        self.__especializacion = especializacion

    
class Administrador(Ciudadano):
    def __init__(self, nombre: str,documento: int,edad: int, numempresas: int, \
                 empresamasgrande: str):
        super().__init__(nombre,documento,edad)
        self.__numempresas = numempresas
        self.__empresamasgrande = empresamasgrande

    def getNumempresas(self):
        return self.__numempresas
    def getEmpresamasgrande(self):
        return self.__empresamasgrande
    
    def setNumempresas(self, numempresas:str):
        self.__numempresas = numempresas
    def setEmpresamasgrande(self,nombreEquipo:int):
        self.__nombreEquipo = nombreEquipo

    def saludo(self):
        return 'Hola soy un administrador de empresas muy exitoso'


def main():
    arquitecto = Arquitecto('Daniel',1235436546,30,'Rascacielo',5)
    medicoCirujano = MedicoCirujano('Gabriel',101203405,40,'Universidad la Javeriana','Cardiovascular')
    administrador = Administrador('Juan',1066865613,27,6,'Microsoft')

    print(f'Nombre: {arquitecto.getNombre()}\n'+\
    f'Documento: {arquitecto.getDocumento()}\n'+\
    f'Edad: {arquitecto.getEdad()}\n'+\
    f'Tipo de construcion: {arquitecto.getTipodeconstrucion()}\n'+\
    f'Experiencia: {arquitecto.getExperiencia()}\n'+\
    f'Saludo: {arquitecto.saludo()}\n')

    print(f'Nombre: {medicoCirujano.getNombre()}\n'+\
    f'Documento: {medicoCirujano.getDocumento()}\n'+\
    f'Edad: {medicoCirujano.getEdad()}\n'+\
    f'Universidad: {medicoCirujano.getUniversidad()}\n'+\
    f'Estudios: {medicoCirujano.getEspecializacion()}\n'+\
    f'Saludo: {medicoCirujano.saludo()}\n')

    print(f'Nombre: {administrador.getNombre()}\n'+\
    f'Documento: {administrador.getDocumento()}\n'+\
    f'Edad: {administrador.getEdad()}\n'+\
    f'Numero de empresas: {administrador.getNumempresas()}\n'+\
    f'Empresa mas grande que administró: {administrador.getEmpresamasgrande()}\n'+\
    f'Saludo: {administrador.saludo()}\n')


if __name__=='__main__':
    main()  