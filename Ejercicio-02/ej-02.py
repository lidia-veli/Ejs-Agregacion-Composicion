'''ENUNCIADO: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, 
se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?'''


class Yin: 
    pass 

class Yang: 
    def __del__(self): 
        print("Yang destruido") 


yin = Yin()  # instanciar Yin
yang = Yang()  # instanciar Yang
yin.yang = yang  # guardamos la referencia al objeto Yang como atributo del objeto de tipo Yin
 
print(yang) 
#>>> <__main__.Yang object at 0x1011da828> 

print(yang is yin.yang)  # hacen referencia al mismo aobjeto
#>>> True

# Se destruye la instancia 'yang' del objeto de clase Yang pero no se muestra que el objeto destruído
# porque todavía hay otra variable que hace referencia a ese objeto (yin.yang).
#del(yang)
#print("?")      
#>>> ? 
#    Yang destruido          # se destruye una vez se acaba el programa


# para que aparezca antes la destrucción del objeto Yang hay que eliminar también la otra variable
# que hace referencia a ese objeto. Tendríamos que sustituir el párrafo decódigo anterior por:
del(yang)
del(yin.yang)
print("?")
#>>> Yang destruido
#    ?
