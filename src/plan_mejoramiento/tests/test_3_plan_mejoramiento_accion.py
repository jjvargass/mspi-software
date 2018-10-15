# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_accion(common.TransactionCase):
    def test_date_accion_validaciones(self):
        _logger.info("\n***** test_date_accion_validaciones *****")
        """
            Se Valida control de fecha inicio y fin en la accion
        """

        plan_id = self.ref('plan_mejoramiento.id_plan_i_01')
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')
        ejecutor_oas_id = self.ref('plan_mejoramiento.id_user_ejecutor_oas')
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

        # Crear Hallazgo
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(auditor_id).create({
            'plan_id': plan_id,
            'name': 'Hallazgo Test 01',
            'descripcion': 'Descripción de Hallazgo Interno 01',
            'proceso_id' : self.ref('operacion_por_procesos.mapa_proceso_proceso_7'),
            'dependencia_id': self.ref('base_idu.hr_department_9'),
            'state': 'en_progreso',
            'user_id': auditor_id,
        })
        # Crear Accion
        try:
            accion_01 = self.env['plan_mejoramiento.accion'].sudo(ejecutor_oas_id).create({
                'name': 'accion Interna 01',
                'descripcion': 'Descripción Acción Interna Preventiva de ...',
                'tipo': 'preventivo',
                'state': 'nuevo',
                'ejecutor_id': ejecutor_oas_id,
                'hallazgo_id': hallazgo.id,
                'dependencia_id': self.ref('base_idu.hr_department_9'),
                'objetivo': 'Objetivo de accion Interna',
                'indicador': 'tareas asignadas/tareas resueltas',
                'unidad_medida': 'tareas resueltas',
                'meta': 'lograr realizar...',
                #'recurso_ids': [id_recusro_01,],
                'fecha_inicio': today + timedelta(days=10),
                'fecha_fin': today,
            })
        except ValidationError:
            pass
        else:
            self.fail('[No se generó exception]-Se Esperava Exception de Check y nchange (Fecha_inicio > Fecha_fin) al Crear la Acción')


        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()