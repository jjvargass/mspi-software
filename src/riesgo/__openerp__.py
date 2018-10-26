{
    'name': 'Gestión de Riesgos',
    'version': '1.0',
    'depends': [
        'activo_informacion',
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
        'views/riesgo_view.xml',
        'data/riesgo.factor.csv',
        'data/riesgo.tipo_riesgo.csv',
        'data/riesgo.impacto.csv',
        'data/riesgo.probabilidad.csv',
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
