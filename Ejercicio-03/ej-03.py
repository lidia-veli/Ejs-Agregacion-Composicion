from enum import Enum
class Orientacion(Enum):
    N = "Norte"
    S = "Sur"
    E = "Este"
    W = "Oeste"

dic_orient = {"N": Orientacion.N, "NORTE": Orientacion.N,
              "S": Orientacion.S, "SUR": Orientacion.S, 
              "E": Orientacion.E,"ESTE": Orientacion.E, 
              "O": Orientacion.W,"W": Orientacion.W ,"OESTE": Orientacion.W}

paredes_con_ventana = {}  # diccionario de paredes con ventanas
# donde vamos a ir añadiendo las paredes que tengan ventanas con la ventana asociada que tengan

lista_protecciones_ventanas = ['persiana', 'estor', 'cortina']


def pasar_a_tipo_ori(orientacion_str):
    '''Funcion que convierte una cadena de texto en un tipo de orientación'''
    if isinstance(orientacion_str, str):
        ori = orientacion_str.upper()  # lo ponemos en mayúsculas
        if ori in dic_orient:  # y comprobamos que es una orientación válida
            return dic_orient[ori]
        else:
            raise ValueError("Orientación no válida")


class Pared:
    def __init__(self, orientacion):
        self.orientacion = pasar_a_tipo_ori(orientacion) 
    
    def __str__(self):
        return f'Pared de orientación {self.orientacion.value}'



class Cristal:
    def __init__(self, orientacion, superficie, proteccion):
        self.orientacion = pasar_a_tipo_ori(orientacion)
        self.superficie = superficie
        self.proteccion = proteccion

        if not isinstance(superficie, int) and not isinstance(superficie, float):
            raise TypeError("El parámetro superficie debe ser un número real")
        if isinstance(proteccion, str):
            if proteccion.lower() in lista_protecciones_ventanas:
                pass
            else:
                raise ValueError("La protección no es válida")
        else:
            raise Exception("Protección obligatoria")
        
    
    def __str__(self):
        pass


class ParedCortina(Cristal):
    def __init__(self, orientacion, superficie, proteccion):
        Cristal.__init__(self, orientacion, superficie, proteccion)
        paredes_con_ventana.update({self : self})

    def __str__(self):
        return f'Pared Cortina de orientación {self.orientacion.value} y superficie {self.superficie}'


class Ventana(Cristal):
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        paredes_con_ventana.update({pared : self})
        Cristal.__init__(self, pared.orientacion, superficie, proteccion)

    def __str__(self):
        return f'Ventana de orientación {self.pared.orientacion.value} y superficie {self.superficie}'


class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

        if isinstance(paredes, list): # TRUE si el parámetro paredes es una lista
            for p in paredes:
                if not isinstance(p, Pared):
                    raise TypeError("Los objetos dentro de la lista deben ser de la clase Pared")
                else:
                    pass
        else:  # FALSE si el parámetro paredes no es una lista
            raise TypeError("El parámetro paredes deben ser una lista de objetos de la clase Pared")
        
    
    def superficie_acristalada(self):
        superficie = 0
        for p in self.paredes:  # recorremos la lista de paredes
            if p in paredes_con_ventana:  # si hay una ventana en esa pared
                superficie += paredes_con_ventana[p].superficie
        return superficie


if __name__ == "__main__":
    # Instanciación de las paredes
    pared_norte = Pared("NORTE")
    pared_oeste = Pared("OESTE")
    pared_sur = Pared("SUR")
    pared_este = Pared("ESTE")

    # Instanciación de las ventanas
    ventana_norte = Ventana(pared_norte, 0.5, "persiana")
    ventana_oeste = Ventana(pared_oeste, 1, "estor")
    ventana_sur = Ventana(pared_sur, 2, "cortina")
    ventana_este = Ventana(pared_este, 1, "cortina")

    # Instanciación de la casa con las 4 paredes
    casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
    print('Superficie acristalada casa 4 ventanas:', casa.superficie_acristalada())
    # >>> 4.5 # 0.5 + 1 + 2 + 1

    # Cambiamos una ventana por una pared cortina
    casa.paredes[2] = ParedCortina("SUR", 10, "cortina")
    print('Superficie acristalada casa 3 ventanas y 1 pared-cortina:',casa.superficie_acristalada())
    # >>> 12.5
