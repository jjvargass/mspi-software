# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_tipo_calificacion(common.TransactionCase):
    def test_domain_auditor_read_validaciones(self):
        _logger.info("\n***** test_domain_auditor_read_validaciones *****")
        """
            Se valida los permisos y accesos del auditor
        """
        auditor_oaci = self.ref('plan_mejoramiento.id_user_auditor_oaci')
        auditor_oapc = self.ref('plan_mejoramiento.id_user_auditor_oapc')

        # Plan
        planes = self.env['plan_mejoramiento.plan'].sudo(auditor_oaci).search([])
        # tiene acceso de lectura a todos lo planes, creados por él y por otros auditores
        self.assertEqual(3,len(planes))
        # obtener los id de los usuarios de los planes y validar
        user_ids = list(set([i.user_id.id for i in planes]))
        user_ids.sort()
        self.assertEqual([auditor_oaci, auditor_oapc], user_ids)

        # Hallazgo
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(auditor_oaci).search([])
        # tiene acceso de lectura a todos lo hallazgo, creados por él y por otros auditores
        self.assertEqual(3,len(hallazgo))
        # obtener los id de los usuarios de los hallazgo y validar
        user_ids = list(set([i.user_id.id for i in hallazgo]))
        user_ids.sort()
        self.assertEqual([auditor_oaci, auditor_oapc], user_ids)

        # Acción
        accion = self.env['plan_mejoramiento.accion'].sudo(auditor_oaci).search([])
        # tiene acceso de lectura a todos lo accion, creados por él y por otros auditores
        self.assertEqual(3,len(accion))
        # obtener los id de los usuarios de los accción y validar
        user_ids = list(set([i.user_id.id for i in accion]))
        user_ids.sort()
        self.assertEqual([auditor_oaci, auditor_oapc], user_ids)

        #Avances
        avances = self.env['plan_mejoramiento.avance'].sudo(auditor_oaci).search([])
        # tiene acceso de lectura a todos lo avances, creados por él y por otros auditores
        self.assertEqual(2,len(avances))
        # obtener los id de los usuarios de los accción y validar
        user_ids = list(set([i.user_id.id for i in avances]))
        user_ids.sort()
        self.assertEqual([auditor_oaci, auditor_oapc], user_ids)

    def test_domain_auditor_create_validaciones(self):
        _logger.info("\n***** test_domain_auditor_create_validaciones *****")
        """
            Se valida los permisos y accesos del auditor
        """
        auditor_oaci = self.ref('plan_mejoramiento.id_user_auditor_oaci')
        auditor_oapc = self.ref('plan_mejoramiento.id_user_auditor_oapc')
        today = date.today()

        # Plan
        plan = self.env['plan_mejoramiento.plan'].sudo(auditor_oaci).create({
            'name': 'Plan M. INTERNO 01',
            'radicado': 'A001',
            'tipo': 'interno',
            'dependencia_id': self.ref('base_idu.hr_department_7'),
            'origen_id': self.ref('plan_mejoramiento.id_origen_01'),
            'sub_origen_id': self.ref('plan_mejoramiento.id_sub_origen_01'),
        })

        # Hallazgo
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(auditor_oaci).create({
            'plan_id': plan.id,
            'name': 'Hallazgo Interno 02',
            'descripcion': 'Descripción de Hallazgo Interno 01',
            'proceso_id': self.ref('operacion_por_procesos.mapa_proceso_proceso_7'),
            'dependencia_id': self.ref('base_idu.hr_department_7'),
            'state': 'en_progreso',
            'user_id': auditor_oaci,
        })

        # Acciones
        try:
            accion_01 = self.env['plan_mejoramiento.accion'].sudo(auditor_oaci).create({
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
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad al Crear accion_01 El auditor')

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
        try:
            avance = self.env['plan_mejoramiento.avance'].sudo(auditor_oaci).create({
                 'accion_id': self.ref('plan_mejoramiento.id_accion_i_01'),
                 'descripcion': 'Descripcion Unit test de avance 01 de accion perteneciente a oci',
             })
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad al Crear avance por el El auditor')

    def test_domain_auditor_write_validaciones(self):
        _logger.info("\n***** test_domain_auditor_write_validaciones *****")
        """
            Se valida los permisos y accesos del auditor
        """
        auditor_oaci = self.ref('plan_mejoramiento.id_user_auditor_oaci')

        # Plan
        planes = self.env['plan_mejoramiento.plan'].sudo(auditor_oaci).search([])
        planes[0].sudo(auditor_oaci).write({
            'name': 'Sobreescribiendo Nombre',
        })

        # Hallazgo
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(auditor_oaci).search([])
        hallazgo[0].sudo(auditor_oaci).write({
            'name': 'Sobreescribiendo Nombre',
        })

        # Acción
        accion = self.env['plan_mejoramiento.accion'].sudo(auditor_oaci).search([])
        accion[0].sudo(auditor_oaci).write({
            'name': 'Sobreescribiendo Nombre',
        })
        # Avance
        avance = self.env['plan_mejoramiento.avance'].sudo(auditor_oaci).search([])
        avance[0].sudo(auditor_oaci).write({
            'descripcion': 'Sobreescribiendo descripción',
        })

if __name__ == '__main__':
    unittest2.main()