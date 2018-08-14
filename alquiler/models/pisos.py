# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pisos(models.Model):
    _name = 'alquiler'
    numero = fields.Integer()
    tamaño = fields.Integer()
    cant_locales= fields.Integer()
    edificio_name = field.Many2one("edificios", string="edificios")
