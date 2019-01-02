fobi.contrib.plugins.form_elements.security.honeypot
----------------------------------------------------
A `Honeypot <http://en.wikipedia.org/wiki/Honeypot_%28computing%29>`_
form field plugin. Just another anti-spam technique.

Installation
~~~~~~~~~~~~
(1) Add ``fobi.contrib.plugins.form_elements.security.honeypot`` to the
    ``INSTALLED_APPS`` in your ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'fobi.contrib.plugins.form_elements.security.honeypot',
            # ...
        )

(2) In the terminal type:

    .. code-block:: sh

        ./manage.py fobi_sync_plugins

(3) Assign appropriate permissions to the target users/groups to be using
    the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
