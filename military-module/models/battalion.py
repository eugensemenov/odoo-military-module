from odoo import models, fields, api, _
from .lookups import battalion_types_lookup


class Battalion(models.Model):
    _name = 'military_module.battalion'
    _description = "battalion Model"
    _rec_name = "number"

    # region Fields
    number = fields.Char(string="battalion number", required=True)
    description = fields.Text(string="Description")
    battalion_type = fields.Selection(battalion_types_lookup, string="Тип", default='ski')
    commander_id = fields.Many2one('res.partner', string="Командир")
    military_company_ids = fields.One2many('military_module.company', 'battalion_id', string="Роты")

    people_count = fields.Integer(string="Количество людей")
    recruitment_date = fields.Date(string="Дата набора")
    # endregion
