import web, base64
from mvc.models.m_detalle import DetalleProductos
from mvc.models.m_borrar import BorrarProductos

render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

class Borrar:
    def GET(self):
        try:
            # Capturar el parámetro de consulta 'id'
            params = web.input(id=None)
            id_encoded = params.id
            id = decode_id(id_encoded)
            detalle_controller = DetalleProductos()
            response = detalle_controller.detalle_productos(id)

            # Renderizar la plantilla con los detalles del producto
            return render.borrar(response)  # Suponiendo que tienes una plantilla llamada 'detalle.html
        except Exception as e:
                # En caso de que falle la decodificación del ID
                response = ""
                mensaje = "Id no válido"
                # Redirigir al usuario a una página de error
                return render.error(response, mensaje)
    
    def POST(self):
        borrar_controller = BorrarProductos()
        form = web.input()
        id_producto = form.id
        resultado = borrar_controller.eliminar_producto(id_producto)
        
        # Después de borrar, redirigir al usuario a la lista de productos u otra página adecuada
        raise web.seeother('/')

def decode_id(encoded_id):
    # Decodificar el ID desde Base64 y luego decodificar a cadena
    decoded_id = base64.urlsafe_b64decode(encoded_id.encode()).decode()
    return decoded_id

