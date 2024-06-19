from odoo import models, fields, api, _
from .lookups import platoon_types_lookup


class Platoon(models.Model):
    _name = 'military_module.platoon'
    _description = "Platoon Model"
    _rec_name = "number"

    # region Fields
    number = fields.Char(string="Platoon number", required=True)
    description = fields.Text(string="Description")
    platoon_type = fields.Selection(platoon_types_lookup, string="Тип", default='ski')
    commander_id = fields.Many2one('res.partner', string="Командир")
    military_company_id = fields.Many2one('military_module.company', string="Рота")

    people_count = fields.Integer(string="Количество людей")
    recruitment_date = fields.Date(string="Дата набора")
    # endregion

