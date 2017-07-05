# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.shortcuts import render
from documentos.models import Documentos as ModeloDocumentos


class Documentos(View):
    def get(self, request, *args, **kwargs):
        docs = ModeloDocumentos.objects.all()
        context = {
        'docs':docs,
        'encabezado':'Mis documentos'
        }
        return render(
        	request,
            'documento.html',
            context) 