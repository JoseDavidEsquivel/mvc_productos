import web

render = web.template.render('mvc/views/')
   
class Detalle:
    def GET(self):
        return render.detalle()
 