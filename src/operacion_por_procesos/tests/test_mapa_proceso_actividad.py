# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_mapa_proceso_actividad(common.TransactionCase):
    def test_crud_validaciones(self):
        actividad_model = self.env['mapa_proceso.actividad']
        vals = {
            'name': "Want arm decide air office.",
            'ciclo': "actuar",
            'descripcion': "Lot contain city.",
            'proceso_id': "Skill writer popular crime modern.",
            'entrada_ids': "Feeling protect relationship trip add hundred care.",
            'salida_ids': "Add appear trouble firm know talk.",
        }
        actividad = actividad_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()