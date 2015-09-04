from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .models import Region



def index(request):
	return render (request,"prueba.html")
	
def Tarapaca(request):
	return render (request,"tarapaca.html")
	
	
	

#def Antofagasta(request):
#	return render (request,"antofagasta.html")
	
class Antofagasta(TemplateView):
	template_name = 'antofagasta.html'
	
	
	
	
	
	
	
	
def Atacama(request):
	return render (request,"atacama.html")
	
def Coquimbo(request):
	return render (request,"coquimbo.html")
	
def Valparaiso(request):
	return render (request,"valparaiso.html")
	
def LiBerOH(request):
	return render (request,"liberoh.html")
	
def Maule(request):
	return render (request,"maule.html")
	
def Biobio(request):
	return render (request,"biobio.html")
	
def Araucania(request):
	return render (request,"araucania.html")
	
def Lagos(request):
	return render (request,"lagos.html")
	
def Aysen(request):
	return render (request,"aysen.html")
	
def Magallanes(request):
	return render (request,"magallanes.html")
	
def Metropolitana(request):
	return render (request,"metropolitana.html")
	
def Rios(request):
	return render (request,"rios.html")

def AricayPa(request):
	return render (request,"aricaparinacota.html")
	

class Reportar(ListView):
	model = Region
	template_name = 'listview.html'
	
	
	
	
	
	
	
	
