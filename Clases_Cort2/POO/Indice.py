class Personas():
    def __init__(self):
        self.nombre = None        
        self.altura = None
        self.peso = None

    def Indice(self):
        IMC = self.peso/(self.altura/100)**2
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

def main():

    estudiante1 = Personas()
    estudiante1.nombre = 'Pedro Caseres'
    estudiante1.altura =188
    estudiante1.peso = 97

    estudiante2 = Personas()
    estudiante2.nombre = 'Maria Perez'
    estudiante2.altura = 160
    estudiante2.peso = 47

    estudiante3 = Personas()
    estudiante3.nombre = 'Jualian Dominguez'
    estudiante3.altura = 158
    estudiante3.peso = 58

    estudiante4 = Personas()
    estudiante4.nombre = 'Jessica Fuentes'
    estudiante4.altura = 170
    estudiante4.peso = 73

    print(f'Student: {estudiante1.nombre} tu resultado es: {estudiante1.Indice()}')
    print(f'Student: {estudiante2.nombre} tu resultado es: {estudiante2.Indice()}')    
    print(f'Student: {estudiante3.nombre} tu resultado es: {estudiante3.Indice()}')
    print(f'Student: {estudiante4.nombre} tu resultado es: {estudiante4.Indice()}')

if __name__=='__main__':
    main() 
