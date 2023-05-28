from django.contrib import admin
from .models import Categoria, Filme, Locacao, Cliente
# Register your models here.
from django.contrib import admin
from .models import Categoria, Filme, Locacao, Cliente

admin.site.register(Categoria)
admin.site.register(Filme)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')
admin.site.register(Locacao, LocacaoAdmin)
admin.site.register(Cliente)
