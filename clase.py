class Animal (object):

	def __init__(self, perro, gato):
	        self.perro= perro
	        self.gato= gato


def obtener_informacion(self):
    print 'Diga que tipo de animal es'
    return '{perro} {gato}'.format(perro=self.perro,gato=self.gato)

class Perro (Animal):
	def __init__(self, nombre, color, cola):
            self.nombre = nombre
            self.cola = cola
            self.color = color
	def obtener_informacion(self):
         print 'dijite los datos del perro'
         return '{nombre} {cola} {color}'.format(nombre=self.nombre,cola=self.cola,color=self.color)


class Gato(Animal):
    def __init__(self, nombre, raza, pelo):
        self.nombre = nombre
        self.raza = raza
        self.pelo = pelo

    def obtener_informacion(self):
        print 'dijite los datos del gato'
        return '{nombre} {raza} {pelo}'.format(nombre=self.nombre, raza=self.raza, pelo=self.pelo)


if __name__=='__main__':
    gatos= Gato ('MICHI', 'ANGORA','BLANCO')
    print (gatos.obtener_informacion())
    perros= Perro ('DOLAR', 'LARGA', 'CAFE')
    print(perros.obtener_informacion())