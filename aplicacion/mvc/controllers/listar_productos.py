import web

render = web.template.render('mvc/views/', base='layout')
   
class Listar:
    def GET(self):
        return render.listar()
 