import web, os, base64
from mvc.models.m_detalle import DetalleProductos
from mvc.models.m_actualizar import ActualizarProductos

render = web.template.render('mvc/views/', base='layout')  # Asegúrate de que la ruta sea la correcta

class Actualizar:
    def GET(self, mensaje=""):
        # Capturar el parámetro de consulta 'id'
        params = web.input(id=None)
        producto_id = params.id
        detalle_controller = DetalleProductos()
        response = detalle_controller.detalle_productos(producto_id)

        # Renderizar la plantilla con los detalles del producto
        return render.actualizar(response, mensaje)  # Suponiendo que tienes una plantilla llamada 'detalle.html
    
    def POST(self):
        detalle_controller = DetalleProductos()  # Instancia de DetalleProductos para utilizar su método
        actualizar_controller = ActualizarProductos()
        form = web.input(imagen={})
        id = form.id
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
            imagen_actual = detalle_controller.detalle_productos(id)
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
