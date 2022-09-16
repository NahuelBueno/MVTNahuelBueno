from fileinput import close
from django.shortcuts import render
from django.http import HttpResponse
from App18.models import Familia
from django.template import Template, Context
# Create your views here.


def familia(self):
    

    flia1 = Familia(nombre="Daniel", edad=55, dni=20175049)
    flia1.save()
    flia2 = Familia(nombre="Gabriela", edad=52, dni=20643292)
    flia2.save()
    flia3 = Familia(nombre="Nahuel", edad=25, dni=40554279)
    flia3.save()


    diccionario = "nombre", {flia1.nombre}, "edad", {flia1.edad}, "años",  "dni:", {flia1.dni}, "El segundo integrante de mi familia", {flia2.nombre}, "edad", {flia2.edad}, "años"   "dni:", {flia2.dni}, "El tercer integrante de mi familia ",{flia3.nombre}, "edad", {flia3.edad}, "años"  "dni:", {flia3.dni}
    
    miHtml = open(C:/Users/Nahuel Bueno/Desktop/Clase18/Entrega18/Entrega18/Plantillas/Template1.html)
    plantilla = Template(miHtml.read())
    miHtml.close
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)