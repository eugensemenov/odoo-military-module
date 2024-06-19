from odoo import models, fields, api, _
from .lookups import company_types_lookup


class Company(models.Model):
    _name = 'military_module.company'
    _description = "Company Model"
    _rec_name = "number"

    # region Fields
    number = fields.Char(string="Сompany number", required=True)
    description = fields.Text(string="Description")
    company_type = fields.Selection(company_types_lookup, string="Тип", default='ski')
    commander_id = fields.Many2one('res.partner', string="Командир")
    battalion_id = fields.Many2one('military_module.battalion', string="Battalion")
    platoons_ids = fields.One2many('military_module.platoon', 'military_company_id', string="Взводы")

    people_count = fields.Integer(string="Количество людей")
    recruitment_date = fields.Date(string="Дата набора")
    # endregion

