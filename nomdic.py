import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser('valor')
    parser.add_argument('NOMBRE')
    args = parser.parse_args()

    registro = {'NOMBRE':{'Carol','Brian'}}

    for llave,valor in registro.iteritems():
        if args.NOMBRE == llave:
   	        print('la llave',args.NOMBRE,' se registra en el diccionario')

        else:
           print('la llave',args.NOMBRE,'no  se registra en el diccionario')