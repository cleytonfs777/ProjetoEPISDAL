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


@register.filter(name="circunferencia_mao")
def circunferencia_mao(circunferencia):
    # Retorna o valor da circunferência da mão
    valores = [('10 - XL', '23 a 25cm'), ('11 - XXL', '25 a 28cm'), ('12 - 3XL', '28 a 30cm'), ('5 - XXS', '12 a 15cm'),
               ('6 - XS', '18 a 19cm'), ('7 - S', '19 a 20cm'), ('8 - M', '20 a 21.5cm'), ('9 - L', '21.5 a 23cm')]

    for valor in valores:
        if circunferencia == valor[1]:
            return f"{valor[0]} - {valor[1]}"
