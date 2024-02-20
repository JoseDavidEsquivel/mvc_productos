import web

render = web.template.render('mvc/views/')
   
class Insertar:
    def GET(self):
        return render.insertar()
 