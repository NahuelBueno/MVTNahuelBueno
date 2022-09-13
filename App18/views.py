from django.shortcuts import render
from django.http import HttpResponse
from App18.models import Familia
# Create your views here.


def familia(request):

    flia1 = Familia(nombre="Daniel", edad=55, dni=20175049)
    flia1.save()
    flia2 = Familia(nombre="Gabriela", edad=52, dni=20643292)
    flia2.save()
    flia3 = Familia(nombre="Nahuel", edad=25, dni=40554279)
    flia3.save()



    return HttpResponse("Primer integrante de mi familia {flia1.nombre} edad {flia1.edad} años  y dni: {flia1.dni}, El segundo integrante de mi familia")