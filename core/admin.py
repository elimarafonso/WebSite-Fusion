from django.contrib import admin

# Register your models here.
from .models import Cargo, Servico, Funcionario, Features, Avaliacao


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'cargo', 'modificado')


@admin.register(Features)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'description')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('ativo', 'nome', 'foto', 'profissao', 'comentario', 'estrelas')






