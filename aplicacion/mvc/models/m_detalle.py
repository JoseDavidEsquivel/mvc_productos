import mysql.connector

class DetalleProductos:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mvc"
        )
        self.cursor = self.conn.cursor()

    def detalle_productos(self, id):
        # Construcción de la consulta SQL
        query = "SELECT * FROM productos WHERE id = %s"
        
        # Ejecutar la consulta
        self.cursor.execute(query, (id,))
        productos = self.cursor.fetchall()
        # Procesamiento de los resultados
        listado = []
        for row in productos:
            producto = {
                'id': row[0],
                'nombre': row[1],
                'descripcion': row[2],
                'precio': row[3],
                'existencias': row[4]
            }
            listado.append(producto)
        # Convertir a formato JSON
        return listado

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
