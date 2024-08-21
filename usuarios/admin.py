from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django

from .forms import UserChangeForm, UserCreationForm
from .models import Users
from epis.models import ConjuntoEPI, CapaceteEPI, LuvaEPI, BalaclavaEPI, BotaEPI, CapaceteAquaticoEPI, CapaceteVeicularEPI, LuvaVeicularEPI

# Criação dos Inlines para os EPIs


class ConjuntoEPIInline(admin.StackedInline):
    model = ConjuntoEPI
    can_delete = False
    extra = 0


class CapaceteEPIInline(admin.StackedInline):
    model = CapaceteEPI
    can_delete = False
    extra = 0


class LuvaEPIInline(admin.StackedInline):
    model = LuvaEPI
    can_delete = False
    extra = 0


class BalaclavaEPIInline(admin.StackedInline):
    model = BalaclavaEPI
    can_delete = False
    extra = 0


class BotaEPIInline(admin.StackedInline):
    model = BotaEPI
    can_delete = False
    extra = 0


class CapaceteAquaticoEPIInline(admin.StackedInline):
    model = CapaceteAquaticoEPI
    can_delete = False
    extra = 0


class CapaceteVeicularEPIInline(admin.StackedInline):
    model = CapaceteVeicularEPI
    can_delete = False
    extra = 0


class LuvaVeicularEPIInline(admin.StackedInline):
    model = LuvaVeicularEPI
    can_delete = False
    extra = 0

# Modificação da classe UsersAdmin para incluir os Inlines


@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users

    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': (
                'cargo', 'numbm', 'postgrad', 'time_service_days',
                'status', 'sitfunc', 'gto', 'ativ_esp', 'list_ativ_esp', 'cob', 'unid_lot', 'unid_princ',
                'sexo', 'emailfunc', 'priorit'
            )
        }),
    )

    add_fieldsets = admin_auth_django.UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'classes': ('wide',),
            'fields': (
                'cargo', 'numbm', 'postgrad', 'time_service_days',
                'status', 'sitfunc', 'gto', 'ativ_esp', 'list_ativ_esp', 'cob', 'unid_lot', 'unid_princ',
                'sexo', 'emailfunc', 'priorit'
            )
        }),
    )

    # Adicionando os inlines para edição dos EPIs
    inlines = [
        ConjuntoEPIInline,
        CapaceteEPIInline,
        LuvaEPIInline,
        BalaclavaEPIInline,
        BotaEPIInline,
        CapaceteAquaticoEPIInline,
        CapaceteVeicularEPIInline,
        LuvaVeicularEPIInline,
    ]
