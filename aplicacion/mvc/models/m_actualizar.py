import mysql.connector

class ActualizarProductos:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mvc"
        )
        self.cursor = self.conn.cursor()

    def actualizar_productos(self, id, nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension):

        valores = [nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension, id]
        query = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, existencias = %s, imagen_nombre = %s,imagen_extension = %s WHERE id = %s"

        self.cursor.execute(query, valores)
        mensaje = 'Producto actualizado correctamente'
        self.conn.commit()
        return mensaje


    def close_connection(self):
        self.cursor.close()
        self.conn.close()
