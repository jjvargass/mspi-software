# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_causa(common.TransactionCase):
    def test_crud_validaciones(self):
        causa_model = self.env['riesgo.causa']
        vals = {
            'que': "Stop scientist factor society price American stand.",
            'como': "Call democratic age.",
            'cuando': "Design direction nearly toward seat dream.",
            'consecuencia': "Learn economy participant way decide store.",
        }
        causa = causa_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()