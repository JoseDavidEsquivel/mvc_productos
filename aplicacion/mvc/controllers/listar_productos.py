# import web
# import sqlite3
# # from mvc.models.m_listar import ModeloProductos
# from pydantic import BaseModel

# conn = sqlite3.connect("sql/productos.db")

# class Producto(BaseModel):
#     id: int
#     nombre: str
#     descripcion: str
#     precio: int
#     existencias: int

# render = web.template.render('mvc/views/', base='layout')

# class Listar:
#     def GET(self):
#         """Lista los productos existentes, en un rango de 50 registros"""
#         c = conn.cursor()
#         c.execute('SELECT * FROM productos;')
#         response = []
#         for row in c.fetchall():
#             producto = Producto(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], existencias=row[4])
#             lista = {
#                 'id': row[0],
#                 'nombre': str(row[1]), 
#                 'descripcion': str(row[2]), 
#                 'precio': row[3], 
#                 'existencias': row[4]
#                 }
            
#             response.append(lista)
#             print(response)
#         return render.listar(response)

import web
from mvc.models.m_listar import ModeloProductos

render = web.template.render('mvc/views/', base='layout')

class Listar:
    def GET(self):
        producto_controller = ModeloProductos()
        productos = producto_controller.listar_productos()
        return render.listar(productos)
