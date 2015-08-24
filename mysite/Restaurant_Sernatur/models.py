from __future__ import unicode_literals

from django.db import models

class Region(models.Model):
    id = models.IntegerField(primary_key=True) 
    nom_reg = models.CharField(max_length=50)

		
class Provincia(models.Model):
	id_prov = models.IntegerField(primary_key=True)
	id_reg = models.ForeignKey('Region', db_column='id')
	nom_prov = models.CharField(max_length=50)
	

	  
class Comuna(models.Model):
	id_com = models.IntegerField(primary_key=True)
	id_prov = models.ForeignKey('Provincia', db_column='id_prov')
	nom_com = models.CharField(max_length=50)
	
	
	
class Restaurant(models.Model):
	id_rest = models.IntegerField(primary_key=True)
	id_com = models.ForeignKey('Comuna', db_column='id_com')
	nombre = models.CharField(max_length=50)
	numero = models.CharField(max_length=50)
	web = models.CharField(max_length=50)
    #rut = models.CharField(max_length=50)
	clase = models.CharField(max_length=50)
	fono = models.CharField(max_length=50)
	calle = models.CharField(max_length=50)
	
	
	
    

# Create your models here.


