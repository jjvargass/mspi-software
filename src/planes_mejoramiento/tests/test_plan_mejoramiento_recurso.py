# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_recurso(common.TransactionCase):
    def test_crud_validaciones(self):
        recurso_model = self.env['plan_mejoramiento.recurso']
        vals = {
            'name': "Fight build character could represent detail paper.",
            'descripcion': "Turn look pressure energy.",
            'activo_sistema': False,
            'tipo': "tecnologico",
        }
        recurso = recurso_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()