from django import forms
from django.utils.translation import ugettext_lazy as _

from fobi.base import BaseFormFieldPluginForm, get_theme
from fobi.helpers import validate_initial_for_choices

__title__ = 'fobi.contrib.plugins.form_elements.fields.select.forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RadioInputForm',)

theme = get_theme(request=None, as_instance=True)


class RadioInputForm(forms.Form, BaseFormFieldPluginForm):
    """Form for ``RadioInputPlugin``."""

    plugin_data_fields = [
        ("label", ""),
        ("name", ""),
        ("choices", ""),
        ("help_text", ""),
        ("initial", ""),
        ("required", False)
    ]

    label = forms.CharField(
        label=_("Label"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    name = forms.CharField(
        label=_("Name"),
        required=True,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    choices = forms.CharField(
        label=_("Choices"),
        required=True,
        help_text=_("Enter single values/pairs per line. Example:<code><br/>"
                    "&nbsp;&nbsp;&nbsp;&nbsp;1<br/>"
                    "&nbsp;&nbsp;&nbsp;&nbsp;2<br/>"
                    "&nbsp;&nbsp;&nbsp;&nbsp;alpha, Alpha<br/>"
                    "&nbsp;&nbsp;&nbsp;&nbsp;beta, Beta<br/>"
                    "&nbsp;&nbsp;&nbsp;&nbsp;omega"
                    "</code><br/>"
                    "It finally transforms into the following HTML "
                    "code:<code><br/>"
                    '&nbsp;&nbsp;&nbsp;&nbsp;'
                    '&lt;select id="id_NAME_OF_THE_ELEMENT" '
                    'name="NAME_OF_THE_ELEMENT"&gt;<br/>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                    '&lt;option value="1"&gt;1&lt;/option&gt;<br/>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                    '&lt;option value="2"&gt;2&lt;/option&gt;<br/>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                    '&lt;option value="alpha"&gt;Alpha&lt;/option&gt;<br/>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                    '&lt;option value="beta"&gt;Beta&lt;/option&gt;<br/>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                    '&lt;option value="omega"&gt;omega&lt;/option&gt;<br/>'
                    '&nbsp;&nbsp;&nbsp;&nbsp;&lt;/select&gt;'
                    "</code>"),
        widget=forms.widgets.Textarea(
            attrs={'class': theme.form_element_html_class}
        )
    )
    help_text = forms.CharField(
        label=_("Help text"),
        required=False,
        widget=forms.widgets.Textarea(
            attrs={'class': theme.form_element_html_class}
        )
    )
    initial = forms.CharField(
        label=_("Initial"),
        required=False,
        widget=forms.widgets.TextInput(
            attrs={'class': theme.form_element_html_class}
        )
    )
    required = forms.BooleanField(
        label=_("Required"),
        required=False,
        widget=forms.widgets.CheckboxInput(
            attrs={'class': theme.form_element_checkbox_html_class}
        )
    )

    def clean_initial(self):
        """Validating the initial value."""
        return validate_initial_for_choices(self, 'choices', 'initial')
        #
        # availalble_choices = dict(
        #     get_select_field_choices(self.cleaned_data['choices'])
        #     ).values()
        #
        # if not self.cleaned_data['initial'] in availalble_choices:
        #     raise forms.ValidationError(
        #         _("Invalid value for initial! Should be any of the "
        #           "following: {0}".format(','.join(availalble_choices)))
        #         )
        # return self.cleaned_data['initial']
