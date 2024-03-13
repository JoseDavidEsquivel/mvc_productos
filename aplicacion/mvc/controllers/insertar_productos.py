import web, os
from mvc.models.m_insertar import InsertarProductos

render = web.template.render('mvc/views/', base='layout')

class Insertar:
    def GET(self, mensaje=""):
        return render.insertar(mensaje)

    def POST(self):
        insertar_controller = InsertarProductos()
        form = web.input(imagen={})
        nombre = form.nombre
        descripcion = form.descripcion
        precio = form.precio
        if float(precio) <= 0:
            precio = 0
        existencias = form.existencias
        if int(existencias) <= 0:
            existencias = 0
        imagen = form.imagen

        

        # Verificar el tamaño del archivo
        tamano_maximo = 1024 * 1024  # 1MB
        if len(imagen.value) > tamano_maximo:
            mensaje = 'El tamaño de la imagen excede el límite permitido (1MB)'
            return render.insertar(mensaje)
        
        print(len(imagen.value))

        imagen_nombre = imagen.filename
        imagen_extension = os.path.splitext(imagen.filename)[-1]

        # Obtener el último ID insertado en la base de datos
        ultimo_id = insertar_controller.obtener_ultimo_id()
        if ultimo_id is None:
            ultimo_id = 0
        else:
            ultimo_id = int(ultimo_id)

        # Cambiar el nombre de la imagen al ID del producto
        imagen_nombre = str(ultimo_id + 1) + imagen_extension

        # Guardar la imagen en el servidor
        with open('static/images/' + imagen_nombre, 'wb') as f:
            f.write(imagen.file.read())

        imagen_nombre = str(ultimo_id + 1)
        # Insertar el producto en la base de datos
        mensaje = insertar_controller.insertar_productos(nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension)
        return render.insertar(mensaje)
