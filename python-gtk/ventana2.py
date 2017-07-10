import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

if __name__== '__main__':
	ventana = Gtk.Window(title='ejemplo 1')
	ventana.connect('delete-event',Gtk.main_quit)
	button2= Gtk.Button('este es el primer boton')
	
	pass