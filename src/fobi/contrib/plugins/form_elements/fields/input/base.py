from __future__ import absolute_import

from django.forms.fields import Field
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, get_theme

from . import UID
from .forms import InputForm

__title__ = 'fobi.contrib.plugins.form_elements.fields.input.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('InputPlugin',)

theme = get_theme(request=None, as_instance=True)


class InputPlugin(FormFieldPlugin):
    """Input field plugin."""

    uid = UID
    name = _("Input")
    group = _("Fields")
    form = InputForm

    def get_form_field_instances(self, request=None, form_entry=None,
                                 form_element_entries=None, **kwargs):
        """Get form field instances."""
        widget_attrs = {
            'class': theme.form_element_html_class,
            'placeholder': self.data.placeholder,
            'type': self.data.type_value,
        }

        if self.data.autocomplete_value is not None:
            widget_attrs.update({'autocomplete': 'on'})

        if self.data.autofocus_value is not None:
            widget_attrs.update({'autofocus': 'autofocus'})

        if self.data.disabled_value is not None:
            widget_attrs.update({'disabled': 'disabled'})

        # if self.data.formnovalidate_value:
        #     widget_attrs.update({'formnovalidate': 'formnovalidate'})

        if self.data.list_value is not None:
            widget_attrs.update({'list': self.data.list_value})

        if self.data.max_value is not None:
            widget_attrs.update({'max': self.data.max_value})

        if self.data.min_value is not None:
            widget_attrs.update({'min': self.data.min_value})

        if self.data.multiple_value is not None:
            widget_attrs.update({'multiple': 'multiple'})

        if self.data.pattern_value is not None:
            widget_attrs.update({'pattern': self.data.pattern_value})

        if self.data.readonly_value is not None:
            widget_attrs.update({'readonly': 'readonly'})

        if self.data.step_value is not None:
            widget_attrs.update({'step': self.data.step_value})

        if self.data.type_value and self.data.type_value in ('submit',
                                                             'button',
                                                             'reset',):
            widget_attrs.update({'value': self.data.label})

        field_kwargs = {
            'label': self.data.label
            if self.data.type_value not in ('submit', 'button', 'reset',)
            else '',
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': TextInput(attrs=widget_attrs),
        }
        # if self.data.max_length is not None:
        #     kwargs['max_length'] = self.data.max_length

        return [(self.data.name, Field, field_kwargs)]
