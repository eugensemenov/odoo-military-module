from odoo import models, fields, api, _


class Battalion(models.Model):
    _name = 'military-module.company'
    _description = "battalion Model"

    # region Fields
    number = fields.Char(string="battalion number", required=True)
    description = fields.Text(string="Description")
    battalion_type = fields.Selection([
        ('mechplatoon', 'Механизированый батальон'),
        ('provision', 'Батальон обеспечения'),
        ('engineering', 'Инженерный батальон'),
        ('infantry', 'Пехотный батальон'),
        ('ski', 'Лыжный батальон')
    ], string="Тип", default='ski')
    commander_id = fields.Many2one('res.сompany', string="Командир")
    company_ids = fields.One2many('military-module.company', 'battalion_id', string="роты")

    people_count = fields.Integer(string="Количество людей")
    recruitment_date = fields.Date(string="Дата набора")
    # endregion