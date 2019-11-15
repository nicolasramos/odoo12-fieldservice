# Copyright (C) 2019 Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    @api.model
    def run(self, procurements):
        for procurement in procurements:
            if 'stock_request_id' in procurement.values and procurement.values.get('stock_request_id'):
                req = self.env['stock.request'].browse(
                    procurement.values.get('stock_request_id'))
        return super().run(procurements)
