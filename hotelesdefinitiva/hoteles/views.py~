from django.http import HttpResponse
from django.shortcuts import render
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from django.contrib import auth
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import sys
import string
import urllib2
from datetime import datetime 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from urllib2 import urlopen
from models import Hotel
from models import Imagen
from models import Comentario
from models import ConfUsuario
from models import Elegidos
from operator import itemgetter
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def normalize_whitespace(text):
	"Remove redundant whitespace from a string"
	return string.join(string.split(text), ' ')

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
	self.dict = {}
	self.lista_hoteles = []

    def dameLista(self):
	return self.lista_hoteles


    def startElement (self, name, attrs):
        if name == 'service':
	    self.id = attrs.get('id')
	    self.dict['id'] = self.id 
            self.inItem = True
        elif self.inItem:
	    if name =='language':
		self.inContent = True
            if name == 'name':
                self.inContent = True
	    elif name == 'email':
		self.inContent = True
            elif name == 'phone':
                self.inContent = True
	    elif name == 'body':
		self.inContent = True
	    elif name == 'web':
		self.inContent = True
	    elif name == 'address':
		self.inContent = True
	    elif name == 'country':
		self.inContent = True
	    elif name == 'latitude':
		self.inContent = True
	    elif name == 'longitude':
		self.inContent = True
	    elif name == 'subAdministrativeArea':
		self.inContent = True
	    elif name == 'item': 
		self.tipo = normalize_whitespace(attrs.get('name'))		
		self.inContent = True
	    elif name == 'url':
		self.inContent = True
	    
            
    def endElement (self, name):
        if name == 'service':
		self.lista_hoteles.append(self.dict)
		self.dict={}
                self.inItem = False
        elif self.inItem:
            if name == 'name':
                self.nombre = self.theContent
		self.dict['nombre'] = self.theContent
                #print line.encode('utf-8') 
                self.inContent = False
                self.theContent = ""
	    elif name == 'language':
		self.languaje = self.theContent
		self.dict['languaje'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'email':
		self.email = self.theContent
		self.dict['email'] = self.theContent
                self.inContent = False
                self.theContent = ""
            elif name == 'phone':
		self.telefono = self.theContent
		self.dict['telefono'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'body':
		self.cuerpo = self.theContent
		self.dict['cuerpo'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'web':
		self.web = self.theContent
		self.dict['web'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'address':
		self.address = self.theContent
		self.dict['address'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'country':
		self.pais = self.theContent
		self.dict['pais'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'latitude':
		self.latitud = self.theContent
		self.dict['latitude'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'longitude':
		self.longitud = self.theContent
		self.dict['longitude'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'subAdministrativeArea':
		self.subAA = self.theContent
		self.dict['subAdministrativeArea'] = self.theContent
                self.inContent = False
                self.theContent = ""
	    elif name == 'url':
		self.url = self.theContent
		#self.dict['url'] = self.theContent
		if self.languaje == 'es':
			imagen = Imagen(url = self.url, hotel_id = self.id)
			imagen.save()
			self.inContent = False
               		self.theContent = ""
		else:
                	self.inContent = False
               	 	self.theContent = ""
	    elif name == 'item':
		if self.tipo == 'idTipo':
			self.idTipo = self.theContent
			self.dict['idTipo'] = self.theContent
		elif self.tipo == 'Tipo':
			self.Tipo = self.theContent
			self.dict['Tipo'] = self.theContent
		elif self.tipo == 'idCategoria':
			self.idCategoria = self.theContent
			self.dict['idCategoria'] = self.theContent
		elif self.tipo == 'Categoria':
			self.Categoria = self.theContent
			self.dict['Categoria'] = self.theContent
		elif self.tipo == 'idSubCategoria':
			self.idSubCategoria = self.theContent
			self.dict['idSubCategoria'] = self.theContent
		elif self.tipo == 'SubCategoria':
			self.SubCategoria = self.theContent
			self.dict['SubCategoria'] = self.theContent	
                self.inContent = False
                self.theContent = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


def cargar(request):
#ESTA COMPLETA
	# Load parser and driver
	theParser = make_parser()
	theHandler = myContentHandler()
	theParser.setContentHandler(theHandler)
	
	# Ready, set, go!
	url = ("http://cursosweb.github.io/etc/alojamientos_es.xml")
	xmlFile = urlopen(url)
	#xmlFile = open('/home/lucia/alojamientos_es.xml')
	theParser.parse(xmlFile)
	lista = theHandler.dameLista()
	for dic in lista:
		h = Hotel(hotel_id = dic["id"], nombre = dic["nombre"], email = dic["email"], telefono = dic["telefono"], cuerpo = dic["cuerpo"], web = dic["web"], address = dic["address"], pais = dic["pais"], latitud = dic["latitude"], longitud= dic["longitude"], subAA = dic["subAdministrativeArea"], idTipo = dic["idTipo"], Tipo = dic["Tipo"], idCategoria = dic["idCategoria"], Categoria = dic["Categoria"], idSubCategoria = dic["idSubCategoria"], subCategoria = dic["SubCategoria"], NumComentarios = 0)
		h.save()
	
	respuesta = 'Archivos guardados correctamente'

	
	template = get_template('cargar.html')
	Context = RequestContext(request, {'respuesta': respuesta})
	return HttpResponse(template.render(Context))


@csrf_exempt
def principal(request):
	hoteles = Hotel.objects.all()
	imagenes = Imagen.objects.all()
	comentarios = Comentario.objects.all()
	dict = {}
	puesto = False
	
	listahotelesordenada = []
	indice = 0
	for hotel in hoteles:
		NumComentarios = 0
		for comentario in comentarios:
			if comentario.hotel_id == hotel.hotel_id:
				NumComentarios = NumComentarios + 1
				dict[hotel.hotel_id] = NumComentarios
	
	listahotelesordenada = sorted(dict.items(), key = itemgetter(1), reverse = True)
	if len(listahotelesordenada) > 10:
		listahotelesordenada=listahotelesordenada[0:10]
	listaparaenviar=[]
	listadefinitiva=[]

	for indice in range(len(listahotelesordenada)):
		for hotel in hoteles:
			if hotel.hotel_id == listahotelesordenada[indice][0]:
				for imagen in imagenes:
					if ((imagen.hotel_id == listahotelesordenada[indice][0]) and (puesto == False)) :
						listaparaenviar.append((hotel, imagen))
						puesto = True
		puesto = False
	indice = indice + 1
	usuarios = User.objects.all()
	confusus = ConfUsuario.objects.all()
	listausuarios=[]
	for usu in usuarios:
		puesto=False
		configuracion = False
		for confusu in confusus:
			if str(usu) == confusu.Nombre:
				configuracion = True
				puesto = True
				titulo = confusu.Titulopagina
				listausuarios.append((usu, configuracion, titulo))
						
		if puesto == False:
			configuracion = False
			titulo = 'Pagina de'
			listausuarios.append((usu, configuracion, titulo))
	if request.user.is_authenticated():
		usuarioautenticado = True
		usuarioactual = request.user.username
	else:
		usuarioautenticado = False
		usuarioactual = ''
	
	if request.method == 'POST':
		camponombre = request.body.split("&")[0]
		campopass = request.body.split("&")[1]
		name = camponombre.split("=")[1]
		passw = campopass.split("=")[1]
		user = auth.authenticate(username = name, password = passw)
		if user is not None:
			auth.login(request, user)
			usuarioautenticado= True
			usuarioactual = user.username


	listadefinitiva.append((listaparaenviar,listausuarios, usuarioautenticado, usuarioactual))	
	template = get_template('index.html')
	Context = RequestContext(request, {'lista': listadefinitiva})
	return HttpResponse(template.render(Context))

@csrf_exempt
def alojamientos(request):
	hoteles = Hotel.objects.all()
	listadehoteles = []
	if request.method == 'GET':
		for hotel in hoteles:
			listadehoteles.append(hotel)
	elif request.method == 'POST' or request.method == 'PUT':
		cuerpo1 = request.body.split("&")[0]
		cuerpo2 = request.body.split("&")[1]
		categoria = cuerpo1.split("=")[1]
		subcategoria = cuerpo2.split("=")[1]
		subcategoria = subcategoria.split("+")[0] + " estrellas"
		for hotel in hoteles:
			if (hotel.Categoria == categoria and len(categoria) != 0 and hotel.subCategoria == subcategoria and len(subcategoria) != 10):
				listadehoteles.append(hotel)
			elif hotel.subCategoria == subcategoria and len(categoria) == 0:
				listadehoteles.append(hotel)
			elif hotel.Categoria == categoria and len(subcategoria) == 10:
				listadehoteles.append(hotel)
		
		
	template = get_template('alojamientos.html')
	Context = RequestContext(request, {'lista': listadehoteles})
	return HttpResponse(template.render(Context))

@csrf_exempt
def alojamiento (request, indice):
	encontrado = False
	hoteles = Hotel.objects.all()
	imagenes = Imagen.objects.all()
	comentarios = Comentario.objects.all()
	listafinal = []
	listaimagenes = []
	listacomentarios = []
	listaparaenviar = []
	listahoteles = []
	autenticado = False
	for hotel in hoteles:	
		if (hotel.hotel_id == indice) :
			totalimagenes = 0
			indicecomentario = 1
			encontrado = True
			for imagen in imagenes:
				if ((imagen.hotel_id == hotel.hotel_id) and (totalimagenes < 5)):
					totalimagenes = totalimagenes + 1
					listaimagenes.append(imagen)
			for comentario in comentarios:
				if (comentario.hotel_id == hotel.hotel_id):
					try:
						comentario = comentario.Cuerpo.split("=")[1]
						buscar = '+'
						reemplazar = ' ' 
						comentario = comentario.replace(buscar,reemplazar)
						listacomentarios.append(comentario)
						indicecomentario = indicecomentario + 1
					except IndexError:
						listacomentarios.append(comentario.Cuerpo)
						indicecomentario = indicecomentario + 1
			listahoteles.append(hotel)
			
	if request.user.is_authenticated() and encontrado == True:
		autenticado = True

	if request.method == 'POST':
		comentario = request.body
		if (comentario.split("=")[0] == 'mibotondeopcion'):
			if comentario.split("=")[1] == 'Ingl':
				theParser = make_parser()
				theHandler = myContentHandler()
				theParser.setContentHandler(theHandler)
				url = ("http://cursosweb.github.io/etc/alojamientos_en.xml")
				xmlFile = urlopen(url)
				theParser.parse(xmlFile)
				lista = theHandler.dameLista()
				for dic in lista:
					h = Hotel(hotel_id = dic["id"], nombre = dic["nombre"], email = dic["email"], telefono = dic["telefono"], cuerpo = dic["cuerpo"], web = dic["web"], address = dic["address"], pais = dic["pais"], latitud = dic["latitude"], longitud= dic["longitude"], subAA = dic["subAdministrativeArea"], idTipo = dic["idTipo"], Tipo = dic["Tipo"], idCategoria = dic["idCategoria"], Categoria = dic["Categoria"], idSubCategoria = dic["idSubCategoria"], subCategoria = dic["SubCategoria"], NumComentarios = 0)

					if (h.hotel_id == indice):
						listahoteles.append(h)

			elif comentario.split("=")[1] == 'Fran':
				theParser = make_parser()
				theHandler = myContentHandler()
				theParser.setContentHandler(theHandler)
				url = ("http://cursosweb.github.io/etc/alojamientos_fr.xml")
				xmlFile = urlopen(url)
				theParser.parse(xmlFile)
				lista = theHandler.dameLista()
				for dic in lista:
					h = Hotel(hotel_id = dic["id"], nombre = dic["nombre"], email = dic["email"], telefono = dic["telefono"], cuerpo = dic["cuerpo"], web = dic["web"], address = dic["address"], pais = dic["pais"], latitud = dic["latitude"], longitud= dic["longitude"], subAA = dic["subAdministrativeArea"], idTipo = dic["idTipo"], Tipo = dic["Tipo"], idCategoria = dic["idCategoria"], Categoria = dic["Categoria"], idSubCategoria = dic["idSubCategoria"], subCategoria = dic["SubCategoria"], NumComentarios = 0)
					if (h.hotel_id == indice):
						listahoteles.append(h)
				
			else:
				respuesta = respuesta						
		elif (comentario.split("=")[0] == 'seleccion'):
			ahora = datetime.now()
			u = Elegidos(Nombre = request.user.username,Fecha = ahora, hotel_id = indice)
			u.save()
		
		else:
			for hotel in hoteles:
				if (hotel.hotel_id == indice) :
					comentario = request.body.split("=")[1]
					buscar = '+'
					reemplazar = ' ' 
					comentario = comentario.replace(buscar,reemplazar) 
					c = Comentario(Cuerpo = comentario, hotel_id = indice)
					c.save()
					hotel.NumComentarios = hotel.NumComentarios + 1
					listacomentarios.append(comentario)
		

	listafinal.append((listahoteles, listaimagenes, listacomentarios))
	listaparaenviar.append((listafinal, autenticado))
	template = get_template('alojamiento.html')
	Context = RequestContext(request,{'lista': listaparaenviar})
	return HttpResponse(template.render(Context))

@csrf_exempt
def usuario (request, nombre):
	encontradousuario = False
	puesto = False
	elegidos = Elegidos.objects.all()
	hoteles = Hotel.objects.all()
	imagenes = Imagen.objects.all()
	usuarios = ConfUsuario.objects.all()
	usuarioautenticado = False
	selecciono = False
	colorazul = False
	colorrosa=False
	colorgris=False
	listaparaenviar = []
	listaconf = []
	listafinal = []
	for elegido in elegidos:
		if elegido.Nombre == nombre:
			encontradousuario = True
			for hotel in hoteles:
				puesto = False
				if elegido.hotel_id == hotel.hotel_id:
					for imagen in imagenes:
						if ((imagen.hotel_id == hotel.hotel_id) and (puesto == False)):
							listaparaenviar.append((hotel, imagen, elegido))
							puesto = True
						
	if request.user.is_authenticated():
		usuarioautenticado = True
		if request.method == 'POST' or request.method == 'PUT':
			usus = ConfUsuario.objects.all()
			encontrado = False
			encontrado2=False
			encontrado3=False
			
			
			for usu in usuarios:
			   if request.user.username == usu.Nombre:
				resp = request.body.split("=")[0]
				if  resp == 'titulo':
					encontrado2=True
					titulonuevo = request.body.split("=")[1]
					buscar = '+'
					reemplazar = ' ' 
					titulonuevo = titulonuevo.replace(buscar,reemplazar)
					if usu.Nombre == nombre:
						usu.Titulopagina = titulonuevo
						usu.save()
						encontrado = True
						
				else:
					selecciono = True
					opcionelegida = request.body.split("=")[1]
					if usu.Nombre == nombre:
						if (opcionelegida == 'Defecto'):
							usu.tama = 10
							usu.fondo = 'azul'
							usu.save()
							encontrado2 = True
						if (opcionelegida == 'Segundo'):
							usu.tama = 8
							usu.fondo = 'gris'
							usu.save()
							encontrado2 = True
						if (opcionelegida == 'Tercero'):
							usu.tama = 10
							usu.fondo = 'rosa'
							usu.save()
							encontrado2 = True
						

			if encontrado == False:
			    if request.user.username == usu.Nombre:
				usu = ConfUsuario(Titulopagina = titulonuevo, Nombre = nombre, tama = '',	fondo = '')
				usu.save()
			elif encontrado2 == False:
			    if request.user.username == usu.Nombre:
				titulo = 'Pagina de ' + nombre
				if (opcion == defecto):
					usu = ConfUsuario(Titulopagina = titulo, Nombre = nombre, tama = 10, fondo = 'azul')
					usu.save()
				if (opcion == Segundo):
					usu = ConfUsuario(Titulopagina = titulo, Nombre = nombre, tama = 8, fondo = 'gris')
					usu.save()
				if (opcion == Tercero):
					usu = ConfUsuario(Titulopagina = titulo, Nombre = nombre, tama = 10, fondo = 'rosa')
					usu.save()

	for usu in usuarios:
		if request.user.username == usu.Nombre:	
			if (usu.fondo == 'azul'):
				colorazul = True
				colorrosa = False
				colorgris = False
			if (usu.fondo == 'gris'):
				colorazul = False
				colorrosa = False
				colorgris = True
			if (usu.fondo == 'rosa'):
				colorazul = False
				colorrosa = True
				colorgris = False
			listafinal.append((listaparaenviar, usuarioautenticado, nombre, colorazul, colorrosa, colorgris))

	template = get_template('usuario.html')
	Context = RequestContext(request,{'lista': listafinal})
	return HttpResponse(template.render(Context)) 



def about(request):
	respuesta = "Esta practica pertenece a Lucia Villa Martinez y sirve para buscar hoteles, seleccionarlos y poner comentarios sobre ellos."

	template = get_template('about.html')
	Context = RequestContext(request,{'respuesta': respuesta})
	return HttpResponse(template.render(Context)) 



def xml (request, nombre):
	respuesta = ''
	usuarios = ConfUsuario.objects.all()
	elegidos = Elegidos.objects.all()
	imagenes = Imagen.objects.all()
	hoteles = Hotel.objects.all()
	lista = []
	respuesta = '<?xml version="1.0" encoding="UTF-8"?>'
	lista.append(respuesta)
	respuesta = 'serviceList</br>'
	lista.append(respuesta)
	for elegido in elegidos:
		if elegido.Nombre == nombre:
			encontradousuario = True
			for hotel in hoteles:
				puesto = False
				if elegido.hotel_id == hotel.hotel_id:
					for imagen in imagenes:
						if ((imagen.hotel_id == hotel.hotel_id) and (puesto == False)):
							puesto = True
							respuesta = '<service>'
							lista.append(respuesta)
							respuesta = '	<hotel>'
							lista.append(respuesta)
						        respuesta = '<name> ' +hotel.nombre + '</name>'
							lista.append(respuesta)
							respuesta = '	<url> ' +hotel.web + '</url>'
							lista.append(respuesta)
							respuesta = '	<localizacion> ' +hotel.address + '</localizacion>'
							lista.append(respuesta)
							respuesta = '	<fecha> ' +str(elegido.Fecha) + '</fecha> '
							lista.append(respuesta)
							respuesta = '	<imagenurl> ' +imagen.url + '</imagenurl>'
							lista.append(respuesta)
							respuesta = '</service>'
							lista.append(respuesta)
		
	
	template = get_template('xml.html')
	Context = RequestContext(request,{'lista': lista})
	return HttpResponse(template.render(Context)) 
	


