# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alquiler(models.Model, res.partner):
    _name = 'alquiler'
    numero_local = fields.Integer()
    metros_c = fields.Integer()
    medidor_c = fields.Integer()
    medidor_a = fields.Integer()
    sala= fields.One2one("pisos", string ="sala")
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
