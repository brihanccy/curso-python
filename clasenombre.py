import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('NOMBRE')
    parser.add_argument('EDAD')
    parser.add_argument('clase')
    args = parser.parse_args()
   
    registro = {
    'NOMBRE': args.NOMBRE,
    'EDAD': args.EDAD,
    'clase': args.clase}
    
    for llave,valor in registro.iteritems():
   	    print(llave,valor)
   		

    

    
    