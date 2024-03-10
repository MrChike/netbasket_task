from odoo.tests.common import TransactionCase
from models.product import ProductTemplate


class TestProductTemplate(TransactionCase):
    def test_slug_field(self):
        field = self.env['product.template'].create({'slug’: ’'})
        field.action()
        product_template = ProductTemplate()
        self.assertEqual(field.slug, product_template.slug)
