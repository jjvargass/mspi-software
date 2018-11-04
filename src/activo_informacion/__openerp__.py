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
        'data/activo_informacion.activo_tipo.csv',
        'data/activo_informacion.clasificacion.csv',
        'data/activo_informacion.acceso.csv',
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
