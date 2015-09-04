"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from Restaurant_Sernatur.views import Antofagasta
from Restaurant_Sernatur.views import Reportar




urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'Restaurant_Sernatur.views.index'),
	
	url(r'^antofagasta',Antofagasta.as_view()),
	
	url(r'^reportar',Reportar.as_view()),
	
	
	

	# url(r'^tarapaca', 'Restaurant_Sernatur.views.Tarapaca'),
	# #url(r'^antofagasta',Antofagasta.as_view()),
	# url(r'^atacama', 'Restaurant_Sernatur.views.Atacama'),
	# url(r'^coquimbo', 'Restaurant_Sernatur.views.Coquimbo'),
	# url(r'^valparaiso', 'Restaurant_Sernatur.views.Valparaiso'),
	# url(r'^libertador', 'Restaurant_Sernatur.views.LiBerOH'),
	# url(r'^maule', 'Restaurant_Sernatur.views.Maule'),
	# url(r'^biobio', 'Restaurant_Sernatur.views.Biobio'),
	# url(r'^araucania', 'Restaurant_Sernatur.views.Araucania'),
	# url(r'^lagos', 'Restaurant_Sernatur.views.Lagos'),
	# url(r'^aysen', 'Restaurant_Sernatur.views.Aysen'),
	# url(r'^magallanes', 'Restaurant_Sernatur.views.Magallanes'),
	# url(r'^metropolitana', 'Restaurant_Sernatur.views.Metropolitana'),
	# url(r'^rios', 'Restaurant_Sernatur.views.Rios'),
	# url(r'^AricayPa', 'Restaurant_Sernatur.views.AricayPa'),
	# #url(r'^reportar/$', Restaurant.views.ReportarRest.as_view(), name='rest-list'),
	#url(r'^', include('mysite\Restaurant_Sernatur\urls')),
	
	
	
]
