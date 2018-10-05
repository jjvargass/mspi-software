# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_mapa_proceso_proceso(common.TransactionCase):
    def test_crud_validaciones(self):
        proceso_model = self.env['mapa_proceso.proceso']
        vals = {
            'name': "New stop since blue design like image.",
            'objetivo': "During something feel course position effort head.",
            'alcance': "One box inside.",
            'tipo': "misional",
            'dependencia_lider': self.ref('operacion_por_procesos.dependencia_lider_01'),
            'dependencia_gestor_ids': [
                (4, self.ref('operacion_por_procesos.dependencia_gestor_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'actividad_ids': "Technology stage later to mean cultural.",
        }
        proceso = proceso_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()