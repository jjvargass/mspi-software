# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_tipo_riesgo(common.TransactionCase):
    def test_crud_validaciones(self):
        tipo_riesgo_model = self.env['riesgo.tipo_riesgo']
        vals = {
            'name': "Action mention picture.",
            'descripcion': "Action listen war international.",
            'activo_sistema': True,
        }
        tipo_riesgo = tipo_riesgo_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()