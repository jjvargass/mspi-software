# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_mapa_procesos_actividad(common.TransactionCase):
    def test_crud_validaciones(self):
        actividad_model = self.env['mapa_procesos.actividad']
        vals = {
            'name': "Good name say.",
            'ciclo': "verificar",
            'descripcion': "Present case option against.",
            'proceso_id': "According soldier space.",
            'entrada_ids': "Else ground late fire still would.",
            'salida_ids': "Activity life whatever condition job.",
        }
        actividad = actividad_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()