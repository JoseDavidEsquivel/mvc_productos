import web

render = web.template.render('mvc/views/')
   
class Listar:
    def GET(self):
        return render.listar()
 