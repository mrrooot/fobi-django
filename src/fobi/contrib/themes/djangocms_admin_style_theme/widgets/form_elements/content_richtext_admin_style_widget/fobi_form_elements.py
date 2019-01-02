from fobi.base import form_element_plugin_widget_registry
from fobi.contrib.plugins.form_elements.content.content_richtext.widgets \
    import (
        BaseContentRichTextPluginWidget
    )
from fobi.contrib.themes.simple import UID

__title__ = 'fobi.contrib.themes.djangocms_admin_style_theme.widgets.' \
            'form_elements.content_richtext_admin_style_widget.' \
            'fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('ContentRichTextPluginWidget',)


class ContentRichTextPluginWidget(BaseContentRichTextPluginWidget):
    """ContentRichText plugin widget for djangocms_admin_style theme."""

    theme_uid = UID


# Registering the widget
form_element_plugin_widget_registry.register(ContentRichTextPluginWidget)
