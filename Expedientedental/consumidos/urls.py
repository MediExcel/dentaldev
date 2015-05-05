from django.conf.urls import patterns, url
from consumidos.views import EditPaqueteView, paquetec, Pending, manage_paquetes

urlpatterns = patterns(
    'consumidos.views',

    url(r'^pendientes/$', Pending.as_view()),
    url(r'^tipoPaquete/$', 'paquete_item'),
    url(r'^paquetes/$', paquetec),
    url(r'^paquetes/insumos/(?P<pk>\d+)/$', manage_paquetes, name='insumos'),
    url(r'^tipoPaquete/edit/(?P<pk>\d+)$', EditPaqueteView.as_view()),

)

urlpatterns += patterns(
    '',
    # Reportes PDF
    # url(r'^paquetes/pdf/$',PaquetesPDF.as_view()),
)
