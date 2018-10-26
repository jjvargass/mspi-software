# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_probabilidad(common.TransactionCase):
    def test_crud_validaciones(self):
        probabilidad_model = self.env['riesgo.probabilidad']
        vals = {
            'name': "Hair road many.",
            'descripcion': "Agreement do somebody much try.",
            'nivel': 38283920,
            'frecuencia': "Painting several full brother do feeling hair.",
            'activo_sistema': False,
        }
        probabilidad = probabilidad_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()