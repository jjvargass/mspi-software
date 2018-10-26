# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_impacto(common.TransactionCase):
    def test_crud_validaciones(self):
        impacto_model = self.env['riesgo.impacto']
        vals = {
            'name': "Would these tough happy former treat compare.",
            'nivel': 59512701,
            'cuantitativo': "People into fear actually eight government.",
            'cualitativo': "Wide president lose pass explain.",
            'activo_sistema': True,
        }
        impacto = impacto_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()