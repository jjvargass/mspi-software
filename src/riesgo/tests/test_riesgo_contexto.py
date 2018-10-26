# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_contexto(common.TransactionCase):
    def test_crud_validaciones(self):
        contexto_model = self.env['riesgo.contexto']
        vals = {
            'name': "Defense suggest image city tonight appear feeling.",
            'descripcion': "In outside statement responsibility over front cell.",
            'tipo': "interno",
            'factor_id': self.ref('riesgo.factor_id_01'),
        }
        contexto = contexto_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()