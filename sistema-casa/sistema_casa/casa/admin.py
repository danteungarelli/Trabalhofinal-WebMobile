from django.contrib import admin
from casa.models import Casa

class CasaAdmin(admin.ModelAdmin):
    list_display=['titulo', 'num_quartos', 'num_banheiros', 'tipo', 'area','status','foto']
    
admin.site.register(Casa, CasaAdmin)

