class Ciudadano():
    def __init__(self): 
        self.__idioma = None        
        self.__nombre = None

    # ------------- Getters ------------------
    def getIdioma(self):
        return self.__idioma
    def getNombre(self):
        return self.__nombre
    
    # ------------- Setters ------------------ 
    def setNombre(self, nombre:str):
        self.__nombre = nombre
    def setIdioma(self,idioma:str):
        self.__idioma = idioma


    def saludo(self):
        return "Bonjorno!"


class Colombia(Ciudadano):
    def __init__(self):
        super().__init__()

        self.__cc = None

    def getCC(self):
        return self.__cc
    
    def setCC(self, cc:int):
        self.__cc = cc 

    def saludo(self):
        return 'Qiubo parce!'


class Inglaterra(Ciudadano):
    def __init__(self):
        super().__init__()

        self.__id = None

    def getId(self):
        return self.__id
    
    def setId(self, id:int):
        self.__id = id 

    def saludo(self):
        return 'Quoi de beau!'


class China(Ciudadano):
    def __init__(self):
        super().__init__()

        self.__shengfenzheng = None

    def getShengfenzheng(self):
        return self.__shengfenzheng
    
    def setShengfenzheng(self, shengfenzheng:int):
        self.__shengfenzheng = shengfenzheng 

    def saludo(self):
        return 'NiGanMaYa !!'


def darSaludo(obj:Ciudadano):
    return obj.saludo()


def main():
    colombiano = Colombia()
    colombiano.setNombre('Kevin')
    colombiano.setIdioma('Español')
    colombiano.setCC(1538292)

    ingles = Inglaterra()
    ingles.setNombre('Richard')
    ingles.setIdioma('English')
    ingles.setId(8221492732)
    
    chino = China()
    chino.setNombre('Richard')
    chino.setIdioma('English')
    chino.setShengfenzheng(845)

    persona = Ciudadano()
    persona.setNombre('Richard')
    persona.setIdioma('English')

    print(f'Aplicante: {colombiano.getNombre()}\n'+\
          f'Idioma: {colombiano.getIdioma()}\n' + \
          f'CC: {colombiano.getCC()}\n'+\
          darSaludo(colombiano))
    
    print(f'Aplicante: {ingles.getNombre()}\n'+\
          f'Idioma: {ingles.getIdioma()}\n'+ \
          f'CC: {ingles.getId()}\n'+\
          darSaludo(ingles))
    
    print(f'Aplicante: {chino.getNombre()}\n'+\
          f'Idioma: {chino.getIdioma()}\n' + \
          f'CC: {chino.getShengfenzheng()}\n'+\
          darSaludo(chino))
    
    print(f'Aplicante: {chino.getNombre()}\n'+\
          f'Idioma: {chino.getIdioma()}\n' + \
          darSaludo(persona))


if __name__=='__main__':
    main()
