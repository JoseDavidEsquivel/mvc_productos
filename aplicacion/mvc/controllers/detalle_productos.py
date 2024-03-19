# import web
# from mvc.models.m_detalle import DetalleProductos

# render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

# class Detalle:
#     def GET(self):
#         # Capturar el parámetro de consulta 'id'
#         params = web.input(id=None)
#         producto_id = params.id
#         detalle_controller = DetalleProductos()
#         response = detalle_controller.detalle_productos(producto_id)
#         print(producto_id)

#         # Renderizar la plantilla con los detalles del producto
#         return render.detalle(response=response)  # Suponiendo que tienes una plantilla llamada 'detalle.html

import web
from mvc.models.m_detalle import DetalleProductos
import base64

render = web.template.render('mvc/views/', base='layout')

class Detalle:
    def GET(self):
        try:
            # Capturar el parámetro de consulta 'id'
            params = web.input(id=None)
            producto_id_encoded = params.id
            producto_id = decode_id(producto_id_encoded)  # Decodificar el ID

            detalle_controller = DetalleProductos()
            response = detalle_controller.detalle_productos(producto_id)

            # Renderizar la plantilla con los detalles del producto
            return render.detalle(response=response)
        except Exception as e:
            # En caso de que falle la decodificación del ID
            response = ""
            mensaje = "Id no válido"
            # Redirigir al usuario a una página de error
            return render.error(response, mensaje)

def decode_id(encoded_id):
    # Decodificar el ID desde Base64 y luego decodificar a cadena
    decoded_id = base64.urlsafe_b64decode(encoded_id.encode()).decode()
    return decoded_id
