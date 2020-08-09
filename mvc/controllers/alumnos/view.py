''' 
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 19-07-2020
DESCRIPTION: Uso de la arquitectura MVC. Formulario HTML5, haciendo uso de Bulma y Web.py, muestra los archivos insertados en list.html
'''

import web # IMPORTACCION DE WEB.

import mvc.models.model as model

model_alumnos = model.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class View():
    
    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
            return render.view(result) # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.
