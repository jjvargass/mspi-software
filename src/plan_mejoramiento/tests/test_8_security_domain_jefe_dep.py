# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *


logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_domain_jefe_dep(common.TransactionCase):
    def test_domain_jefe_read_validaciones(self):
        """
            Se valida los permisos y accesos del jefe_dependencia
        """
        jefe_oas_id = self.browse_ref('plan_mejoramiento.id_user_jefe_oas')
        # Plan
        planes = self.env['plan_mejoramiento.plan'].sudo(jefe_oas_id.id).search([])
        self.assertEqual(3, len(planes))
        # Hallazgo
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(jefe_oas_id.id).search([])
        self.assertEqual(3, len(hallazgo))
        # Accion
        accion = self.env['plan_mejoramiento.accion'].sudo(jefe_oas_id.id).search([])
        self.assertEqual(3, len(accion))
        # Avance
        avance = self.env['plan_mejoramiento.avance'].sudo(jefe_oas_id.id).search([])
        self.assertEqual(2, len(avance))


    def test_domain_jefe_create_validaciones(self):
        """
            Se valida los permisos y accesos del jefe_dependencia Create
        """
        jefe_oas_id = self.browse_ref('plan_mejoramiento.id_user_jefe_oas')
        today = date.today()
        # Plan
        try:
            crear_plan = self.env['plan_mejoramiento.plan'].sudo(jefe_oas_id).create({})
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad al Crear Plan')
        # Hallazgo
        try:
            crear_hallazgo = self.env['plan_mejoramiento.plan'].sudo(jefe_oas_id).create({})
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad al Crear Plan')
        # Acción
        accion_01 = self.env['plan_mejoramiento.accion'].sudo(jefe_oas_id).create({
            'name': 'accion Interna 01',
            'descripcion': 'Descripción Acción Interna Preventiva de ...',
            'tipo': 'preventivo',
            'state': 'nuevo',
            'ejecutor_id': self.ref('plan_mejoramiento.id_user_ejecutor_oas'),
            'hallazgo_id': self.ref('plan_mejoramiento.id_hallazgo_i_01'),
            'dependencia_id': self.ref('base_idu.hr_department_9'),
            'objetivo': 'Objetivo de accion Interna',
            'indicador': 'tareas asignadas/tareas resueltas',
            'unidad_medida': 'tareas resueltas',
            'meta': 'lograr realizar...',
            #'recurso_ids': [id_recusro_01,],
            'fecha_inicio': today,
            'fecha_fin': today  + timedelta(days=10),
        })
        # Avance
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')
        # Crear Parametros del sistema
        wizard = self.env['plan_mejoramiento.wizard.activar_avance'].sudo(auditor_id).create({
                'fecha_inicio': today,
                'fecha_fin': today + timedelta(days=10),
        })
        # Ejecutar wizard para establecer fechas para crear avances
        wizard.activar_avance()
        # Crear Avance
        avance = self.env['plan_mejoramiento.avance'].sudo(jefe_oas_id).create({
             'accion_id': self.ref('plan_mejoramiento.id_accion_i_02'),
             'descripcion': 'Descripcion Unit test de avance 01 de accion perteneciente a oci',
         })

    def test_domain_jefe_write_validaciones(self):
        """
            Se valida los permisos y accesos del jefe_dependencia Writre
        """
        jefe_oas_id = self.ref('plan_mejoramiento.id_user_jefe_oas')
        planes = self.env['plan_mejoramiento.plan'].sudo(jefe_oas_id).search([])
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(jefe_oas_id).search([])
        accion = self.env['plan_mejoramiento.accion'].sudo(jefe_oas_id).search([])
        avance = self.env['plan_mejoramiento.avance'].sudo(jefe_oas_id).search([])
        # Plan
        try:
            planes[0].sudo(jefe_oas_id).write({
                'name': 'Sobreescribiendo Nombre',
            })        
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad al Crear Plan')
        # Hallazgo
        try:
            hallazgo[0].sudo(jefe_oas_id).write({
                'name': 'Sobreescribiendo Nombre',
            })        
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad al Crear Plan')
        # Acción
        accion[0].sudo(jefe_oas_id).write({
            'name': 'Sobreescribiendo Nombre',
        })
        # Avance
        avance[0].sudo(jefe_oas_id).write({
            'descripcion': 'Sobreescribiendo Nombre',
        })


if __name__ == '__main__':
    unittest2.main()