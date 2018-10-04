# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_hallazgo(common.TransactionCase):
    def test_crud_validaciones(self):
        hallazgo_model = self.env['plan_mejoramiento.hallazgo']
        vals = {
            'name': "Town should stuff morning.",
            'descripcion': "Less oil owner article war option.",
            'user_id': self.ref('plan_mejoramiento.user_id_01'),
            'causa_ids': [
                (4, self.ref('plan_mejoramiento.causa_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'proceso_id': self.ref('plan_mejoramiento.proceso_id_01'),
            'dependencia_id': self.ref('plan_mejoramiento.dependencia_id_01'),
            'state': "en_progreso",
            'plan_id': self.ref('plan_mejoramiento.plan_id_01'),
            'acciones_ids': "Majority go weight return degree anyone land.",
        }
        hallazgo = hallazgo_model.create(vals)

        # Campos computados
        self.assertEqual(hallazgo.fecha_inicio, 'Valor Esperado')
        self.assertEqual(hallazgo.fecha_fin, 'Valor Esperado')

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()