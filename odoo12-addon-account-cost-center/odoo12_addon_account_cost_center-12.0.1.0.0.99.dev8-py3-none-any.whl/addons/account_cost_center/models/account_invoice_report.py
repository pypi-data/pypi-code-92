# Copyright 2015-2019 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    cost_center_id = fields.Many2one(
        'account.cost.center',
        string='Cost Center',
        readonly=True
    )

    def _select(self):
        return super(AccountInvoiceReport, self)._select() + \
            ", sub.cost_center_id as cost_center_id"

    def _sub_select(self):
        return super(AccountInvoiceReport, self)._sub_select() + \
            ", ail.cost_center_id as cost_center_id"

    def _group_by(self):
        return super(AccountInvoiceReport, self)._group_by() + \
            ", ail.cost_center_id"
