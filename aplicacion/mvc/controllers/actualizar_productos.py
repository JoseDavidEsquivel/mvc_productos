import web
from mvc.models.m_detalle import DetalleProductos
from mvc.models.m_actualizar import ActualizarProductos

render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

class Actualizar:
    def GET(self, mensaje = "" ):
        # Capturar el parámetro de consulta 'id'
        params = web.input(id=None)
        temp_id = params.id
        temp_id = temp_id.replace('{','')
        temp_id = temp_id.replace('}','')
        producto_id = temp_id
        detalle_controller = DetalleProductos()
        response = detalle_controller.detalle_productos(producto_id)

        # Renderizar la plantilla con los detalles del producto
        return render.actualizar(mensaje,response)  # Suponiendo que tienes una plantilla llamada 'detalle.html
    
    def POST(self, mensaje = "YUPI!!!!!" ):
        actualizar_controller = ActualizarProductos()
        form = web.input()
        temp_id = form.id
        temp_id = temp_id.replace('{','')
        temp_id = temp_id.replace('}','')
        id = temp_id
        nombre = form.nombre2
        descripcion = form.descripcion2
        precio = form.precio2
        existencias = form.existencias2
        print(id, nombre, descripcion, precio, existencias)
        mensaje = actualizar_controller.actualizar_productos(id, nombre, descripcion, precio, existencias)
        detalle_controller = DetalleProductos()
        response = detalle_controller.detalle_productos(id)
        # Aquí pareces estar sobrescribiendo el mensaje, ten cuidado si esto es intencional
        return render.insertar(response)

