from django.contrib import admin
from .models import *

# Register your models here.
class AuditAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class InfoAcademicaInline(admin.TabularInline):
    readonly_fields = ('created', 'updated')
    model = InfoAcademica

class ExperienciaLaboralInline(admin.TabularInline):
    readonly_fields = ('created', 'updated')
    model = ExperienciaLaboral

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('documento', 'tipo_documento',  'nombre', 'cargo', 'fecha_ingreso', 'display_salario')
    list_filter = ('estado',)
    fieldsets = (
        ('Información personal', {
            'fields': (('tipo_documento', 'documento'),'nombre', 'sexo', 'nacionalidad', 'fecha_nacimiento','estado_civil', ('libreta_militar', 'distrito_militar', 'numero_libreta'), ('direccion_residencia', 'estrato'), ('departamento', 'ciudad'), ('telefono', 'celular'), 'correo')
        }),
        ('Información de nómina', {
            'fields': ('fecha_ingreso', 'cargo', 'salario', ('sede', 'area', 'seccion'), 'estado')
        }),
        ('Seguridad social', {
            'fields': ('eps', 'afp', 'caja', 'arl', ('rh', 'grupo_rh'))
        }),
        ('Persona contacto', {
            'fields': ('persona_contacto', 'celuar_contacto', 'coreeo_contacto')
        }),
    )
    inlines = [InfoAcademicaInline, ExperienciaLaboralInline]
    search_fields = ['nombre', 'documento', ]


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Pais, AuditAdmin)
admin.site.register(Departamento, AuditAdmin)
admin.site.register(Ciudad, AuditAdmin)
admin.site.register(Sede, AuditAdmin)
admin.site.register(Seccion, AuditAdmin)
admin.site.register(Area, AuditAdmin)
admin.site.register(Cargo, AuditAdmin)
admin.site.register(Afp, AuditAdmin)
admin.site.register(Arl, AuditAdmin)
admin.site.register(Eps, AuditAdmin)
admin.site.register(CajaCompensacion, AuditAdmin)
admin.site.register(MotivoAusentismo, AuditAdmin)
admin.site.register(Ausentismo, AuditAdmin)



