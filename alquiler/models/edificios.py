# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Edificios(models.Model):
    _name = 'Edificio'
    nombre = fields.Char()
    direccion= fields.Char()
    area_terreno= fields.Char()
    area_construida = fields.Char()
    pisos= fields.Integer()
    valor_real = fields.Char()
    valor_fiscal = fields.Char()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
