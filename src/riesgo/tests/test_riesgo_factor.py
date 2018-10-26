# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_factor(common.TransactionCase):
    def test_crud_validaciones(self):
        factor_model = self.env['riesgo.factor']
        vals = {
            'name': "No hold with pretty.",
            'descripcion': "Though three even.",
            'tipo': "externo",
            'activo_sistema': False,
        }
        factor = factor_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()