# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Documentos (models.Mode):
	edad = models.IntegerField(null=True, blank=True)
    fecha = models.DataTimefield(null=True, blank=True)
    def_unicode_(self):
       return 'Documento - {0}'.format(self.id)