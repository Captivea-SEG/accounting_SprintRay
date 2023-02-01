# -*- coding: utf-8 -*-
{
    'name': 'Project Hierarchy (Parent Projects and Child Projects)',
    'version': '1.0.2',
    'summary': """
    Sub Projects Hierarchy,
    Parent Project Subprojects,
    Parent Project Child Projects,
    Parent Project Sub-projects,
    Master Project Parent,
    Project Level,
    Multiple Child Project Distribution,
    Dividing Fractions Project,
    Split Projects,
    Divide Projects,
    Child-Project Split Subproject,
    Sub-Project Divide Subproject,
    Sub Project Fraction Subproject,
    Adding Fraction Project Work,
    Multiplying Projects    
    """,
    'category': 'Project',
    'author': 'XFanis',
    'support': 'odoo@xfanis.dev',
    'website': 'https://xfanis.dev/odoo.html',
    'license': 'OPL-1',
    'price': 20,
    'currency': 'EUR',
    'description':
        """
        Project Hierarchy (Parent Projects and Child Projects)
        The module allow you create subproject for project and keep your projects directory clean and organized
        """,
    'data': [
        'views/project.xml',
        'views/res_config_settings.xml',
    ],
    'depends': ['project'],
    'qweb': [],
    'images': [
        'static/description/xf_project_hierarchy.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
