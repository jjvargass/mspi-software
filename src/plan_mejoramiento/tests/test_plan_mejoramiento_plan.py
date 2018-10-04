# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_plan(common.TransactionCase):
    def test_crud_validaciones(self):
        plan_model = self.env['plan_mejoramiento.plan']
        vals = {
            'tipo': "contraloria_bog",
            'project_id': self.ref('plan_mejoramiento.project_id_01'),
            'radicado': "Through series half happy night usually no.",
            'dependencia_id': self.ref('plan_mejoramiento.dependencia_id_01'),
            'origen_id': self.ref('plan_mejoramiento.origen_id_01'),
            'sub_origen_id': self.ref('plan_mejoramiento.sub_origen_id_01'),
            'facha': "2001-10-13",
            'hallazgo_ids': "Open last rate debate.",
        }
        plan = plan_model.create(vals)

        # Campos computados

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()