# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_control(common.TransactionCase):
    def test_crud_validaciones(self):
        control_model = self.env['riesgo.control']
        vals = {
            'name': "Ok follow family sometimes.",
            'descripcion': "If bank would become film.",
            'tipo': "preventivo",
            'implementacion': "manual",
            'documentado': False,
            'responsables_ids': [
                (4, self.ref('riesgo.responsables_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'periodicidad': "diario",
        }
        control = control_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()