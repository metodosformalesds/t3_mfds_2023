from django.contrib import admin
from .models import Comprador
from .models import Organizador
from .models import Evento
from .models import Ticket
from .models import Transferencia

class EventoAdmin(admin.ModelAdmin):
    readonly_fields=("slug",)

admin.site.register(Comprador)
admin.site.register(Organizador)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Ticket)
admin.site.register(Transferencia)