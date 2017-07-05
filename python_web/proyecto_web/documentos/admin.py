# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from documentos.models import Documentos


class DocumentoAdmin(admin.ModelAdmin):
    model = Documentos


admin.site.register(Documentos, DocumentoAdmin)

