# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_origen(common.TransactionCase):
    def test_crud_validaciones(self):
        origen_model = self.env['plan_mejoramiento.origen']
        vals = {
            'name': "Government skill throw at.",
            'descripcion': "Culture quite exactly professor manage herself treat.",
            'parent_id': self.ref('planes_mejoramiento.parent_id_01'),
            'activo_sistema': False,
        }
        origen = origen_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()