from django.urls import path

from . import views

urlpatterns = [
    path('ciurb/', views.ciurb, name='ciurb'),
    path('multimissao/', views.multimissao, name='multimissao'),
    path('salvamento/', views.salvamento, name='salvamento'),
    path('motorresgate/', views.motorresgate, name='motorresgate'),
]
