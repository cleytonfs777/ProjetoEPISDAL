from django import forms
from django.contrib.auth import forms as auth_forms
from .models import Users


class UserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = Users
        fields = '__all__'


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = Users
        fields = '__all__'
