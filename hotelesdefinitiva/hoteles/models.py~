from django.db import models
from datetime import datetime

# Create your models here.
class Hotel (models.Model):
	hotel_id = models.CharField(max_length=10)
	nombre = models.CharField(max_length=32)
	email = models.CharField(max_length=50)
	telefono = models.CharField(max_length=40)
	cuerpo = models.TextField()
	web = models.CharField(max_length=150)
	address = models.CharField(max_length=32)
	pais = models.CharField(max_length=32)
	latitud = models.CharField(max_length=32)
	longitud= models.CharField(max_length=32)
	subAA = models.CharField(max_length=32)
	idTipo = models.CharField(max_length=32)
	Tipo = models.CharField(max_length=32)
	idCategoria = models.CharField(max_length=32)
	Categoria = models.CharField(max_length=32)
	idSubCategoria = models.CharField(max_length=32)
	subCategoria = models.CharField(max_length=32)
	NumComentarios = models.IntegerField(default=0)

class Imagen (models.Model):
	url = models.CharField(max_length=60)
	hotel_id = models.CharField(max_length=10)

class Comentario (models.Model):
	Cuerpo = models.TextField()
	hotel_id = models.CharField(max_length=10)

class ConfUsuario (models.Model):
	Titulopagina = models.CharField(max_length=150, default ="")
	Nombre = models.CharField(max_length=32)
	tama = models.CharField(max_length=32)
	fondo = models.CharField(max_length=32)
	hotel_id = models.CharField(max_length=10)

class Elegidos (models.Model):
	Nombre = models.CharField(max_length=32)
	Fecha = models.DateTimeField(default = datetime.now())
	hotel_id = models.CharField(max_length=10)




