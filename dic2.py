import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]


def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'ciudad': random.choice(CIUDADES)
        }

    return estudiantes

libreria=generar_diccionario_estudiantes()

for clave,valor in libreria.iteritems():
    lista= 'El nombre del estudiante es {0} de edad {1}, es de la ciudad de {2} y ' \
           'cursa {3} en la universidad'
    print (lista.format(clave,valor['edad'],valor['ciudad'],valor['anio']))
for clave,valor in libreria .iteritems():
    lista1 = 'el estudiante {0} de la ciudad de {1} es de edad {2}, es de la ciudad de {3}, y' \
             'cursa {3} en la universidad'
    if valor['ciudad'] =='Managua':
        print (lista1.format(clave,valor['ciudad'],valor['edad'],valor['anio']))
for clave, valor in libreria.iteritems():
    lista2 = 'el estudiante {0} de la ciudad de {1} es de edad {2}, es de la ciudad de {3}, y' \
             'cursa {3} en la universidad'
    if valor['ciudad'] == 'Masaya' and valor['anio']== 1:
        print (lista1.format(clave,valor['ciudad'],valor['edad'],valor['anio']))
for clave, valor in libreria.iteritems():
    lista3 = 'el estudiante {0} de la ciudad de {1} es de edad {2}, es de la ciudad de {3}, y' \
             'cursa {3} en la universidad'
    if valor ['edad'] < 21 :
        print (lista1.format(clave, valor['ciudad'], valor['edad'], valor['anio']))


