import web
from mvc.models.m_detalle import DetalleProductos
from mvc.models.m_borrar import BorrarProductos

render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

class Borrar:
    def GET(self):
        # Capturar el parámetro de consulta 'id'
        params = web.input(id=None)
        producto_id = params.id
        detalle_controller = DetalleProductos()
        response = detalle_controller.detalle_productos(producto_id)

        # Renderizar la plantilla con los detalles del producto
        return render.borrar(response)  # Suponiendo que tienes una plantilla llamada 'detalle.html
    
    def POST(self):
        borrar_controller = BorrarProductos()
        form = web.input()
        id_producto = form.id
        resultado = borrar_controller.eliminar_producto(id_producto)
        
        # Después de borrar, redirigir al usuario a la lista de productos u otra página adecuada
        raise web.seeother('/')

