from django.contrib import admin
from .models import Alojamento, AlojamentoViewsCount,ContactsSchedule
# Register your models here.

admin.site.register(Alojamento)
admin.site.register(AlojamentoViewsCount)
admin.site.register(ContactsSchedule)

