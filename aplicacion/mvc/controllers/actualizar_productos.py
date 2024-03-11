import web
from mvc.models.m_detalle import DetalleProductos
from mvc.models.m_actualizar import ActualizarProductos

render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

class Actualizar:
    def GET(self):
        # Capturar el parámetro de consulta 'id'
        params = web.input(id=None)
        producto_id = params.id
        detalle_controller = DetalleProductos()
        response = detalle_controller.detalle_productos(producto_id)

        # Renderizar la plantilla con los detalles del producto
        return render.actualizar(response)  # Suponiendo que tienes una plantilla llamada 'detalle.html
    
    def POST(self):
        actualizar_controller = ActualizarProductos()
        form = web.input()
        id = form.id
        nombre = form.nombre2
        descripcion = form.descripcion2
        precio = form.precio2
        if float(precio) < 0:
            precio = 0
        existencias = form.existencias2
        if int(existencias) < 0:
            existencias = 0
        # print(id, nombre, descripcion, precio, existencias)
        actualizar_controller.actualizar_productos(id, nombre, descripcion, precio, existencias)
        detalle_controller = DetalleProductos()
        response = detalle_controller.detalle_productos(id)
        # Aquí pareces estar sobrescribiendo el mensaje, ten cuidado si esto es intencional
        return render.actualizar(response)

