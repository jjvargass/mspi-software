{
    'name': 'Gestion de Activos de Información',
    'version': '1.0',
    'depends': [
        'base',
        'base_idu',
        'document',
        'model_security',
        'operacion_por_procesos',
    ],
    'author': "José Javier Vargas Serrato",
    'category': 'MSPI',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/activo_informacion_view.xml',
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
