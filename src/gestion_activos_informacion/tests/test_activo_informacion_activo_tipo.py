# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_activo_informacion_activo_tipo(common.TransactionCase):
    def test_crud_validaciones(self):
        activo_tipo_model = self.env['activo_informacion.activo_tipo']
        vals = {
            'active': False,
            'name': "Above me blue organization see type know four.",
            'descripcion': "Treatment source international bank business friend green.",
            'tipo': "hardware",
        }
        activo_tipo = activo_tipo_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()