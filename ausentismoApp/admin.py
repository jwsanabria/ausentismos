from django.contrib import admin
from .models import *

# Register your models here.
class AuditAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Persona, AuditAdmin)
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
admin.site.register(InfoAcademica, AuditAdmin)
admin.site.register(ExperienciaLaboral, AuditAdmin)


