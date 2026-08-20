"""
skilredi_keyterms_app Django application initialization.
"""

from django.apps import AppConfig
from edx_django_utils.plugins.constants import PluginURLs, PluginSettings
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

class KeytermsDjangoAppConfig(AppConfig):
    """
    Configuration for the skilredi_keyterms_app Django application.
    """

    name = 'skilredi_keyterms_app'

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {

        # Configuration setting for Plugin URLs for this app.
        'url_config': {

            'lms.djangoapp': {
                'namespace': name,
                'regex': '^api/keyterms/',
                'relative_path': 'urls',
            }
        }
    }
