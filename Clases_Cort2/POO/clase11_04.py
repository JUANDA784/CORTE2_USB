#IMC version 2
#Que es un diagrama de clase

class Personas():
    def __init__(self): #Este es el construtor
        self.__nombre = None        
        self.__altura = None
        self.__peso = None

    # ------------- Getters ------------------ Me devuelve
    def getNombre(self):
        return self.__nombre
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    
    # ------------- Setters ------------------ Se lleva
    def setNombre(self, nombre:str):#Para que la variable nombre siempre sea string.
        self.__nombre = nombre
    def setAltura(self,altura:int):
        self.__altura = altura
    def setPeso(self,peso:int):
        self.__peso = peso

    # ------------- Metodo IMC ---------------

    

    def __Indice(self):
        IMC = self.__peso/(self.__altura/100)**2
        if IMC <= 18.5:
            return str('Por debajo')
        elif IMC <= 24.9:
            return str('Saludable')
        elif IMC <= 29.9:
            return str('Sobrepeso')
        elif IMC <= 34.9:
            return str('Obesidad I')
        elif IMC <= 39.9:
            return str('Obesidad II')
        else:
            return str('Obesidad III')
        
    def getIMC(self):
        return self.__Indice()

def main():

    estudiante1 = Personas()#Metodo se llama al final con un entreparentesis.Funciones que pertenecen a la clase
    estudiante1.setNombre('Juan David')
    estudiante1.setAltura(174)
    estudiante1.setPeso(57)

    print(f'Student: {estudiante1.getNombre()} tu resultado es: {estudiante1.getIMC()}')

#- metodo privado
#+ metodo publico

if __name__=='__main__':
    main() 
