# Framework web.py
import web

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.listar_productos.Listar',
    '/insertar', 'mvc.controllers.insertar_productos.Insertar',
    '/actualizar', 'mvc.controllers.actualizar_productos.Actualizar',
    '/borrar', 'mvc.controllers.borrar_productos.Borrar',
    '/detalle', 'mvc.controllers.detalle_productos.Detalle',
    '/documentacion', 'mvc.controllers.documentacion.Documentacion',
    '/buscar', 'mvc.controllers.buscar_productos.Buscar'
    )

app = web.application(urls, globals())

# Punto de Entrada
if __name__ == "__main__":
    web.config.debug = False
    app.run()