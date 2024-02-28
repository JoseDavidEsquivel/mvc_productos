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

    def actualizar_productos(self, id, nombre, descripcion, precio, existencias):
        # Incluir el id en los valores, al final, porque se usará en la cláusula WHERE
        valores = [nombre, descripcion, precio, existencias, id]

        # Construcción de la consulta SQL para actualizar
        query = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, existencias = %s WHERE id = %s"

        # Ejecutar la consulta
        self.cursor.execute(query, valores)
        mensaje = 'Producto actualizado correctamente'
        self.conn.commit()
        return mensaje


    def close_connection(self):
        self.cursor.close()
        self.conn.close()
