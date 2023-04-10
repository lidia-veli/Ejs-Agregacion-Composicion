class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f'Hola, soy {self.nombre}'
    
    def __del__(self):
        print(f'{self.nombre} se ha quedado en el paro')


class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empresa = None  # empresa a la que pertenece el edificio AGREGACIÓN
        # en un principio no pertenece a ninguna

    def __str__(self):
        return f'Edificio {self.nombre} de la empresa {self.empresa}'
    
    def __del__(self):
        print(f'Se ha destruido el edificio {self.nombre}')


class Ciudad:
    def __init__(self, nombre, lista_nombre_edificios):
        self.nombre = nombre
        # empresas de la ciudad: COMPOSICIÓN
        self.edificios = [ Edificio(name) for name in lista_nombre_edificios]
    
    def __str__(self):
        return f'En la ciudad de {self.nombre} están los edificios: {self.edificios}'
    
    def __del__(self):
        print(f'Destrucción catastrófica de la ciudad de {self.nombre}!!')


class Empresa:
    def __init__(self, nombre, lista_nombre_empleados):
        self.nombre = nombre
        
        # empleados de la empresa: COMPOSICIÓN
        self.empleados = [ Empleado(name) for name in lista_nombre_empleados ]

        # edificios de la empresa: AGREGACIÓN
        self.edificios = []
    
    def __str__(self):
        return f'Empresa {self.nombre}'
    
    def __del__(self):
        print(f'Ha desaparecido la empresa {self.nombre}')
    
    def agregar_edificios(self, lista_edif):
        for edif in lista_edif:
            if isinstance(edif, Edificio):
                self.edificios.append(edif)  # añadimos el edificio a la lista-atributo .edificios de la empresa
                edif.empresa = self  # actualizamos el atributo del objeto Edificio, que ahora pertenece a esta empresa
            else:
                raise TypeError('El objeto debe ser de la clase Edificio')


if __name__ == '__main__':
    # Instanciamos compañia
    company = Empresa('YooHoo', ['Martin','Salim','Xing'] )
    print(company)
    print()

    # Instanciamos empleados
    employees = company.empleados  # lista de objetos clase Empleado
    for e in employees:
        print(e)
    print()

    # Instanciamos ciudades
    new_york = Ciudad('New York', ['Alfa','Beta'])
    print(new_york)
    los_angeles = Ciudad('Los Angeles', ['Casio'])
    print(los_angeles)
    print()

    company.agregar_edificios(new_york.edificios + los_angeles.edificios)  # asociamos los edificios a la empresa
    buildings = company.edificios  # lista de edificios de la compañía
    for b in buildings: 
        print(b)
    
    # Destruccion ciudades
    del new_york
    del los_angeles

