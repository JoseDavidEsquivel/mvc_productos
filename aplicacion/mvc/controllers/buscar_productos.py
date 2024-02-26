import web

render = web.template.render('mvc/views/', base='layout')

class Buscar:
    def GET(self):
        return render.buscar()
 