from django.contrib import admin
from .models import (
    ConjuntoEPI,
    CapaceteEPI,
    LuvaEPI,
    BalaclavaEPI,
    BotaEPI,
    CapaceteAquaticoEPI,
    CapaceteVeicularEPI,
    LuvaVeicularEPI
)


class EPIBaseAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anofabricacao',
                    'estadodeconservacao', 'condicao', 'possui', 'recebido')
    list_filter = ('estadodeconservacao', 'condicao',
                   'marca', 'modelo', 'anofabricacao')
    search_fields = ('marca', 'modelo', 'plannumber')
    readonly_fields = ('datapreenchimento',)


class ConjuntoEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + \
        ('jaquetatamanho', 'calcatamanho')
    list_filter = EPIBaseAdmin.list_filter + ('jaquetatamanho', 'calcatamanho')


class CapaceteEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + ('cor',)
    list_filter = EPIBaseAdmin.list_filter + ('cor',)


class LuvaEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + ('circunferenciamao',)
    list_filter = EPIBaseAdmin.list_filter + ('circunferenciamao',)


class BalaclavaEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + ('camadas',)
    list_filter = EPIBaseAdmin.list_filter + ('camadas',)


class BotaEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + ('tamanho',)
    list_filter = EPIBaseAdmin.list_filter + ('tamanho',)


class CapaceteAquaticoEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + ('cor',)
    list_filter = EPIBaseAdmin.list_filter + ('cor',)


class CapaceteVeicularEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + ('cor',)
    list_filter = EPIBaseAdmin.list_filter + ('cor',)


class LuvaVeicularEPIAdmin(EPIBaseAdmin):
    list_display = EPIBaseAdmin.list_display + ('circunferenciamao',)
    list_filter = EPIBaseAdmin.list_filter + ('circunferenciamao',)


# Registrando os modelos no Django Admin
admin.site.register(ConjuntoEPI, ConjuntoEPIAdmin)
admin.site.register(CapaceteEPI, CapaceteEPIAdmin)
admin.site.register(LuvaEPI, LuvaEPIAdmin)
admin.site.register(BalaclavaEPI, BalaclavaEPIAdmin)
admin.site.register(BotaEPI, BotaEPIAdmin)
admin.site.register(CapaceteAquaticoEPI, CapaceteAquaticoEPIAdmin)
admin.site.register(CapaceteVeicularEPI, CapaceteVeicularEPIAdmin)
admin.site.register(LuvaVeicularEPI, LuvaVeicularEPIAdmin)
