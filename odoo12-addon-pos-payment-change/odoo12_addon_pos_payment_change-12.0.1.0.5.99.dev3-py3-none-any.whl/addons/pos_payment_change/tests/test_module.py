# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError


class TestModule(TransactionCase):
    """Tests for 'Point of Sale - Change Payment' Module"""

    def setUp(self):
        super().setUp()
        self.PosSession = self.env["pos.session"]
        self.PosOrder = self.env["pos.order"]
        self.AccountJournal = self.env["account.journal"]
        self.PosMakePayment = self.env['pos.make.payment']
        self.PosPaymentChangeWizard = self.env["pos.payment.change.wizard"]
        self.PosPaymentChangeWizardNewLine = self.env[
            "pos.payment.change.wizard.new.line"
        ]
        self.product = self.env.ref("product.product_product_3")
        self.pos_config = self.env.ref("point_of_sale.pos_config_main").copy()

    def _initialize_journals_open_session(self):

        self.check_journal = self.AccountJournal.create({
            "name": "Demo Check Journal",
            "type": "bank",
            "journal_user": True,
        })
        self.cash_journal = self.AccountJournal.create({
            "name": "Demo Cash Journal",
            "type": "cash",
            "journal_user": True,
        })

        # create new session and open it
        self.pos_config.journal_ids = [
            self.check_journal.id,
            self.cash_journal.id,
        ]
        self.pos_config.open_session_cb()
        self.session = self.pos_config.current_session_id
        self.check_statement = self.session.statement_ids.filtered(
            lambda x: x.journal_id == self.check_journal
        )
        self.cash_statement = self.session.statement_ids.filtered(
            lambda x: x.journal_id == self.cash_journal
        )

    def _sale(self, journal_1, price_1, journal_2=False, price_2=0.0):
        price = price_1 + price_2
        line_vals = {
            "name": "OL/0001",
            "product_id": self.product.id,
            "qty": 1.0,
            "price_unit": price,
            "price_subtotal": price,
            "price_subtotal_incl": price,
        }
        order = self.PosOrder.create({
            "session_id": self.session.id,
            "amount_tax": 0,
            "amount_total": price,
            "amount_paid": price,
            "amount_return": 0,
            "lines": [[0, False, line_vals]],
        })
        order.add_payment({
            'amount': price_1,
            'payment_date': fields.Date.today(),
            'payment_name': "Demo",
            'journal': journal_1.id,
            })
        if journal_2:
            order.add_payment({
                'amount': price_2,
                'payment_date': fields.Date.today(),
                'payment_name': "Demo",
                'journal': journal_2.id,
            })
        order.action_pos_order_paid()
        return order

    def _change_payment(
            self, order, journal_1, amount_1, journal_2=False, amount_2=0.0
    ):
        # Switch to check journal
        wizard = self.PosPaymentChangeWizard.with_context(
            active_id=order.id
        ).create({})
        self.PosPaymentChangeWizardNewLine.with_context(
            active_id=order.id
        ).create(
            {
                "wizard_id": wizard.id,
                "new_journal_id": journal_1.id,
                "amount": amount_1,
            }
        )
        if journal_2:
            self.PosPaymentChangeWizardNewLine.with_context(
                active_id=order.id
            ).create(
                {
                    "wizard_id": wizard.id,
                    "new_journal_id": journal_2.id,
                    "amount": amount_2,
                }
            )
        wizard.button_change_payment()

    # Test Section
    def test_01_payment_change_policy_update(self):
        self.pos_config.payment_change_policy = "update"

        self._initialize_journals_open_session()
        # Make a sale with 35 in cash journal and 65 in check
        order = self._sale(self.cash_journal, 35, self.check_journal, 65)

        order_qty = len(self.PosOrder.search([]))

        with self.assertRaises(UserError):
            # Should not work if total is not correct
            self._change_payment(
                order, self.cash_journal, 10, self.check_journal, 10)

        self._change_payment(
            order, self.cash_journal, 10, self.check_journal, 90)

        # check Session
        self.assertEqual(
            self.cash_statement.balance_end,
            10,
            "Bad recompute of the balance for the statement cash",
        )

        self.assertEqual(
            self.check_statement.balance_end,
            90,
            "Bad recompute of the balance for the statement check",
        )

        # Check Order quantity
        self.assertEqual(
            order_qty,
            len(self.PosOrder.search([])),
            "In 'Update' mode, changing payment should not create"
            " other PoS Orders",
        )

    def test_02_payment_change_policy_refund(self):
        self.pos_config.payment_change_policy = "refund"

        self._initialize_journals_open_session()
        # Make a sale with 35 in cash journal and 65 in check
        order = self._sale(self.cash_journal, 35, self.check_journal, 65)

        order_qty = len(self.PosOrder.search([]))

        self._change_payment(
            order, self.cash_journal, 50, self.check_journal, 50)

        # Check Order quantity
        self.assertEqual(
            order_qty + 2,
            len(self.PosOrder.search([])),
            "In 'Refund' mode, changing payment should generate"
            " two new PoS Orders",
        )
