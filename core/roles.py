# core/roles.py
from rolepermissions.roles import AbstractUserRole


class Administrador(AbstractUserRole):
    available_permissions = {
        'cadastrar_epi': True,
        'listar_epi': True,
        'cadastrar_recursos': True,
    }


class Militar(AbstractUserRole):
    available_permissions = {
        'listar_epi': True,
    }
