import web
from mvc.models.m_insertar import InsertarProductos

render = web.template.render('mvc/views/', base='layout')

class Insertar:
    def GET(self, mensaje = "" ):
         # Definir mensaje aquí o de donde sea apropiado
        return render.insertar(mensaje)

    def POST(self):
        insertar_controller = InsertarProductos()
        form = web.input()
        nombre = form.nombre
        descripcion = form.descripcion
        precio = form.precio
        if precio < 0:
            precio = 0
        existencias = form.existencias
        if existencias < 0:
            existencias = 0
        
        mensaje = insertar_controller.insertar_productos(nombre, descripcion, precio, existencias)
        # Aquí pareces estar sobrescribiendo el mensaje, ten cuidado si esto es intencional
        return render.insertar(mensaje)
