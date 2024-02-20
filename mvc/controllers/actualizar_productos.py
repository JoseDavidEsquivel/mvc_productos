import web

render = web.template.render('mvc/views/')
   
class Actualizar:
    def GET(self):
        return render.actualizar()
 