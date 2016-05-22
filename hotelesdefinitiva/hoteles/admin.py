from django.contrib import admin
from models import Hotel
from models import Imagen
from models import Comentario
from models import ConfUsuario
from models import Elegidos

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Imagen)
admin.site.register(Comentario)
admin.site.register(ConfUsuario)
admin.site.register(Elegidos)

