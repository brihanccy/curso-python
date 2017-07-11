import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Mi_Ventana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(Mi_Ventana, self).__init__(*args, **kwargs)
		self.set_size_request(500, 300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set.column_homogeneous(True)
		self.add(self.contenedor)
	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		set.contenedor.attach(self.entrada,0,0,1,1)
	def agregar_boton(self):
		self.boton = Gtk.Button('agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.positionType.BOTON,
			1,
			1
			)
	def agregar_lista(self):
		'''

		crear un treview:
		1. crear el model de datos Gtk.ListStore(type,type,...,type)
		2. crear el vidget
