from .base import *

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR('../db/example_djangocms_2.db'),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS += [
    'cms',  # DjangoCMS
    'mptt',
    'menus',
    'sekizai',
    # 'djangocms_admin_style',

    # Some plugins
    'cms.plugins.picture',
    'cms.plugins.snippet',

    'fobi.contrib.apps.djangocms_integration',  # Fobi DjangoCMS app

    # 'djangocms_page',  # Example
]

try:
    # INSTALLED_APPS.remove('admin_tools') \
    #    if 'admin_tools' in INSTALLED_APPS else None
    # INSTALLED_APPS.remove('admin_tools.menu') \
    #    if 'admin_tools.menu' in INSTALLED_APPS else None
    INSTALLED_APPS.remove('admin_tools.dashboard') \
        if 'admin_tools.dashboard' in INSTALLED_APPS else None
except Exception as err:
    pass

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES += [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)
TEMPLATE_CONTEXT_PROCESSORS += [
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    # 'cms.context_processors.cms_settings',
]

FOBI_DEFAULT_THEME = 'bootstrap3'
# FOBI_DEFAULT_THEME = 'foundation5'
# FOBI_DEFAULT_THEME = 'simple'

CMS_TEMPLATES = (
    ('cms_page/{0}/page_with_sidebar.html'.format(FOBI_DEFAULT_THEME),
     'General template with sidebar for {0}'.format(FOBI_DEFAULT_THEME)),
    ('cms_page/{0}/page_without_sidebar.html'.format(FOBI_DEFAULT_THEME),
     'General template without sidebar for {0}'.format(FOBI_DEFAULT_THEME)),
)

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',
}

LANGUAGE_CODE = 'en'

# FEINCMS_RICHTEXT_INIT_CONTEXT = {
#    'TINYMCE_JS_URL': STATIC_URL + 'tiny_mce/tiny_mce.js',
# }
