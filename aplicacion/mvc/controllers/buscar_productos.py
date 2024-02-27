import web
from mvc.models.m_buscar import BuscarProductos


render = web.template.render('mvc/views/', base='layout')

class Buscar:
    def GET(self):
        return render.buscar(listado=[])  # Pasar una lista vacía al renderizar la página inicialmente
    
    def POST(self):
        listar_controller = BuscarProductos()
        form = web.input()
        id = form.id
        nombre = form.nombre
        descripcion = form.descripcion
        precio = form.precio
        existencias = form.existencias
        # existencias = ""
        listado = listar_controller.buscar_productos(id, nombre, descripcion, precio, existencias)
        return render.buscar(listado=listado)  # Pasar el listado obtenido de la búsqueda a la vista

    


 