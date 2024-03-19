import web
from mvc.models.m_listar import ModeloProductos
import base64

render = web.template.render('mvc/views/', base='layout')

class Listar:
    def GET(self):
        i = web.input(page=1)
        page = int(i.page)
        producto_controller = ModeloProductos()
        productos = producto_controller.listar_productos(page)

        # Codificar los IDs antes de pasarlos a la vista
        for producto in productos:
            producto['id_encoded'] = encode_id(producto['id'])
        
        return render.listar(productos, page=page)

def encode_id(id):
    # Codificar el ID como bytes, luego a Base64, y finalmente decodificar a una cadena para la URL
    encoded_id = base64.urlsafe_b64encode(str(id).encode()).decode()
    return encoded_id
