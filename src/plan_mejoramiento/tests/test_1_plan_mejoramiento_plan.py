# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_plan(common.TransactionCase):
    def test_crud_validaciones(self):
        _logger.info("\n***** test_crud_validaciones Plan *****")
        """
            Se valida la creación del Plan y que la información 
            corresponda conla herencia de proyectos
        """
        plan_model = self.env['plan_mejoramiento.plan']
        auditro= self.browse_ref('plan_mejoramiento.id_user_auditor_oaci')
        
        vals = {
            'name': "Plan Test",
            'tipo': "contraloria_bog",
            'radicado': "Through series half happy night usually no.",
            'origen_id': self.ref('plan_mejoramiento.id_origen_01'),
            'sub_origen_id': self.ref('plan_mejoramiento.id_sub_origen_01'),
            'user_id': auditro.id,
            'dependencia_id': auditro.department_id.id,
        }
        plan = plan_model.create(vals)

        self.assertEqual(
            auditro.id,
            plan.user_id.id,
            'Usuario del Plan no es el asignado'
        )
        self.assertEqual(
            auditro.id,
            plan.edt_raiz_id.user_id.id,
            'Usuario del Plan.edt_raiz_id no es el asignado'
        )
        self.assertEqual(
            auditro.id,
            plan.project_id.user_id.id,
            'Usuario del Plan.project_id no es el asignado'
        )


if __name__ == '__main__':
    unittest2.main()