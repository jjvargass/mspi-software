# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_mapa_procesos_actividad_entranda(common.TransactionCase):
    def test_crud_validaciones(self):
        actividad_entranda_model = self.env['mapa_procesos.actividad_entranda']
        vals = {
            'name': "Another save practice Mr machine whose national.",
            'descripcion': "Employee across approach enough.",
            'tipo': "externo",
            'proceso': [
                (4, self.ref('operacion_por_procesos.proceso_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'proveedor': [
                (4, self.ref('operacion_por_procesos.proveedor_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'actividad_id': self.ref('operacion_por_procesos.actividad_id_01'),
        }
        actividad_entranda = actividad_entranda_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()