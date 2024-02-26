import web
# import sqlite3
# from pydantic import BaseModel

# conn = sqlite3.connect("sql/productos.db")

# class Producto(BaseModel):
#     id: int
#     nombre: str
#     descripcion: str
#     precio: int
#     existencias: int

# class ModeloProductos:
#     async def __init__(self):
#         """Lista los productos existentes, en un rango de 50 registros"""
#         c = conn.cursor()
#         c.execute('SELECT * FROM productos;')
#         response = []
#         for row in c.fetchall():
#             producto = Producto(id=row[0], nombre=row[1], descripcion=row[2], precio=row[3], existencias=row[4])
#             response.append(producto)
#         self.lista = response
#         await self.lista

class ModeloProductos:
    def __init__(self):
        self.lista = [
            {
                'id': 1,
                'nombre': 'Laptop Intel', 
                'descripcion': 'Laptop potente', 
                'precio': 1500, 
                'existencias': 30
            },
            {
                'id': 1,
                'nombre': 'Laptop Intel', 
                'descripcion': 'Laptop potente', 
                'precio': 1500, 
                'existencias': 30
            },
            {
                'id': 1,
                'nombre': 'Laptop Intel', 
                'descripcion': 'Laptop potente', 
                'precio': 1500, 
                'existencias': 30
            },
            {
                'id': 1,
                'nombre': 'Laptop Intel', 
                'descripcion': 'Laptop potente', 
                'precio': 1500, 
                'existencias': 30
            },
        ]
            