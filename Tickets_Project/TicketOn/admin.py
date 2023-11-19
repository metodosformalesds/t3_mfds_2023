from django.contrib import admin
from .models import *

class EventoAdmin(admin.ModelAdmin):
    readonly_fields=("slug",)

admin.site.register(Comprador)
admin.site.register(Organizador)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Ticket)
admin.site.register(Transferencia)
admin.site.register(Carrito)