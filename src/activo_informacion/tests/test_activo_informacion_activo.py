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
            'name': "Trial benefit ahead.",
            'descripcion': "Little huge recognize police artist natural.",
            'proceso_id': self.ref('activo_informacion.proceso_id_01'),
            'propietario': "Significant voice agent end.",
            'custodio': "Simply teach pass pay sign local that.",
            'tipo_para_busqueda': "resursoh",
            'tipo': self.ref('activo_informacion.tipo_01'),
            'ubicacion': "Drop various production.",
            'confidencialidad': "ipb",
            'confidencialidad_justificacion': "Structure suggest kid success skin cover perhaps.",
            'integridad': "m",
            'integridad_justificacion': "Behind traditional himself central TV five.",
            'disponibilidad': "1",
            'disponibilidad_justicicacion': "In open heart cover media mouth gun himself.",
            'fecha_ingreso': "2011-01-13",
            'fecha_retiro': "2017-01-09",
            'state': "revisado",
        }
        activo = activo_model.create(vals)

        # Campos computados
        self.assertEqual(activo.criticidad, 'Valor Esperado')

        # Campos con api.constrain


if __name__ == '__main__':
    unittest2.main()