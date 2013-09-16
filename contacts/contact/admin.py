from django.contrib import admin
from contact.models import Lice, Kompanija, Grupi

class KompanijaInline(admin.TabularInline):
    model = Kompanija
    extra = 3
    
class LiceInline(admin.TabularInline):
    model = Lice
    extra = 3

class GrupiAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,                      {'fields' : ['oblast']}), 
    ('Informacii za datum',     {'fields':  ['datum_kreiranje']}),
    ]
    inlines = [KompanijaInline]
    
class KompanijaAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,                      {'fields' : ['ime', 'opis']}),
    ('Informacii za datum',     {'fields':  ['datum_kreiranje']}),
    ]
    inlines = [LiceInline]

admin.site.register(Grupi, GrupiAdmin)
admin.site.register(Kompanija, KompanijaAdmin)

