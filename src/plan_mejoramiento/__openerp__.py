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
        'views/plan_mejoramiento_view.xml',
        'data/plan_mejoramiento.tipo_calificacion.csv',
        'data/ir.config_parameter.csv',
        'wizards/reporte_plan_view.xml',
    ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'description': """
## Dependencias módulos Python
## Configuración adicional
    """,
}
