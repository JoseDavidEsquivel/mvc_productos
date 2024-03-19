import web, base64
from mvc.models.m_buscar import BuscarProductos


render = web.template.render('mvc/views/', base='layout')

class Buscar:
    def GET(self):
        return render.buscar(listado=[])  # Pasar una lista vacía al renderizar la página inicialmente
    
    def POST(self):
        listar_controller = BuscarProductos()
        form = web.input()
        id = form.id
        nombre = form.nombre
        descripcion = form.descripcion
        precio = form.precio
        existencias = form.existencias
        # existencias = ""
        listado = listar_controller.buscar_productos(id, nombre, descripcion, precio, existencias)
        # print(listado)

        for producto in listado:
            producto['id_encoded'] = encode_id(producto['id'])

        # print(listado[0]['id_encoded'])
        
        return render.buscar(listado=listado)  # Pasar el listado obtenido de la búsqueda a la vista


def encode_id(id):
    # Codificar el ID como bytes, luego a Base64, y finalmente decodificar a una cadena para la URL
    encoded_id = base64.urlsafe_b64encode(str(id).encode()).decode()
    return encoded_id




 