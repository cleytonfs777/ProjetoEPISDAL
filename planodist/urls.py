from django.urls import path

from . import views

urlpatterns = [
    path('criaplano/', views.criaplano, name='criaplano'),
]
