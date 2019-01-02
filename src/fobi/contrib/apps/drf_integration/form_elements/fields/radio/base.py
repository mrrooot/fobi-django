from django.utils.translation import ugettext_lazy as _

from rest_framework.fields import ChoiceField

from .......base import IntegrationFormFieldPlugin
from .......helpers import get_select_field_choices
from .... import UID as INTEGRATE_WITH_UID
from ....base import (
    DRFIntegrationFormElementPluginProcessor,
    DRFSubmitPluginFormDataMixin,
)

from . import UID

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.fields.' \
            'radio.base'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RadioInputPlugin',)


class RadioInputPlugin(IntegrationFormFieldPlugin,
                       DRFSubmitPluginFormDataMixin):
    """ChoiceField plugin."""

    uid = UID
    integrate_with = INTEGRATE_WITH_UID
    name = _("Radio")
    group = _("Fields")

    def get_custom_field_instances(self,
                                   form_element_plugin,
                                   request=None,
                                   form_entry=None,
                                   form_element_entries=None,
                                   **kwargs):
        """Get form field instances."""
        choices = get_select_field_choices(form_element_plugin.data.choices)
        field_kwargs = {
            'required': form_element_plugin.data.required,
            'initial': form_element_plugin.data.initial,
            'label': form_element_plugin.data.label,
            'help_text': form_element_plugin.data.help_text,
            # 'max_length': form_element_plugin.data.max_length,
            'choices': choices,
        }
        return [
            DRFIntegrationFormElementPluginProcessor(
                field_class=ChoiceField,
                field_kwargs=field_kwargs
            )
        ]