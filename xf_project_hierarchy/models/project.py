from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Project(models.Model):
    _inherit = 'project.project'

    parent_id = fields.Many2one(
        string='Parent Project',
        comodel_name='project.project',
        index=True,
        ondelete='restrict',
    )
    child_ids = fields.One2many(
        string='Sub-projects',
        comodel_name='project.project',
        inverse_name='parent_id',
    )
    count_child_ids = fields.Integer(
        string='Count Sub-projects',
        compute='_compute_count_child_ids',
    )
    percentage = fields.Float(
        string='Percentage',
        default=0.0,
    )
    total_percentage = fields.Float(
        string='Total Percentage of Sub-projects',
        compute='_compute_total_percentage',
        compute_sudo=True,
        store=True,
    )
    allow_subprojects = fields.Boolean(
        string='Allow Sub-projects',
        related='company_id.allow_subprojects',
    )
    is_partner_required = fields.Boolean(
        string='Is Partner Required',
        compute='_compute_is_partner_required',
    )

    @api.constrains('parent_id')
    def _check_project_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive projects.'))

    def _compute_count_child_ids(self):
        for project in self.sudo():
            project.count_child_ids = len(project.child_ids)

    @api.depends('child_ids.percentage')
    def _compute_total_percentage(self):
        for project in self:
            if project.child_ids:
                project.total_percentage = sum(project.child_ids.mapped('percentage'))
            else:
                project.total_percentage = 0

    @api.constrains('percentage', 'total_percentage')
    def _check_percentage(self):
        for project in self:
            if project.percentage < 0 or project.percentage > 100:
                raise ValidationError(_('The percentage of a project should be between 0 and 100.'))
            if project.total_percentage < 0 or project.total_percentage > 100:
                raise ValidationError(_('The total percentage of sub-projects should be between 0 and 100.'))

    @api.depends('parent_id', 'company_id')
    def _compute_is_partner_required(self):
        for project in self:
            if project.company_id.project_partner_required == 'required':
                project.is_partner_required = True
            elif project.company_id.project_partner_required == 'subproject' and project.parent_id:
                project.is_partner_required = True
            else:
                project.is_partner_required = False

    def action_view_sub_projects(self):
        self.ensure_one()
        if not self.child_ids:
            return {'type': 'ir.actions.act_window_close'}

        action = self.env['ir.actions.actions']._for_xml_id('project.open_view_project_all')
        action['domain'] = [('id', 'in', self.child_ids.ids)]
        action['context'] = {'default_parent_id': self.id, }
        action['display_name'] = _('Sub-Projects')
        return action
