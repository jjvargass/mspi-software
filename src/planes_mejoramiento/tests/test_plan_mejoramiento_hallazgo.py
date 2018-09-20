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
            'name': "Continue partner total realize property audience camera.",
            'descripcion': "Ability low however probably.",
            'user_id': self.ref('planes_mejoramiento.user_id_01'),
            'causa_ids': [
                (4, self.ref('planes_mejoramiento.causa_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'proceso_id': self.ref('planes_mejoramiento.proceso_id_01'),
            'dependencia_id': self.ref('planes_mejoramiento.dependencia_id_01'),
            'state': "terminado",
            'plan_id': self.ref('planes_mejoramiento.plan_id_01'),
            'acciones_ids': "Ahead thing organization main gas.",
        }
        hallazgo = hallazgo_model.create(vals)

        # Campos computados
        self.assertEqual(hallazgo.fecha_inicio, 'Valor Esperado')
        self.assertEqual(hallazgo.fecha_fin, 'Valor Esperado')

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()