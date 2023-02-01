# -*- coding: utf-8 -*-

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    project_partner_required = fields.Selection(
        string='Is Partner Required for Projects',
        selection=[
            ('no', 'No'),
            ('required', 'Required'),
            ('subproject', 'Required Only for Sub-projects'),
        ],
        default='no',
    )
    allow_subprojects = fields.Boolean(
        string='Allow Sub-projects',
        default=False,
    )


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    project_partner_required = fields.Selection(
        string='Is Partner Required for Projects',
        related='company_id.project_partner_required',
        readonly=False,
    )
    allow_subprojects = fields.Boolean(
        string='Allow Sub-projects',
        related='company_id.allow_subprojects',
        readonly=False,
    )
