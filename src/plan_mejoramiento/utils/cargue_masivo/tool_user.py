#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

class ToolUser():
    def __init__(self, odoo, _logger):
        self.odoo = odoo
        self._logger = _logger


    def get_user(self, login=None, email=None):
        if email:
            user = self.odoo.model('res.users').get([('email','=',email.strip())])
        elif login:
            user = self.odoo.model('res.users').get([('login','=',login.strip())])
        return user

    def find_area(self, name_area):
        area = self.odoo.model('hr.department').get([('abreviatura','=',name_area.strip())])
        if area is None:
            raise Exception("El Area: '" + name_area + "' no se encuentar definida en la BD")
        return area

    def get_rol_number_csv(self, number_rol_user):
        categoria = self.odoo.model('ir.module.category').get([('name','=','Planes de Mejoramiento')])
        if number_rol_user.strip() == '1': # se define 1 en el archivo plan
            # buscar Auditor
            groups = self.odoo.model('res.groups').get([('category_id','=',categoria.id),('name','=','Auditor')])
        elif number_rol_user.strip() == '2':
            # buscar Ejecutor
            groups = self.odoo.model('res.groups').get([('category_id','=',categoria.id),('name','=','Ejecutor')])
        return groups

    def create_user(self, auditor_login, name_user, email_user, area_user, number_rol_user=None):
        # buscar area
        area = self.find_area(area_user)
        if number_rol_user:
            groups = self.get_rol_number_csv(number_rol_user)
            # crear usuario
            new_user = self.odoo.model('res.users').create({
                'name': name_user.strip(),
                'login': auditor_login.strip(),
                'groups_id': [(4,groups.id)],
                'lang': 'es_CO',
                'tz': 'America/Bogota',
            })
        else:
            # crear usuario sin grupo
            new_user = self.odoo.model('res.users').create({
                'name': name_user.strip(),
                'login': auditor_login.strip(),
                'lang': 'es_CO',
                'tz': 'America/Bogota',
            })
        # actualizar partner_id para correo
        partner = self.odoo.model('res.partner').get([('id','=',new_user.partner_id.id)])
        partner.write({
            'email': email_user,
        })
        # crear empleado
        new_employee = self.odoo.model('hr.employee').create({'name':name_user.strip(), 'user_id': new_user.id, 'department_id': area.id})
        return new_user

    def add_rol_to_user(self, number_rol_user, email):
        groups = self.get_rol_number_csv(number_rol_user)
        user = self.get_user(None, email)
        # si no tiene el rol lo agrega
        if not groups.id in user.groups_id.id:
            self._logger.debug("se agrega rol")
            user.write({
                'groups_id': [(4,groups.id)],
            })

    def get_usertes(self, auditor, email=None):
        user = self.odoo.model('res.users').get(
            [
                ('email','=',email.strip())
            ]
        )
        user2 = self.odoo.model('res.users').get(
            [
                ('email','=','kkikik@gmail.com')
            ]
        )
#         self._logger.debug("user")
#         self._logger.debug("{0}".format(user))
        self._logger.debug("user02")
        self._logger.debug("{0}".format(user2))
        self._logger.debug("{0}".format(not user2))
        
#         if user:
#             self._logger.debug("entra user")

        if not user2:
            self._logger.debug("entra user2")
        else:
            self._logger.debug("No entra con NONE user2")

# 

# 
#     def find_user_existing(self, auditor, email=None):
#         user = self.odoo.model('res.users').get([('login','=',auditor.strip())])
#         if user:
#             return True
#         else:
#             if email:
#                 user = self.odoo.model('res.users').get([('email','=',email.strip())])
#             if user:
#                 return True
#             return False
# 
#     def get_user(self, auditor, email=None):
#         user = self.odoo.model('res.users').get([('login','=',auditor.strip())])
#         if user:
#             return user.id
#         else:
#             if email:
#                 user = self.odoo.model('res.users').get([('email','=',email.strip())])
#             if user:
#                 return user.id
# 

# 

# 
#     def get_object_user(self, usuario_id):
#         user = self.odoo.model('res.users').get([('id','=', usuario_id)])
#         return  user
# 
#     def asignar_jefe_al_area(self, abreviatura_area, usuario_id):
#         area = self.odoo.model('hr.department').get([
#                 ('abreviatura', '=', abreviatura_area)
#             ])
#         usuario = self.get_object_user(usuario_id)
#         area.write({
#             'manager_id': usuario.employee_id.id,
#         })
# 
#     def asignar_rol_jefe_depedencia(self, user_id):
#         groups = self.odoo.model('res.groups').get([('name','=','Jefe Dependencia')])
#         groups.write({
#             'users': [(4,user_id)]
#         })