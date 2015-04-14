from django import forms
import datetime as dt
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory, BaseFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from paquete.models import Paquete, PaqueteItem, PaqueteConsumido,\
PaqueteConsumidoItem
from Inventario.models import Producto
from crispy_forms.layout import(Layout, Fieldset, HTML, Field, ButtonHolder,\
Submit)

class PaqueteForm(forms.ModelForm):
	productos=forms.ModelMultipleChoiceField(queryset=Producto.objects.all())
	DEFAULT_PRODUCT_QUANTITY = 1

	class Meta:
		model=Paquete

	def __init__(self, *args, **kwargs):
		super(PaqueteForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper=FormHelper()
		self.helper.layout=Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>

							"""
			),
			Fieldset(
				'',

				# Field('paquete' , wrapper_class='col-md-2'),
				Field('nombre',wrapper_class='col-md-4'),
				Field('descripcion',wrapper_class='col-md-8'),				
				Field('productos' , wrapper_class='col-md-12'),

				# Field('cantidad_producto' , wrapper_class='col-md-2'),

				),
			ButtonHolder(
					Submit('save','Generar')

			)
		)
		self.fields['nombre'].label='Nombre'
		self.fields['descripcion'].label='Descripion'
		self.fields['productos'].label='Productos'
		# self.fields['cantidad_producto'].label='Cantidad'

	def save(self, commit=True):
		paquete = super(PaqueteForm,self).save(commit)
		items = self.save_to_items(paquete, commit)
		return (paquete, items)

	def save_to_items(self, paquete, commit=True):
		productos = self.cleaned_data.get('productos')
		items = []
		for producto in productos:
			item = PaqueteItem(
					paquete=paquete,
					producto=producto,
					cantidad_producto=self.DEFAULT_PRODUCT_QUANTITY
				)
			if commit:
				item.save()
			items.append(item)
		return items


class PaqueteConsumidoForm(forms.ModelForm):
	class Meta:
		model = PaqueteConsumido

	def __init__(self, *args, **kwargs):
		super(PaqueteConsumidoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		
		self.helper.layout = Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>

							"""
			),
			Fieldset(
				'',

				Field('paquete', wrapper_class='col-md-3'),
				Field('medico', wrapper_class='col-md-3'),
				Field('fecha', wrapper_class='col-md-3'),
				Field('paciente', wrapper_class='col-md-3'),


				),
			

			)
		
		# self.fields['paquete'].label = 'Paquete'
		self.fields['medico'].label = 'M&eacute;dico'
		# self.fields['paciente'].label = 'Paciente'
		
		self.fields['fecha'].initial = dt.datetime.now()

class PaqueteConsumidoIForm(forms.ModelForm):
	class Meta:
		model = PaqueteConsumidoItem

	def __init__(self, *args, **kwargs):
		super(PaqueteConsumidoIForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		
		self.helper.layout = Layout(
			HTML("""
							<p class="parrafo"> Campos con ( * ) Son Requeridos. </p>

							"""
			),
			Fieldset(
				'',

				Field('paquete_consumido', wrapper_class='col-md-3'),
				Field('tratamiento_pago', wrapper_class='col-md-2'),
				Field('producto', wrapper_class='col-md-3'),
				Field('cantidad', wrapper_class='col-md-2'),
				Field('precio', wrapper_class='col-md-2'),


				),
			ButtonHolder(
					Submit('save','Generar')
			

			)

			)
