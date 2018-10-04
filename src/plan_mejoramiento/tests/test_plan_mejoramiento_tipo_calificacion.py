# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_tipo_calificacion(common.TransactionCase):
    def test_crud_validaciones(self):
        tipo_calificacion_model = self.env['plan_mejoramiento.tipo_calificacion']
        vals = {
            'name': "Side establish book Congress sound situation cultural.",
            'activo_sistema': False,
            'tipo': "contraloria_bog",
            'state': "terminado_con_retraso",
        }
        tipo_calificacion = tipo_calificacion_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()