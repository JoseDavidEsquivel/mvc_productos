import web

render = web.template.render('mvc/views/', base='layout')
   
class Documentacion:
    def GET(self):
        return render.documentacion()
 