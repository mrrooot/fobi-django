fobi.contrib.plugins.form_elements.fields.decimal
-------------------------------------------------
A ``Fobi`` Decimal form field plugin. Makes use of the
``django.forms.fields.DecimalField`` and ``django.forms.widgets.NumberInput``
(falling back to ``django.forms.widgets.TextInput`` for older Django
versions).

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.fields.decimal`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.fields.decimal',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
