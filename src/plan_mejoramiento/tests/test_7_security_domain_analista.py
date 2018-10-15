# -*- encoding: utf-8 -*-
import unittest2
import logging
from openerp.tests import common
from openerp.exceptions import ValidationError, AccessError, Warning
from datetime import *


logging.basicConfig()
_logger = logging.getLogger('TEST')

class Test_plan_mejoramiento_domain_analista(common.TransactionCase):
    def test_domain_analista_read_validaciones(self):
        """
            Se valida el dominio de lectura del analista.
            Puede leer todo
        """
        # Plan
        analista_oas_id = self.ref('plan_mejoramiento.id_user_analista_oas')
        planes = self.env['plan_mejoramiento.plan'].sudo(analista_oas_id).search([])
        self.assertEqual(3, len(planes))
        # Hallazgo
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(analista_oas_id).search([])
        self.assertEqual(3, len(hallazgo))
        # Accion
        accion = self.env['plan_mejoramiento.hallazgo'].sudo(analista_oas_id).search([])
        self.assertEqual(3, len(accion))
        # Avance
        avance = self.env['plan_mejoramiento.avance'].sudo(analista_oas_id).search([])
        self.assertEqual(2, len(avance))

    def test_domain_analista_create_validaciones(self):
        """
            Se valida el dominio de creación del analista.
            No puede crear nada
        """
        analista_oas_id = self.ref('plan_mejoramiento.id_user_analista_oas')
        # Plan
        try:
            crear_plan = self.env['plan_mejoramiento.plan'].sudo(analista_oas_id).create({})
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Crando Plan')
        # Hallazgo
        try:
            crear_hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(analista_oas_id).create({})
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Crando Hallazgo')
        # Acción
        try:
            crear_accion = self.env['plan_mejoramiento.accion'].sudo(analista_oas_id).create({})
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Crando Accion')
        # Avance
        auditor_id = self.ref('plan_mejoramiento.id_user_auditor_oaci')
        accion_id = self.ref('plan_mejoramiento.id_accion_i_01')
        # Crear Parametros del sistema
        today = date.today()
        wizard = self.env['plan_mejoramiento.wizard.activar_avance'].sudo(auditor_id).create({
                'fecha_inicio': today,
                'fecha_fin': today + timedelta(days=1),
        })
        # Ejecutar wizard para establecer fechas para crear avances
        wizard.activar_avance()
        # Crear Avance
        try:
            avance = self.env['plan_mejoramiento.avance'].sudo(analista_oas_id).create({
                 'accion_id': accion_id,
                 'descripcion': 'Descripcion Unit test de avance 01 de accion perteneciente a oci',
             })
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Crando Avance')


    def test_domain_analista_write_validaciones(self):
        """
            Se valida el dominio de escritura del analista.
            No puede escrivir nada
        """
        analista_oas_id = self.ref('plan_mejoramiento.id_user_analista_oas')

        planes = self.env['plan_mejoramiento.plan'].sudo(analista_oas_id).search([])
        hallazgo = self.env['plan_mejoramiento.hallazgo'].sudo(analista_oas_id).search([])
        accion = self.env['plan_mejoramiento.accion'].sudo(analista_oas_id).search([])
        avance = self.env['plan_mejoramiento.avance'].sudo(analista_oas_id).search([])

        # Plan
        try:
            planes[0].sudo(analista_oas_id).write({
                'name': 'Sobreescribiendo Nombre',
            })
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Sobreescribiendo Plan')
        # Hallazgo
        try:
            hallazgo[0].sudo(analista_oas_id).write({
                'name': 'Sobreescribiendo Nombre',
            })
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Sobreescribiendo Hallazgo')
        # Accion
        try:
            accion[0].sudo(analista_oas_id).write({
                'name': 'Sobreescribiendo Nombre',
            })
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Sobreescribiendo Accion')
        # Avance
        try:
            avance[0].sudo(analista_oas_id).write({
                 'descripcion': 'Hola ....',
             })
        except AccessError:
            pass
        else:
            self.fail('No se genero Exception de Seguridad Sobreescribiendo Avance')

if __name__ == '__main__':
    unittest2.main()