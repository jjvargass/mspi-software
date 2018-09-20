# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_causa(common.TransactionCase):
    def test_crud_validaciones(self):
        causa_model = self.env['plan_mejoramiento.causa']
        vals = {
            'name': "Door among feel raise worker sing.",
            'descripcion': "Value scene tree.",
            'activo_sistema': False,
        }
        causa = causa_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()