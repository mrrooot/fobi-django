=======================================================================================
fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget
=======================================================================================
A rich-text widget for the ``content_richtext`` plugin (for Bootstrap 3 theme).

Installation
============
1. Add ``fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget``
   to the ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi.contrib.themes.bootstrap3',
        'fobi.contrib.themes.bootstrap3.widgets.form_elements.content_richtext_bootstrap3_widget',
        'fobi.contrib.plugins.form_elements.content.content_richtext',
        # ...
    )

2. Specify ``bootstrap3`` as a default theme in your ``settings.py``:

.. code-block:: python

    FOBI_DEFAULT_THEME = 'bootstrap3'
