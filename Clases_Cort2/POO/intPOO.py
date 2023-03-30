#POO = Programacion orientada a objetos.
class Persona:
    def __init__(self):
        self.nombre = None
        self.apellido = None # None = vacio
        self.edad = None #Self = llama asi mismo
        self.frase = None
    def hablar(self):
        return self.frase

def main():
    estudiante = Persona()
    estudiante.nombre = 'Juan'
    estudiante.apellido = 'Rivero'
    estudiante.edad = 18
    estudiante.frase = 'Oh debo estudiar!'

    futbolista = Persona()
    futbolista.nombre = 'Radamel'
    futbolista.apellido = 'Garcia'
    futbolista.edad = 36
    futbolista.frase = 'Gooooooollll!'

    print(f'El estudiante dice: {estudiante.hablar()}')
    print(f'El señor futbolista dice: {futbolista.hablar()}')

    print(id(estudiante)) #id para mostrar el espacio de memoria del objeto. 
    print(id(futbolista))

if __name__=='__main__':
    main()

