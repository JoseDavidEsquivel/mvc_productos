import web
from mvc.models.m_detalle import DetalleProductos

render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

class Detalle:
    def GET(self):
        # Capturar el parámetro de consulta 'id'
        params = web.input(id=None)
        temp_id = params.id
        temp_id = temp_id.replace('{','')
        temp_id = temp_id.replace('}','')
        producto_id = temp_id
        detalle_controller = DetalleProductos()
        response = detalle_controller.detalle_productos(producto_id)

        # Renderizar la plantilla con los detalles del producto
        return render.detalle(response=response)  # Suponiendo que tienes una plantilla llamada 'detalle.html
