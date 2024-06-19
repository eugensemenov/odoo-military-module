from odoo import models, fields, api, _


class Company(models.Model):
    _name = 'military-module.company'
    _description = "Company Model"

    # region Fields
    number = fields.Char(string="Сompany number", required=True)
    description = fields.Text(string="Description")
    сompany_type = fields.Selection([
        ('mechplatoon', 'Механизированый рота'),
        ('provision', 'Рота обеспечения'),
        ('engineering', 'Инженерный рота'),
        ('infantry', 'Пехотный рота'),
        ('ski', 'Лыжный рота')
    ], string="Тип", default='ski')
    commander_id = fields.Many2one('res.сompany', string="Командир")
    platoons_ids = fields.One2many('military-module.platoon', 'company_id', string="взводы")

    people_count = fields.Integer(string="Количество людей")
    recruitment_date = fields.Date(string="Дата набора")
    # endregion
