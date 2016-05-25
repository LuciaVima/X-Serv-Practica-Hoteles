from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'practicafinal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^cargar$', 'hoteles.views.cargar'),
    url(r'^about$', 'hoteles.views.about'),
    url(r'logout$', 'django.contrib.auth.views.logout'),
    url(r'^alojamientos$', 'hoteles.views.alojamientos'),
    url(r'^alojamientos/(\d+)', 'hoteles.views.alojamiento'),
    url(r'images/(.*)$', 'django.views.static.serve',
{'document_root': 'templates/images/'}),
    url(r'css/(.*)$', 'django.views.static.serve',
{'document_root': 'templates/css/'}),
    url(r'^$', 'hoteles.views.principal'),
    url(r'/?(.*)/XML$', 'hoteles.views.xml'),
    url(r'/?(.*)', 'hoteles.views.usuario'),
)
