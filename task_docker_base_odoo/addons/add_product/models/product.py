from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _sql_constraints = [
                     ('slug_unique',
                      'unique(slug)',
                      'slug already exists')]

    slug = fields.Char(string='slug')
    additional_barcode = fields.Char(string='Additional Barchode')
