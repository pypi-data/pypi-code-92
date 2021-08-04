# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms

from shuup.admin.utils.views import CreateOrUpdateView
from shuup.core.models import Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        exclude = ()


class CurrencyEditView(CreateOrUpdateView):
    model = Currency
    form_class = CurrencyForm
    template_name = "shuup/admin/currencies/edit_currency.jinja"
    context_object_name = "currency"
    add_form_errors_as_messages = True
