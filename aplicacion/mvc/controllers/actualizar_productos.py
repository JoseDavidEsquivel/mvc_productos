import web, os, base64
from mvc.models.m_detalle import DetalleProductos
from mvc.models.m_actualizar import ActualizarProductos

render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

class Actualizar:
    def GET(self, mensaje=""):
        try:
            # Capturar el parámetro de consulta 'id'
            params = web.input(id=None)
            id_encoded = params.id
            id = decode_id(id_encoded)
            detalle_controller = DetalleProductos()
            response = detalle_controller.detalle_productos(id)

            # Renderizar la plantilla con los detalles del producto
            return render.actualizar(response, mensaje)  # Suponiendo que tienes una plantilla llamada 'detalle.html
        except Exception as e:
            # En caso de que falle la decodificación del ID
            response = ""
            mensaje = "Id no válido"
            # Redirigir al usuario a una página de error
            return render.error(response, mensaje)
        
    
    def POST(self):
        detalle_controller = DetalleProductos()  # Instancia de DetalleProductos para utilizar su método
        actualizar_controller = ActualizarProductos()
        form = web.input(imagen={})
        id_encoded = form.id
        id = decode_id(id_encoded)
        nombre = form.nombre2
        descripcion = form.descripcion2
        precio = form.precio
        if float(precio) < 0:
            precio = 0
        existencias = form.existencias
        if int(existencias) < 0:
            existencias = 0
        imagen = form.imagen

        tamano_imagen = len(imagen.value)
        # Verificar el tamaño del archivo
        tamano_maximo = 1024 * 1024  # 1MB
        if int(tamano_imagen) > tamano_maximo:
            mensaje = 'El tamaño de la imagen excede el límite permitido (1MB)'
            response = detalle_controller.detalle_productos(id)
            return render.actualizar(response,mensaje)

        imagen_nombre = imagen.filename
        imagen_extension = os.path.splitext(imagen.filename)[-1]

        # print(f"La extension de tu imagen es {imagen_extension}")
        # print(f"Con el nombre de {imagen_nombre}")

        if imagen_extension:
            # Cambiar el nombre de la imagen al ID del producto
            imagen_nombre = str(id) + imagen_extension

            # Guardar la imagen en el servidor
            with open('static/images/' + imagen_nombre, 'wb') as f:
                f.write(imagen.file.read())
            imagen_nombre = str(id)
        else:
            print(id)
            imagen_actual = detalle_controller.detalle_productos(id)
            print(imagen_actual)
            imagen_nombre = imagen_actual[0]['imagen_nombre']
            imagen_extension =  imagen_actual[0]['imagen_extension']
            # print(f"La extension de tu imagen es {imagen_extension}")
            # print(f"Con el nombre de {imagen_nombre}")
            detalle_controller.close_connection()
            detalle_controller.__init__()

        # print(id, nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension)
        mensaje = actualizar_controller.actualizar_productos(id, nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension)
        response = detalle_controller.detalle_productos(id)
        return render.actualizar(response,mensaje)


def decode_id(encoded_id):
    # Decodificar el ID desde Base64 y luego decodificar a cadena
    decoded_id = base64.urlsafe_b64decode(encoded_id.encode()).decode()
    return decoded_id

