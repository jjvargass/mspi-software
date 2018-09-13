# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError

logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_activo_informacion_activo(common.TransactionCase):
    def test_crud_validaciones(self):
        activo_model = self.env['activo_informacion.activo']
        vals = {
            'name': "Sport behind street wide.",
            'descripcion': "Else around student miss court behind suddenly.",
            'proceso_id': self.ref('gestion_activos_informacion.proceso_id_01'),
            'propietario': "Outside his pick.",
            'custodio': "Now natural find effort most fine fast.",
            'tipo_para_busqueda': "servicio",
            'tipo': self.ref('gestion_activos_informacion.tipo_01'),
            'ubicacion': "Miss deal doctor purpose plant month.",
            'confidencialidad': "ipr",
            'confidencialidad_justificacion': "Difference your goal must foot nearly success.",
            'integridad': "b",
            'integridad_justificacion': "Prevent some interview wide thank.",
            'disponibilidad': "3",
            'disponibilidad_justicicacion': "Argue wall consider up provide catch son.",
            'fecha_ingreso': "2001-05-09",
            'fecha_retiro': "1989-02-14",
            'state': "edicion",
        }
        activo = activo_model.create(vals)

        # Campos computados
        self.assertEqual(activo.criticidad, 'Valor Esperado')

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()