{
    'name': 'Operación por Procesos',
    'version': '1.0',
    'depends': [
        'base',
        'base_idu',
        'model_security',
        'document',
    ],
    'author': "José Javier Vargas Serrato",
    'category': 'MSPI',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/mapa_proceso_view.xml',
        'data/mapa_proceso.proceso.csv',
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
