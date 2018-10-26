# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_riesgo(common.TransactionCase):
    def test_crud_validaciones(self):
        riesgo_model = self.env['riesgo.riesgo']
        vals = {
            'name': "Road record others say official cell.",
            'descripcion': "General benefit usually strategy last.",
            'proceso_id': self.ref('riesgo.proceso_id_01'),
            'seguridad_de_la_informacion': True,
            'activo_informacion_id': self.ref('riesgo.activo_informacion_id_01'),
            'causa_ids': [
                (4, self.ref('riesgo.causa_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'contexto_ids': [
                (4, self.ref('riesgo.contexto_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'tipo_riesgo_id': self.ref('riesgo.tipo_riesgo_id_01'),
            'probabilidad_id': self.ref('riesgo.probabilidad_id_01'),
            'user_id': self.ref('riesgo.user_id_01'),
            'dependencia_id': self.ref('riesgo.dependencia_id_01'),
            'impacto_id': self.ref('riesgo.impacto_id_01'),
            'evaluar_control_ids': "From financial end bar coach form.",
        }
        riesgo = riesgo_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()