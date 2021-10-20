from django.contrib import admin
from .models import Plant, Medico, Persona


# Register your models here.
admin.site.register(Plant)


class PersonaAdmin(admin.ModelAdmin):
    using = 'otraBase'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)


admin.site.register(Persona, PersonaAdmin)


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'especialidad', 'telefono')
    search_fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'especialidad', 'telefono')

admin.site.register(Medico, MedicoAdmin)
