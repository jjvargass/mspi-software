# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_avance(common.TransactionCase):
    def test_crud_avance_fuera_rango_validaciones(self):
        _logger.info("\n***** test_crud_avance_fuera_rango_validaciones *****")
        """
            Se valida el control de fechas para ingresar avances
        """
        ejecutor_oas_id = self.ref('plan_mejoramiento.id_user_ejecutor_oas')
        ejecutor_oapc_id = self.ref('plan_mejoramiento.id_user_ejecutor_oapc')
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')

        # Abrir Registro de Avance
        today = date.today()
        fecha_incio = timedelta(days=10)
        fecha_fin = timedelta(days=20)

        wizard = self.env['plan_mejoramiento.wizard.activar_avance'].sudo(auditor_id).create({
                'fecha_inicio': today + fecha_incio,
                'fecha_fin': today + fecha_fin,
        })
        wizard.activar_avance()
        # Crear avance fuera del rango de fechas
        try:
            avance = self.env['plan_mejoramiento.avance'].sudo(ejecutor_oas_id).create({
                'accion_id': self.ref('plan_mejoramiento.id_accion_i_02'),
                'descripcion': 'Descripcion de avance 01 de accion perteneciente a oci',
            })
        except Warning:
            print "Se da control de wizard.activar_avance"
            pass
        else:
            self.fail('[No se generó exception]-Se Esperaba de validación Add Task en estado en_progreso')

    def test_crud_avance_en_rango_validaciones(self):
        _logger.info("\n***** test_crud_avance_en_rango_validaciones *****")
        """
            Se valida el control de fechas para ingresar avances
        """
        ejecutor_oas_id = self.ref('plan_mejoramiento.id_user_ejecutor_oas')
        ejecutor_oapc_id = self.ref('plan_mejoramiento.id_user_ejecutor_oapc')
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')

        # Abrir Registro de Avance
        today = date.today()

        wizard = self.env['plan_mejoramiento.wizard.activar_avance'].sudo(auditor_id).create({
                'fecha_inicio': today,
                'fecha_fin': today + timedelta(days=20),
        })
        wizard.activar_avance()

        # Crear Accion nuevo para asociar avance
        # utilizando la referencia de los yml ya en test anteriores se agregavan avances
        # y resultava error de solo un avance en mes
        accion_01 = self.env['plan_mejoramiento.accion'].sudo(ejecutor_oas_id).create({
            'name': 'accion Interna 01',
            'descripcion': 'Descripción Acción Interna Preventiva de ...',
            'tipo': 'preventivo',
            'state': 'nuevo',
            'ejecutor_id': ejecutor_oas_id,
            'hallazgo_id': self.ref('plan_mejoramiento.id_hallazgo_i_01'),
            'dependencia_id': self.ref('base_idu.hr_department_9'),
            'objetivo': 'Objetivo de accion Interna',
            'indicador': 'tareas asignadas/tareas resueltas',
            'unidad_medida': 'tareas resueltas',
            'meta': 'lograr realizar...',
            #'recurso_ids': [id_recusro_01,],
            'fecha_inicio': today,
            'fecha_fin': today,
        })
        # Crear avance en rango de fechas
        avance = self.env['plan_mejoramiento.avance'].sudo(ejecutor_oas_id).create({
            'accion_id': accion_01.id,
            'descripcion': 'Descripcion de avance 01 de accion perteneciente a oci',
        })

if __name__ == '__main__':
    unittest2.main()