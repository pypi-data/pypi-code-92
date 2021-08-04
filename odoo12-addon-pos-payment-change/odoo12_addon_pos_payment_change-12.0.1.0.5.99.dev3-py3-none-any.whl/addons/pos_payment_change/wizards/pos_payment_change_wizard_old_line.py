# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PosPaymentChangeWizardOldLine(models.TransientModel):
    _name = "pos.payment.change.wizard.old.line"
    _description = "PoS Payment Change Wizard Old Line"

    wizard_id = fields.Many2one(
        comodel_name="pos.payment.change.wizard", required=True,
        ondelete='cascade'
    )

    old_journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Journal",
        required=True,
        readonly=True,
    )

    company_currency_id = fields.Many2one(
        comodel_name='res.currency', store=True,
        related='old_journal_id.currency_id',
        string="Company Currency", readonly=True,
        help='Utility field to express amount currency'
    )

    amount = fields.Monetary(
        string="Amount",
        required=True,
        readonly=True, default=0.0,
        currency_field='company_currency_id'
    )
