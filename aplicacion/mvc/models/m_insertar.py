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

    def insertar_productos(self, nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension):
        valores = [nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension]
        query = "INSERT INTO productos (nombre, descripcion, precio, existencias, imagen_nombre, imagen_extension) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, valores)
        mensaje = 'Producto añadido correctamente'
        self.conn.commit()
        return mensaje

    def obtener_ultimo_id(self):
        self.cursor.execute("SELECT id FROM productos ORDER BY id DESC LIMIT 1")
        last_id = self.cursor.fetchone()
        if last_id:
            return last_id[0]
        else:
            return 0


    def close_connection(self):
        self.cursor.close()
        self.conn.close()
