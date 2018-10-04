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
            'name': "Above participant finally western.",
            'descripcion': "Election cultural human husband.",
            'tipo': "correccion",
            'state': "por_aprobar",
            'ejecutor_id': self.ref('plan_mejoramiento.ejecutor_id_01'),
            'dependencia_id': self.ref('plan_mejoramiento.dependencia_id_01'),
            'objetivo': "Beyond federal candidate nice.",
            'indicador': "Idea series want him movie about Mrs page.",
            'unidad_medida': "Consumer cultural song minute himself author civil group.",
            'meta': "There animal hot reflect.",
            'recurso_ids': [
                (4, self.ref('plan_mejoramiento.recurso_ids_01')),
                (0, 0, {
                    'field_name': valor,
                }),
            ],
            'facha_inicio': "2016-08-25",
            'facha_fin': "1981-02-26",
            'facha_creacion': "1974-05-23",
            'hallazgo_id': self.ref('plan_mejoramiento.hallazgo_id_01'),
            'task_ids': "Better court cold pattern city.",
            'avance_ids': "Change home entire then teacher show out.",
        }
        accion = accion_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()