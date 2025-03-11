import logging

from odoo import _, api, fields, models
_logger = logging.getLogger(__name__)
class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My model'

    name = fields.Char(string='Name', help='Name of record')
    field_one = fields.Integer(string='Int field', help='Value of int field')
    field_two = fields.Float(string='Float field', help='Value of float field')
    result_field = fields.Float(string='Result', compute='_compute_result_field')

    @api.depends('field_one', 'field_two')
    def _compute_result_field(self):
        for record in self:
            record.result_field = record.field_one * record.field_two

    def start_function(self):
        _logger.warning(_('You started function by button'))
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Button Clicked!'),
                'message': _('You clicked the button! This is a notification.'),
                'type': 'success',
                'sticky': False,
            }
        }
