# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_accion(common.TransactionCase):
    def test_crud_validaciones(self):
        accion_model = self.env['plan_mejoramiento.accion']
        vals = {
            'name': "People more image act hear third.",
            'descripcion': "Clearly expect may.",
            'tipo': "mejoramiento",
            'state': "nuevo",
            'ejecutor_id': self.ref('planes_mejoramiento.ejecutor_id_01'),
            'dependencia_id': self.ref('planes_mejoramiento.dependencia_id_01'),
            'objetivo': "Trouble water already.",
            'indicador': "Value including the one at can long according.",
            'unidad_medida': "Mean treat vote alone.",
            'meta': "Act could method accept state bit.",
            'recurso_ids': [
                (4, self.ref('planes_mejoramiento.recurso_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'facha_inicio': "1996-02-13",
            'facha_fin': "1979-10-31",
            'facha_creacion': "1987-06-23",
            'hallazgo_id': self.ref('planes_mejoramiento.hallazgo_id_01'),
            'task_ids': "Stop true region life role few.",
            'avance_ids': "Brother its number back miss allow court while.",
        }
        accion = accion_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()