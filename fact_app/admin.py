from django.contrib import admin

# Register your models here.
from .models import *

class AdminClient(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone','sexe', 'age', 'zip_code', 'date_creation', 'save_by','address','ville')

class AdminFacture(admin.ModelAdmin):
    list_display = ('client','save_by','facture_date_time','total','last_update_date','paye','facture_type','ville','commentaire')

admin.site.register(Client, AdminClient)
admin.site.register(Facture, AdminFacture)
admin.site.register(Article)
