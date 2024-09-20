from datetime import timedelta
from django import template
from django.db.models import Case, FloatField, Sum, When


register = template.Library()


@register.filter(name="list_gtos")
def list_gtos(list):
    # Verifica se a lista é vazia
    if not list:
        return []
    list = [item.id for item in list]
    print(list)
    print(type(list))
    return list


@register.filter(name="dias_para_anos")
def dias_para_anos(dias):
    # Considera-se que um ano tem 365 dias
    anos = dias // 365
    return f"{anos} anos"
