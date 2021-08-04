# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from django.utils.translation import ugettext_lazy as _


class PrintoutsEmailForm(forms.Form):
    to = forms.EmailField(max_length=256, label=_("To"))
    subject = forms.CharField(max_length=256, label=_("Email Subject"))
    body = forms.CharField(max_length=512, widget=forms.Textarea, label=_("Email Body"))
