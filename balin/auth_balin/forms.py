# -*- coding: utf-8 -*-

from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions


class CreateUserForm(UserCreationForm):

    """
    Form que herda as implementações de `UserCreationForm`
    """

    email = forms.EmailField(
        label=_("Email address")
    )

    is_superuser = forms.BooleanField(
        label=_("Set as Administrator"),
        required=False,
        help_text=_("Define user to Administrador and access all "
                    "funcionalities of system")
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Field('first_name', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('last_name', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('email', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('username', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('password1', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('password2', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('is_superuser'),
            css_class='form-group checkbox'
        ),
        Div(
            FormActions(
                Submit('save', 'Salvar', css_class="btn-lg btn-primary"),
            ),
            css_class='well'
        )
    )

    class Meta(UserCreationForm.Meta):
        fields = ("first_name", "last_name", "username", "email",)


class ChangeUserForm(UserChangeForm):

    """
    Form que herda as implementações de `UserChangeForm`
    """

    email = forms.EmailField(
        label=_("Email address")
    )

    is_superuser = forms.BooleanField(
        label=_("Set as Administrator"),
        required=False,
        help_text=_("Define user to Administrador and access all "
                    "funcionalities of system")
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.layout = Layout(
        Div(
            Field('first_name', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('last_name', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('email', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('username', css_class='form-control'),
            css_class='form-group'
        ),
        Div(
            Field('is_superuser'),
            css_class='form-group, checkbox'
        ),
        Div(
            FormActions(
                Submit('update', 'Atualizar', css_class="btn-lg btn-primary")
            ),
            css_class='well'
        )
    )

    class Meta(UserChangeForm.Meta):
        fields = ("first_name", "last_name", "username", "email",)
        exclude = ("password",)

    def clean_password(self):
        pass
