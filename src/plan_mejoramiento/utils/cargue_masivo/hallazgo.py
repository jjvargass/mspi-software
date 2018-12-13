#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import erppeek

from tool_user import ToolUser


class Hallazgo(ToolUser):
    def __init__(self, odoo, _logger, plan, id_plan_css , options):
        self.odoo = odoo
        self._logger = _logger
        self.plan = plan
        self.id_plan_css = id_plan_css
        self.options = options

    def open_file_hallazgo(self):
        with open(self.options.path_openERP +'plan_mejoramiento.hallazgo.csv') as csvfile:
            cnt = 0
            reader = csv.DictReader(csvfile)
            for row in reader:
                cnt += 1
                if self.id_plan_css == row['plan_id']:
                    self._logger.debug("    ***[{2}] Cargando Hallazgo: [{0}] del Plan: [{1}]***".format(row['name'].split(), self.plan.name, cnt))
                    # Crear hallazgo
                    hallazgo = self.create_hallazgo(row['auditor_login'], row['name'], row['descripcion'], row['capitulo'], row['proceso_id'], row['dependencia'], row['causa'], self.plan)
                    if not hallazgo:
                        raise Exception('No se creó el hallazgo')
                    # Crear Accion
#                     import_accion = ImportAccion(self.odoo, self._logger, hallazgo, row['hallazgo_id'], self.options)
#                     import_accion.open_file_accion()

    def find_causa(self, name_causa):
        causa = self.odoo.model('plan_mejoramiento.causa').get([('name','=',name_causa.strip())])
        if causa is None:
            #crear origen
            new_causa = self.odoo.model('plan_mejoramiento.origen').create({'name':name_causa.strip()})
            return new_causa
        else:
            return causa

    def find_proceso(self, proceso_id):
        proceso = self.odoo.model('plan_mejoramiento.causa').get([('id','=',proceso_id.strip())])
        return proceso

    def create_hallazgo(self, auditor_login, name, descripcion, capitulo, proceso_id, dependencia, causa, plan):
        auditor = self.get_user(auditor_login,None)
        if not auditor:
            raise Exception('Hallazgo, no se encuentra usuario: {}'.format(auditor_login))
            return
            sys.exit("ERROR:DESCRIPTION:EL usuario: " + auditor_login + " No se encuentar definida en la BD")

        dependencia = self.find_area(dependencia)
        causa = self.find_causa(causa)

        proceso = self.find_proceso(proceso_id)
        if not proceso_id:
            raise Exception('Hallazgo, no se encuentra proceso_id: {}'.format(proceso_id))
            return
            sys.exit("ERROR:DESCRIPTION:EL proceso_id: " + proceso_id + " No se encuentar definida en la BD")

        new_hallazgo = self.odoo.model('plan_mejoramiento.hallazgo').create({
            'plan_id': plan.id,
            'name': name.split(),
            'descripcion': descripcion.split(),
            'proceso_id': proceso.id,
            'dependencia_id': dependencia.id,
            'causa_ids': [causa.id],
            'user_id': auditor.id,
            #'capitulo': capitulo
        })
        return new_hallazgo