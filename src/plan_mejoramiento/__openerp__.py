{
    'name': 'Planes de Mejoramiento',
    'version': '1.0',
    'depends': [
        'base',
        'base_idu',
        'document',
        'model_security',
        'operacion_por_procesos',
        'project_portafolio_idu',
    ],
    'author': "José Javier Vargas Serrato",
    'category': 'MSPI',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/crear_progreso_de_tarea.xml',
        'views/plan_mejoramiento_view.xml',
        'views/project_view.xml',
        'data/plan_mejoramiento.tipo_calificacion.csv',
        'data/ir.config_parameter.csv',
        'wizards/reporte_plan_view.xml',
        'wizards/activar_avance_view.xml',
        'workflow/accion_workflow.xml',
    ],
    'test': [
        'tests/000_test_data_usuarios.yml',
        'tests/001_test_data_config.yml',
        'tests/002_test_data_plan.yml',
        'tests/003_test_data_hallazgo.yml',
        'tests/004_test_data_accion.yml',
    ],
    'demo': [
        'tests/000_test_data_usuarios.yml',
        'tests/001_test_data_config.yml',
        'tests/002_test_data_plan.yml',
        'tests/003_test_data_hallazgo.yml',
        'tests/004_test_data_accion.yml',
    ],
    'installable': True,
    'description': """
## Dependencias módulos Python
## Configuración adicional
    """,
}
