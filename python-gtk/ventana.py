import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

if __name__ == '__main__':
	ventana = Gtk.Window(title = 'ejemplo 1')
	ventana.connect('delete-event',Gtk.main_quit)
	button = Gtk.Button('botton1')
	button2 = Gtk.Button('Boton2')
	button3 = Gtk.Button('Boton3')
	button4 = Gtk.Button('salir')
	button4.connect('clicked', Gtk.main_quit)
	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)

	contenedor.attach(
		button,#elemento
		0,#columna
		0,#fila
		3,#numero de columnas a usar
		1,#numero de filas a usar
		)
	contenedor.attach(button2,1,1,1,1)
	contenedor.attach(button3,2,1,1,1)
	contenedor.attach(button4,0,2,1,1)

	ventana.add(contenedor)
	contenedor = Gtk.VBox()
	contenedor.pack_start(button,False,False,0)
	contenedor.pack_end(button2,False,False,0)
	ventana.add(contenedor)
	ventana.show_all()
	
	Gtk.main()