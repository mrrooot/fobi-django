import os

__title__ = 'fobi.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'CUSTOM_THEME_DATA',
    'DEBUG',
    'DEFAULT_MAX_LENGTH',
    'DEFAULT_THEME',
    'DISPLAY_AUTH_LINK',
    'FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS',
    'FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS',
    'FAIL_ON_ERRORS_IN_FORM_WIZARD_HANDLER_PLUGINS',
    'FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS',
    'FAIL_ON_MISSING_FORM_HANDLER_PLUGINS',
    'FAIL_ON_MISSING_INTEGRATION_FORM_ELEMENT_PLUGINS',
    'FAIL_ON_MISSING_INTEGRATION_FORM_HANDLER_PLUGINS',
    'FORM_CALLBACKS_MODULE_NAME',
    'FORM_ELEMENT_PLUGINS_MODULE_NAME',
    'FORM_HANDLER_PLUGINS_EXECUTION_ORDER',
    'FORM_HANDLER_PLUGINS_MODULE_NAME',
    'FORM_IMPORTER_PLUGINS_MODULE_NAME',
    'FORM_WIZARD_HANDLER_PLUGINS_EXECUTION_ORDER',
    'GET_PARAM_INITIAL_DATA',
    'SORT_PLUGINS_BY_VALUE',
    'INTEGRATION_FORM_ELEMENT_PLUGINS_MODULE_NAME',
    'INTEGRATION_FORM_HANDLER_PLUGINS_MODULE_NAME',
    'RESTRICT_PLUGIN_ACCESS',
    'THEME_FOOTER_TEXT',
    'THEMES_MODULE_NAME',
    'WAIT_AT_TEST_END',
    'WAIT_BETWEEN_TEST_STEPS',
    'WIZARD_FILES_UPLOAD_DIR',
)

# **************************************************************
# **************************************************************
# *************************** Core *****************************
# **************************************************************
# **************************************************************

# If set to True, plugins would be only accessible by the white-listed user(s)
# or group(s). If set to False, all users have the same access rights to all
# plugins.
RESTRICT_PLUGIN_ACCESS = True

# Name of the module in which the fobi form field plugins are registered.
FORM_ELEMENT_PLUGINS_MODULE_NAME = 'fobi_form_elements'

# Name of the module in which the fobi form handler plugins are registered.
FORM_HANDLER_PLUGINS_MODULE_NAME = 'fobi_form_handlers'

# Name of the module in which the fobi integration form element plugins are
# registered.
INTEGRATION_FORM_ELEMENT_PLUGINS_MODULE_NAME = 'fobi_integration_form_elements'

# Name of the module in which the fobi integration form handler plugins are
# registered.
INTEGRATION_FORM_HANDLER_PLUGINS_MODULE_NAME = 'fobi_integration_form_handlers'

# Name of the module in which the fobi form importer plugins are registered.
FORM_IMPORTER_PLUGINS_MODULE_NAME = 'fobi_form_importers'

# Name of the module in which the fobi form calacks are registered.
FORM_CALLBACKS_MODULE_NAME = 'fobi_form_callbacks'

# Name of the module in which the fobi themes are discovered.
THEMES_MODULE_NAME = 'fobi_themes'

# Default theme
DEFAULT_THEME = 'bootstrap3'

# GET param to tell whether initial data shall be loaded.
GET_PARAM_INITIAL_DATA = 'fobi_initial_data'

DISPLAY_AUTH_LINK = True

DEBUG = False

# **************************************************************
# **************************************************************
# ************************ Theme related ***********************
# **************************************************************
# **************************************************************

CUSTOM_THEME_DATA = {}
THEME_FOOTER_TEXT = '&copy; django-fobi example site 2014'

# **************************************************************
# **************************************************************
# *********************** Plugin related ***********************
# **************************************************************
# **************************************************************

DEFAULT_MAX_LENGTH = 255
DEFAULT_MIN_LENGTH = 1

FORM_HANDLER_PLUGINS_EXECUTION_ORDER = (
    'http_repost',
    'mail',
    # The 'db_store' is left out intentionally, since it should
    # be the last plugin to be executed.
)

FORM_WIZARD_HANDLER_PLUGINS_EXECUTION_ORDER = (
    'http_repost',
    'mail',
    # The 'db_store' is left out intentionally, since it should
    # be the last plugin to be executed.
)

SORT_PLUGINS_BY_VALUE = False

FAIL_ON_MISSING_FORM_ELEMENT_PLUGINS = True
FAIL_ON_MISSING_FORM_HANDLER_PLUGINS = True
FAIL_ON_MISSING_INTEGRATION_FORM_ELEMENT_PLUGINS = False
FAIL_ON_MISSING_INTEGRATION_FORM_HANDLER_PLUGINS = False
FAIL_ON_MISSING_FORM_WIZARD_HANDLER_PLUGINS = True
FAIL_ON_ERRORS_IN_FORM_ELEMENT_PLUGINS = False
FAIL_ON_ERRORS_IN_FORM_HANDLER_PLUGINS = False
FAIL_ON_ERRORS_IN_FORM_WIZARD_HANDLER_PLUGINS = False

# **************************************************************
# **************************************************************
# ********************** Wizards related ***********************
# **************************************************************
# **************************************************************

# Relative path. If relative path provided, `MEDIA_ROOT` would be prepended.
WIZARD_FILES_UPLOAD_DIR = os.path.join('fobi_wizards', 'files')

# **************************************************************
# **************************************************************
# ************************ Tests related ***********************
# **************************************************************
# **************************************************************

WAIT_BETWEEN_TEST_STEPS = 2
WAIT_AT_TEST_END = 4
