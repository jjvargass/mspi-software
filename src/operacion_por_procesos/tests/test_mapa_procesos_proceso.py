# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_mapa_procesos_proceso(common.TransactionCase):
    def test_crud_validaciones(self):
        proceso_model = self.env['mapa_procesos.proceso']
        vals = {
            'name': "What particular floor gas call.",
            'objetivo': "Sure network building sing imagine.",
            'alcance': "Time federal home baby.",
            'tipo': "control",
            'dependencia_lider': self.ref('operacion_por_procesos.dependencia_lider_01'),
            'dependencia_gestor': [
                (4, self.ref('operacion_por_procesos.dependencia_gestor_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'actividad_ids': "Relate food speak partner investment purpose.",
        }
        proceso = proceso_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()