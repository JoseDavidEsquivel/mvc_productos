# import web
# from mvc.models.m_listar import ModeloProductos

# render = web.template.render('mvc/views/', base='layout')

# class Listar:
#     def GET(self):
#         producto_controller = ModeloProductos()
#         productos = producto_controller.listar_productos()
#         return render.listar(productos)

import web
from mvc.models.m_listar import ModeloProductos

render = web.template.render('mvc/views/', base='layout')

class Listar:
    def GET(self):
        i = web.input(page=1)
        page = int(i.page)
        producto_controller = ModeloProductos()
        productos = producto_controller.listar_productos(page)
        return render.listar(productos, page=page)
