# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_riesgo_evaluacion_control(common.TransactionCase):
    def test_crud_validaciones(self):
        evaluacion_control_model = self.env['riesgo.evaluacion_control']
        vals = {
            'name': "Whole son region though part begin.",
            'riesgo_id': self.ref('riesgo.riesgo_id_01'),
            'control_id': self.ref('riesgo.control_id_01'),
            'existe_documentacion': True,
            'existe_responsable': True,
            'es_automatico': True,
            'es_manual': True,
            'frecuencia_adecuada': False,
            'existe_evidencia': True,
            'es_efectiva': False,
        }
        evaluacion_control = evaluacion_control_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()