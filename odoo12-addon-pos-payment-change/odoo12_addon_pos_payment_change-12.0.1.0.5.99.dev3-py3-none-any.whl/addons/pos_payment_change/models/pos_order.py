# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo import _, api, models
from odoo.tools import float_is_zero
from odoo.exceptions import Warning as UserError


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.multi
    def change_payment(self, payment_lines):
        """
        Change payment of a given order.
        payment_lines should be a list of data that are
        the argument of the Odoo Core function add_payment()
        Return a list of order ids, depending on the
        payment_change_policy of the related pos_config.
        """
        self.ensure_one()
        orders = self

        # Removing zero lines
        precision = self.pricelist_id.currency_id.decimal_places
        payment_lines = [
            x for x in payment_lines if not float_is_zero(
                x["amount"], precision_digits=precision)
        ]

        self._check_payment_change_allowed()

        comment = _(
            "The payments of the Order %s (Ref: %s) has been changed"
            " by %s at %s." % (
                self.name,
                self.pos_reference,
                self.env.user.name,
                datetime.today(),
            )
        )

        if self.config_id.payment_change_policy == "update":
            self.statement_ids.with_context().unlink()

            # Create new payment
            for line in payment_lines:
                self.add_payment(line)

        elif self.config_id.payment_change_policy == "refund":
            # Refund order and mark it as paid
            # with same payment method as the original one
            refund_result = self.refund()
            refund_order = self.browse(refund_result["res_id"])

            refund_order.write({
                "date_order": self.date_order,
                "session_id": self.session_id.id,
                })

            for statement in self.statement_ids:
                refund_order.add_payment({
                    "journal": statement.journal_id.id,
                    "amount": - statement.amount,
                    "payment_date": self.date_order,
                })
            refund_order.action_pos_order_paid()

            # Resale order and mark it as paid
            # with the new payment
            resale_order = self.copy(
                default={"pos_reference": self.pos_reference}
            )

            for line in payment_lines:
                resale_order.add_payment(line)
            resale_order.action_pos_order_paid()

            orders += refund_order + resale_order
            comment += _(" (Refund Order: %s ; Resale Order: %s)" % (
                refund_order.name, resale_order.name))
        for order in orders:
            order.note = "%s\n%s" % (order.note or "", comment)
        return orders

    @api.multi
    def _check_payment_change_allowed(self):
        """Return True if the user can change the payment of a POS, depending
        of the state of the current session."""
        closed_orders = self.filtered(lambda x: x.session_id.state == "closed")
        if len(closed_orders):
            raise UserError(
                _(
                    "You can not change payments of the POS '%s' because"
                    " the associated session '%s' has been closed!"
                    % (
                        ", ".join(closed_orders.mapped("name")),
                        ", ".join(closed_orders.mapped("session_id.name")),
                    )
                )
            )
