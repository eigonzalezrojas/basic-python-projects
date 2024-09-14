"""
*args 
Crea una función que retorne la suma
de una cantidad indefinida de números
1 * signfica que recibe de a un valor

"""

def suma(*args):
    return sum(args)

print (suma(1,2,3))


"""
**kwargs
Crea una función que muestre la información
de un empleado (información desconocida)
el doble ** indica que la data es de tipo diccionario

"""


def mostrar_info(**kwargs):
    for clave, valor in kwargs.items(): # se utiliza el metodo items para recorrer en un diccionario
        print(f"{clave} : {valor}")
        
mostrar_info(nombre="Eithel", edad=35)