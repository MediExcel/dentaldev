# -*- encoding: utf-8 -*-
from django.db import models
from altas.models import Medico, Paciente

from core.models import CancelledModel


class Paquete(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return'%s' % (self.nombre)


class PaqueteItem(models.Model):
    paquete = models.ForeignKey(Paquete)
    producto = models.ForeignKey('inventario.Producto')
    cantidad_producto = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return '%s' % (self.paquete)


class PaqueteConsumido(models.Model):
    paquete = models.ForeignKey(Paquete, null=True)
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    servicio = models.ForeignKey('servicios.Servicio', null=True)
    fecha = models.DateTimeField()
    nota = models.TextField(blank=True)
    status = models.CharField(max_length=1, blank=True, default='En Espera',
                              choices=(('En Espera', 'En Espera'), ('Completado', 'Entregado')))

    def __unicode__(self):
        return '%s %s' % (self.paquete, self.medico)

    def get_item_initials(self):
        paquete = self.paquete
        paquete_items = paquete.paqueteitem_set.all()
        initial_list = []
        for pitem in paquete_items:
            initial = {
                'paquete_consumido': self,
                'producto': pitem.producto,
                'cantidad': pitem.cantidad_producto,
                'precio': pitem.producto.precioUnidad
            }
            initial_list.append(initial)
        return initial_list


class PaqueteConsumidoItem(models.Model):
    paquete_consumido = models.ForeignKey(PaqueteConsumido)
    producto = models.ForeignKey('inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return u'%s %s %s ' % (self.producto, self.cantidad, self.precio)


class ProductoConsumido(models.Model):
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    producto = models.ForeignKey('inventario.Producto')
    cantidad = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s %s' % (
            self.producto, self.cantidad, self.cantidad)


class CancelPC(CancelledModel):
    '''
    Herencia de modelo en core.
    Agrego relacion del producto.
    '''
    pconsumido = models.ForeignKey(ProductoConsumido)

    def __unicode__(self):
        return '%s' % self.reason
