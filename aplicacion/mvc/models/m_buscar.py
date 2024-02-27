import mysql.connector

class BuscarProductos:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mvc"
        )
        self.cursor = self.conn.cursor()

    def buscar_productos(self, id, nombre, descripcion, precio, existencias):
        # Modificacion de las variables nombre y descripcion para que puedan buscar parecidos en vez de buscar el valor exacto
        if nombre != "":
            nombre = f"%{nombre}%"

        if descripcion != "":
            descripcion = f"%{descripcion}%"

        # Comprobación de valores nulos y preparación de valores para la consulta
        valores = [id,nombre, descripcion, precio, existencias]

        for i in range(len(valores)):
            if valores[i] == "":
                valores[i] = "%"  # Reemplaza los valores nulos por "%"

        print(valores)

        # Construcción de la consulta SQL
        query = "SELECT * FROM productos WHERE id LIKE %s AND nombre LIKE %s  AND descripcion LIKE %s AND precio LIKE %s AND existencias LIKE %s LIMIT 25"
        
        # Ejecutar la consulta
        self.cursor.execute(query, valores)
        productos = self.cursor.fetchall()

        # Procesamiento de los resultados
        listado = []
        for row in productos:
            temp_descripcion = row[2]
            descripcion_trunca = temp_descripcion[:50]
            producto = {
                'id': row[0],
                'nombre': row[1],
                'descripcion': descripcion_trunca,
                'precio': row[3],
                'existencias': row[4]
            }
            listado.append(producto)
        print(listado)
        # Convertir a formato JSON
        return listado



    def close_connection(self):
        self.cursor.close()
        self.conn.close()
