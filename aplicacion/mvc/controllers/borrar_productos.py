import web

render = web.template.render('mvc/views/')
   
class Borrar:
    def GET(self):
        return render.borrar()
 