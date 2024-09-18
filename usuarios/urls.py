from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('create-user/', views.create_user_and_epis,
         name='create_user_and_epis'),
    path('criar-usuario-fake/', views.criar_usuario_ficticio_view,
         name='criar_usuario_ficticio'),

    path('popular-lista-usuarios/', views.popular_lista_usuarios_view,
         name='popular_lista_usuarios'),

    path('listar-usuarios/', views.listar_usuarios_view,
         name='listar_usuarios'),


]
