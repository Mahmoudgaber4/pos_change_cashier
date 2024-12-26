from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    pos_order_count = fields.Integer(
        string="POS Order Count",
        compute='_compute_pos_order_count'
    )

    def _compute_pos_order_count(self):
        for employee in self:
            employee.pos_order_count = self.env['pos.order'].search_count([
                ('employee_id', '=', employee.id)
            ])


    def action_open_pos_orders(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'POS Orders',
            'view_mode': 'tree,form',
            'res_model': 'pos.order',
            'domain': [('employee_id', '=', self.id)],
            'context': {'default_employee_id': self.id},
        }