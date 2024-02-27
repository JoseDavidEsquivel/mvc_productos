import mysql.connector

class InsertarProductos:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mvc"
        )
        self.cursor = self.conn.cursor()

    def insertar_productos(self, nombre, descripcion, precio, existencias):

        valores = [nombre, descripcion, precio, existencias]

        # Construcción de la consulta SQL
        query = "INSERT INTO productos (nombre, descripcion, precio, existencias) VALUES (%s , %s , %s , %s)"

        # Ejecutar la consulta
        self.cursor.execute(query, valores)
        mensaje = 'Producto añadido correctamente'
        self.conn.commit()
        return mensaje

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
