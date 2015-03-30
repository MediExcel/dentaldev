import settings

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.core.urlresolvers import reverse 


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from Inventario.views import productoView, unidadView, busqueda, ingresarCantidad, detallesProd, EditProductView
from procesocoopago.views import pagos, aplicarpagoitem

from historialprocedimientos.views import create

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dental.views.home', name='home'),
    # url(r'^dental/', include('dental.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('ActividadesClinicas.urls')),

    url(r'^', include('paquete.urls')),
    url(r'^',include('altas.urls')),
    url(r'^',include('precios.urls')),
    url(r'^',include('bitacora.urls')),
    

    url(r'^cotizacion/', include('cotizacion.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'indexmhp'),

    url(r'^producto/$',productoView),
   
    url(r'^historialprocedimientos/$',create),
    url(r'^producto/unidad/$',unidadView),
    url(r'^producto/edit/(?P<pk>\d+)$',EditProductView.as_view(),name='producto-edit'),
    
    

    

    url(r'^ingresar/(?P<entrada_id>\d+)$',ingresarCantidad),
    url(r'^detalles_producto/(?P<entrada_id>\d+)$',detallesProd),
    url(r'^entradas/$', busqueda),

    #WSSSurl(r'^pago/$',Pago),
    #url(r'^pago/list/$',pagoupdate),
    url(r'^pago/list/$', pagos),
    url(r'^pago/process/$', aplicarpagoitem),


    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),

    #url(r'^prueba/$',busqueda),

    (r'^dajaxice/', include('dajaxice.urls')),
)


