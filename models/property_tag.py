# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real estate property tag'

    name = fields.Char(string='Name')
