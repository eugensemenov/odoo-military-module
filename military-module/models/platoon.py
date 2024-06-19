from odoo import models, fields, api, _


class Platoon(models.Model):
    _name = 'military-module.platoon'
    _description = "Platoon Model"

    # region Fields
    number = fields.Char(string="Platoon number", required=True)
    description = fields.Text(string="Description")
    platoon_type = fields.Selection([
        ('mechplatoon', 'Механизированый взвод'),
        ('provision', 'Взвод обеспечения'),
        ('engineering', 'Инженерный взвод'),
        ('infantry', 'Пехотный взвод'),
        ('ski', 'Лыжный взвод')
    ], string="Тип", default='ski')
    commander_id = fields.Many2one('res.partmer', string="Командир")
    company_id = fields.Many2one('military-module.company', string="Командир")

    people_count = fields.Integer(string="Количество людей")
    recruitment_date = fields.Date(string="Дата набора")
    # endregion

