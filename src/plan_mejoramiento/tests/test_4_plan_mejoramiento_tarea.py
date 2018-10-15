# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_tarea(common.TransactionCase):
    def test_create_task_validaciones(self):
        _logger.info("\n***** test_create_task_validaciones *****")
        """
            Se valida control de Workflow y Dominios de roles en la accion 
            para ingresar tareas
        """

        accion = self.browse_ref('plan_mejoramiento.id_accion_i_01').with_context(no_enviar_mail=True)
        plan_id = self.ref('plan_mejoramiento.id_plan_i_01')
        jefe_oas_id = self.ref('plan_mejoramiento.id_user_jefe_oas')
        ejecutor_oas_id = self.ref('plan_mejoramiento.id_user_ejecutor_oas')
        ejecutor_oapc_id = self.ref('plan_mejoramiento.id_user_ejecutor_oapc')
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

        # (1) Estado inicial de la acion
        self.assertEqual(len(accion.task_ids), 0) # Estado inicial sin tareas
        self.assertEqual(accion.state, 'nuevo') # Estado inicial
        # revisor_id
        
        # Data Task
        task = {
            'project_id': accion.hallazgo_id.plan_id.project_id.id,
            'name': 'tarea test',
            'edt_id': accion.hallazgo_id.plan_id.edt_raiz_id.id,
            'dependencia_id': self.ref('operacion_por_procesos.mapa_proceso_proceso_5'),
            'user_id': self.ref('plan_mejoramiento.id_user_jefe_oapc'),
            'fecha_inicio': today + timedelta(days=2),
            'fecha_fin': today + timedelta(days=3),
            'accion_id': accion.id
        }
        task2 = {
            'project_id': accion.hallazgo_id.plan_id.project_id.id,
            'name': 'tarea test 2',
            'edt_id': accion.hallazgo_id.plan_id.edt_raiz_id.id,
            'dependencia_id': self.ref('operacion_por_procesos.mapa_proceso_proceso_5'),
            'user_id': self.ref('plan_mejoramiento.id_user_jefe_oapc'),
            'fecha_inicio': today + timedelta(days=2),
            'fecha_fin': today + timedelta(days=3),
            'accion_id': accion.id
        }
        # Test Genera Entra a la Excepción, el estado de la accion debe estar en_progreso
        try:
            accion.sudo(ejecutor_oas_id).write({
                'task_ids': [
                    (0,0, task),
                ]
            })
        except ValidationError, e:
            print "Se da control de estado"
            pass
        else:
            self.fail('[No se generó exception]-Se Esperaba de validación Add Task en estado en_progreso')

        # (2) Ejecutor cambia estado de nuevo a por Aprovar
        accion.sudo(ejecutor_oas_id).signal_workflow('wkf_nuevo__por_aprobar')
        self.assertEqual(accion.state, 'por_aprobar', 'wkf_nuevo__por_aprobar No Ejecutado')
        # (3) El Auditor aprueba la acción
        accion.sudo(auditor_id).signal_workflow('wkf_por_aprobar__en_progreso')
        self.assertEqual(accion.state, 'en_progreso', 'wkf_por_aprobar__en_progreso No Ejecutado')

        # (4) Se crea la tarea por el usuario y el estado correcto
        try:
            accion.sudo(ejecutor_oas_id).write({
                'task_ids': [
                    (0,0, task),
                ]
            })
        except ValidationError, e:
            self.fail('Error en el WRF de las acciones en los permisos de los roles')

        # (5) Crear La tarea por otro usaurio que no pertenece al area
        try:
            accion.sudo(ejecutor_oapc_id).write({
                'task_ids': [
                    (0,0, task2),
                ]
            })
        except AccessError, e:
            print "Se da control de dominios"
            print e
            pass
        else:
            self.fail('[No se generó exception]-Se Esperaba de validación Add Task por usuario de otra área')

        # Verificando la cantidad de tareas creadas
        self.assertEqual(len(accion.task_ids), 1)

if __name__ == '__main__':
    unittest2.main()