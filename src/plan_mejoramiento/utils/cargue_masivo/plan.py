#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import erppeek
import sys

from tool_user import ToolUser

class Plan(ToolUser):
    def __init__(self, odoo, _logger, options):
        self.odoo = odoo
        self._logger = _logger
        self.options = options

    def test_get_user(self):
        user = self.get_user('jj', 'analista_oapc@gmail.com')
 
    def open_file_plan(self):
        with open(self.options.path_openERP +'plan_mejoramiento.plan.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    self._logger.debug("***Cargando Plan: {0} ***".format(row['nombre']))
                    # buscar existencia del auditor
                    auditor = self.get_user(None,row['email_user'])
                    if not auditor:
                        # crear
                        self._logger.debug("crea")
                        auditor = self.create_user(row['auditor_login'], row['name_user'], row['email_user'], row['area_user'], row['number_rol_user'])
                    else:
                        # actualizo rol
                        self._logger.debug("Actualiza")
                        self.add_rol_to_user(row['number_rol_user'], row['email_user'])
                    dependencia = self.find_area(row['dependencia'])

                    if row['tipo'].strip() == 'interno':
                        origen = self.find_origen(row['origen'])
                        sub_origen = self.find_sub_origen(origen,row['sub_origen'])
                        # Crear plan interno
                        plan_int = self.create_plan(row['nombre'], row['radicado'], dependencia, auditor, row['tipo'], origen.id, sub_origen.id)
                        # hallazgo
                        #import_hallazgo = ImportHallazgo(self.odoo, self._logger, plan_int, row['id'], self.options)
                        #import_hallazgo.open_file_hallazgo()
                    else:
                        #Crear plan  Ext
                        plan_ext = self.create_plan_ext(row['nombre'], row['radicado'], dependencia, auditor, row['tipo'])
                        # hallazgo
                        #import_hallazgo = ImportHallazgo(self.odoo, self._logger, plan_ext, row['id'], self.options)
                        #import_hallazgo.open_file_hallazgo()
                except Exception as e:
                    self._logger.error('*******************')
                    self._logger.exception(e)

    def find_origen(self, name_origen):
        origen = self.odoo.model('plan_mejoramiento.origen').get([('name','=',name_origen.strip())])
        if origen is None:
            #crear origen
            new_origen = self.odoo.model('plan_mejoramiento.origen').create({'name':name_origen.strip()})
            return new_origen
        else:
            return origen

    def find_sub_origen(self, origen, name_sub_origen):
        sub_origen = self.odoo.model('plan_mejoramiento.origen').get([('name','=',name_sub_origen), ('parent_id','=',origen.id)])
        if sub_origen is None:
            #crear sub-origen
            new_sub_origen = self.odoo.model('plan_mejoramiento.origen').create({'name':name_sub_origen, 'parent_id':origen.id})
            return new_sub_origen
        else:
            return sub_origen

    def create_plan(self, nombre, radicado, dependencia, auditor, tipo, origen, sub_origen):
        new_plan = self.odoo.model('plan_mejoramiento.plan').create({
            'name': nombre,
            'radicado':radicado,
            'dependencia_id': dependencia,
            'user_id': auditor,
            'tipo': tipo,
            'origen_id': origen,
            'sub_origen_id': sub_origen,
        })
        return new_plan

    def create_plan_ext(self, nombre, radicado, dependencia, auditor, tipo):
        new_plan = self.odoo.model('plan_mejoramiento.plan').create({
            'name': nombre.strip(),
            'radicado':radicado.strip(),
            'dependencia_id': dependencia,
            'user_id': auditor,
            'tipo': tipo,
        })
        return new_plan