# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *


logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_wrk_accion(common.TransactionCase):
    def test_wrk_accion_validaciones(self):
        """
            Se ejecutará el cambio de estado de la accion por los usuarios
            correspondientes
        """
        accion = self.browse_ref('plan_mejoramiento.id_accion_i_01').with_context(no_enviar_mail=True)
        jefe_oas_id = self.ref('plan_mejoramiento.id_user_jefe_oas')
        ejecutor_oas_id = self.ref('plan_mejoramiento.id_user_ejecutor_oas')
        ejecutor_oapc_id = self.ref('plan_mejoramiento.id_user_ejecutor_oapc')
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')

        self.assertEqual(len(accion.task_ids), 0) # Estado inicial sin tareas
        self.assertEqual(accion.state, 'nuevo') # Estado inicial

        # (2) Cambiar estado por un usuario no autorizado
        accion.sudo(auditor_id).signal_workflow('wkf_nuevo__por_aprobar')
        self.assertEqual(accion.state, 'nuevo', 'wkf_nuevo__por_aprobar No Ejecutado')

        # (3) Ejecutor cambia estado de nuevo a por Aprovar
        accion.sudo(ejecutor_oas_id).signal_workflow('wkf_nuevo__por_aprobar')
        self.assertEqual(accion.state, 'por_aprobar', 'wkf_nuevo__por_aprobar No Ejecutado')

        # (4) Edición por usuario no autorizado
        try:
            accion.sudo(ejecutor_oapc_id).write({
                'name': 'Sobreescrivir Nombre',
            })
        except AccessError:
            pass
        else:
            self.fail('[No se generó exception]-Se Esperaba de validación domino de acceso')

        # (3) El Auditor aprueba la acción
        accion.sudo(auditor_id).signal_workflow('wkf_por_aprobar__en_progreso')
        self.assertEqual(accion.state, 'en_progreso', 'wkf_por_aprobar__en_progreso No Ejecutado')

        # (4) Cambiar estado por un usuario no autorizado
        accion.sudo(ejecutor_oas_id).signal_workflow('wkf_en_progreso__terminado')
        self.assertEqual(accion.state, 'en_progreso', 'wkf_en_progreso__terminado No Ejecutado')

        # (5) Cambiar estado por un usuario no autorizado
        accion.sudo(auditor_id).signal_workflow('wkf_en_progreso__terminado')
        self.assertEqual(accion.state, 'terminado', 'wkf_en_progreso__terminado No Ejecutado')


if __name__ == '__main__':
    unittest2.main()