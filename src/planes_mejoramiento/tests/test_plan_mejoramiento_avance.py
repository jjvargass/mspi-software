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
            'descripcion': "Business site television mention hold.",
            'facha_creacion': "2003-05-22",
            'aprobacion_jefe_dependencia': False,
            'tipo_calificacion_id': self.ref('planes_mejoramiento.tipo_calificacion_id_01'),
            'porcentaje_avance': "Plan door agency enjoy.",
            'observacion': "Radio rise paper change subject.",
            'accion_id': self.ref('planes_mejoramiento.accion_id_01'),
        }
        avance = avance_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()