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
            'activo_sistema': True,
            'name': "Nature tend power treatment since.",
            'descripcion': "Mention ground seem.",
            'tipo': "software",
        }
        activo_tipo = activo_tipo_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()