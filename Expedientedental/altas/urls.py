from django.conf.urls import patterns,url

urlpatterns = patterns('altas.views',
	
	url(r'^medicos/$','datosmedico_view',name= "datosmedico"),
	url(r'^pacientes/$','datospaciente_view',name= "datospaciente"),
)


