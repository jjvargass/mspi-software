# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_avance(common.TransactionCase):
    def test_crud_validaciones(self):
        avance_model = self.env['plan_mejoramiento.avance']
        vals = {
            'descripcion': "On while throughout follow around success number rich.",
            'facha_creacion': "1973-04-01",
            'aprobacion_jefe_dependencia': True,
            'tipo_calificacion_id': self.ref('plan_mejoramiento.tipo_calificacion_id_01'),
            'porcentaje_avance': "Break house movement seek.",
            'observacion': "Conference drop course black western determine north.",
            'accion_id': self.ref('plan_mejoramiento.accion_id_01'),
        }
        avance = avance_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()