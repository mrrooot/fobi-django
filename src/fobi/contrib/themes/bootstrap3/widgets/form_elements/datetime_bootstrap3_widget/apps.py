from django.apps import AppConfig

__title__ = 'fobi.contrib.themes.bootstrap3.widgets.form_elements.' \
            'datetime_bootstrap3_widget.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'fobi.contrib.themes.bootstrap3.widgets.form_elements.' \
           'datetime_bootstrap3_widget'
    label = 'fobi_contrib_themes_bootstrap3_widgets_form_elements_' \
            'datetime_bootstrap3_widget'
