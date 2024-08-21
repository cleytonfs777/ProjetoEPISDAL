# epis/forms.py
from django import forms
from .models import ConjuntoEPI, CapaceteEPI, LuvaEPI, BalaclavaEPI, BotaEPI, CapaceteAquaticoEPI, CapaceteVeicularEPI, LuvaVeicularEPI


class ConjuntoEPIForm(forms.ModelForm):
    class Meta:
        model = ConjuntoEPI
        fields = '__all__'


class CapaceteEPIForm(forms.ModelForm):
    class Meta:
        model = CapaceteEPI
        fields = '__all__'


class LuvaEPIForm(forms.ModelForm):
    class Meta:
        model = LuvaEPI
        fields = '__all__'


class BalaclavaEPIForm(forms.ModelForm):
    class Meta:
        model = BalaclavaEPI
        fields = '__all__'


class BotaEPIForm(forms.ModelForm):
    class Meta:
        model = BotaEPI
        fields = '__all__'


class CapaceteAquaticoEPIForm(forms.ModelForm):
    class Meta:
        model = CapaceteAquaticoEPI
        fields = '__all__'


class CapaceteVeicularEPIForm(forms.ModelForm):
    class Meta:
        model = CapaceteVeicularEPI
        fields = '__all__'


class LuvaVeicularEPIForm(forms.ModelForm):
    class Meta:
        model = LuvaVeicularEPI
        fields = '__all__'
