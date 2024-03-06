import mysql.connector

class BorrarProductos:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mvc"
        )
        self.cursor = self.conn.cursor()

    def eliminar_producto(self, id):
        # Construcción de la consulta SQL para eliminar
        query = "DELETE FROM productos WHERE id = %s"
        # Ejecutar la consulta de eliminación
        self.cursor.execute(query, (id,))
        self.conn.commit()  # Asegurarse de confirmar los cambios en la base de datos
        resultado = {'exito': True, 'mensaje': f'Producto con id {id} eliminado correctamente.'}
        # except Exception as e:
        #     # En caso de error, hacer rollback y devolver mensaje de error
        #     self.connection.rollback()
        #     resultado = {'exito': False, 'mensaje': f'Error al eliminar producto con id {id}: {str(e)}'}
        
        # Devolver resultado de la operación
        return resultado


    def close_connection(self):
        self.cursor.close()
        self.conn.close()
