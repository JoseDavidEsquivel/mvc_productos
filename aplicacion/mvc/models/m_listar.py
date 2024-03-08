
import mysql.connector

class ModeloProductos:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mvc"
        )
        self.cursor = self.conn.cursor()

    def listar_productos(self, page):
        offset = (page - 1) * 25
        self.cursor.execute("SELECT * FROM productos LIMIT 25 OFFSET %s", (offset,))
        productos = self.cursor.fetchall()

        response = []
        for row in productos:
            temp_descripcion = row[2]
            descripcion_trunca = temp_descripcion[:100]
            producto = {
                'id': row[0],
                'nombre': row[1],
                'descripcion': descripcion_trunca,
                'precio': row[3],
                'existencias': row[4]
            }
            response.append(producto)
        # Convertir a formato JSON
        productos_json = response
        return productos_json

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
